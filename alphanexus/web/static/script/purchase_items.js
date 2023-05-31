//Молюсь богу джаваскрипта, что все сработает

//Все операции при покупке
async function purchase(user, cart, wishlist, sum){
    
    let remaining_wishlist = [];
    
    let unique_wishlist = wishlist.filter((obj) => cart.indexOf(obj) === -1);
    
    for(let unique_game of unique_wishlist){
        remaining_wishlist.push("http://127.0.0.1:8000/api/products/"+unique_game + '/');
    }
    
    for(let game of cart){
        let key = await add_cdkey(game);
        //Обязательно нужно задержку,чтобы POST запрос успел обработаться
        await delay(100); //Проверить на множество товаров, возможно, чем больше товаров, тем больше нужно ждать
        await add_library(user, game, key);
        add_check(user, sum, cart)
    }

    
    clear_cart(user);
    clear_wishlist(user, remaining_wishlist);
    
    document.location.href = "library";
}

//Генерирует уникальный CD ключ
async function generate_key() {
    while(true){
        let result = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        const charactersLength = characters.length;

        let counter = 0;
        while (counter < 20) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
            counter += 1;
        }

        const check_cd = async () => { 
            const response = await fetch("http://127.0.0.1:8000/api/cdkeys/?content="+result);
            return response.json();
        }

        let answer = await check_cd();

        if(answer.length == 0){
            return result;
        }
    }
}

//Добавление ключа в БД
async function add_cdkey(product){
    let key = await generate_key();
    url = "http://127.0.0.1:8000/api/cdkeys/";
    fetch(url, {
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({
            content: key, 
            is_redeemed: true,
            product: "http://127.0.0.1:8000/api/products/"+product + '/'
        }),
    })
    return key;
}

//Добавление в библиотеку пользователя
async function add_library(user, product, key){

    url = "http://127.0.0.1:8000/api/cdkeys/?content="+key;
    const response = await fetch(url);
    console.log(response);
    const key_link = await response.json();

    console.log(key_link);
    var url = "http://127.0.0.1:8000/api/libraries/";
    
    await fetch(url, {
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({
            user: "http://127.0.0.1:8000/api/users/"+user + '/',
            product: "http://127.0.0.1:8000/api/products/"+product + '/',
            cdkey: key_link[0].url
        }),
    })
}


function add_check(user, sum, cart){
    const date = new Date();
    let games = [];
    for(let game of cart){
        games.push("http://127.0.0.1:8000/api/products/"+game + '/');
    }
    url = "http://127.0.0.1:8000/api/checks/";
    fetch(url, {
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({
            user: "http://127.0.0.1:8000/api/users/"+user + '/',
            total: sum,
            date: date,
            games: games
        }),
    })

}

//Важно!
function delay(millisec) {
    return new Promise(resolve => {
        setTimeout(() => { resolve('') }, millisec);
    })
}

function clear_cart(user){
    //Удаляем из корзины
    new_cart = []
    url = '/api/users/'+user+'/';
    fetch(url, {
        method: "PATCH",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({cart: new_cart}),
    })
    .then((response)=>{
        return response.json();
    })
}

function clear_wishlist(user, remaining_wishlist){
    //Удаляем из списка желаемых
    new_cart = []
    url = '/api/users/'+user+'/';
    fetch(url, {
        method: "PATCH",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({wishlist: remaining_wishlist}),
    })
    .then((response)=>{
        return response.json();
    })
}