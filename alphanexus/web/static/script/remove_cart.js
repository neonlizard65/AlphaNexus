function removeCart(user, product, other_products){

    let cart = [];

    for(let other_product of other_products){
        if(other_product != product){
            cart.push("http://127.0.0.1:8000/api/products/"+other_product + '/');
        }
    }


    url = '/api/users/'+user+'/';
    fetch(url, {
        method: "PATCH",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({cart: cart}),
    })
    .then((response)=>{
        return response.json();
    })
    .then((data) => {
        console.log('data:', data);
        location.reload();
    })
}