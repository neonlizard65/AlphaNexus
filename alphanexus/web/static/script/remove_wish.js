function removeWish(user, product, other_products){

    let wishlist = [];

    for(let other_product of other_products){
        if(other_product != product){
            wishlist.push("http://127.0.0.1:9190/api/products/"+other_product + '/');
        }
    }

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