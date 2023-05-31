function addWish(user, product, other_products){

    let wishlist = [];

    for(let other_product of other_products){
        wishlist.push("http://127.0.0.1:8000/api/products/"+other_product + '/');
    }
    wishlist.push("http://127.0.0.1:8000/api/products/"+product+'/');

    console.log({wishlist: wishlist});
    url = '/api/users/'+user+'/';
    fetch(url, {
        method: "PATCH",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },  
        body: JSON.stringify({wishlist: wishlist}),
    })
    .then((response)=>{
        return response.json();
    })
    .then((data) => {
        console.log('data:', data);
        location.reload();
    })
}