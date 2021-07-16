$.ajax({
    url: "refresh.html",
    type: "post",
    data: send,
    dataType: 'json',
    success: function(data){
        console.log(data);
        console.log(data.id);   
    }
});