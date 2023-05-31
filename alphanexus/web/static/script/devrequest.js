function sendRequest(user, dev){
    $.ajax({
        type: "POST",
        url: '/api/developerrequests/',
        data: {
            user: "http://127.0.0.1:8000/api/users/"+user+'/',
            developer: "http://127.0.0.1:8000/api/developers/"+dev+'/',
            approved: null
        },
        success: function(data){
            console.log( 'success, server says '+data);
        },
        error: function(data){
            console.log( 'failure, server says '+data);
        }
    });
    button = document.getElementById("btn-"+dev);
    button.style.display = "none";
    join_block = document.getElementById("join-block-"+dev);
    join_block.innerHTML = "<h4>Заявка подана.</h4>";
}