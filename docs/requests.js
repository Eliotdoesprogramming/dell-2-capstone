


// select the text inside of a text input with the id modelurl1 using jquery

let predPizza = (url) => {
    console.log(url)
    //make a request to localhost:5000/pizza with a json object containing the url
    //the server should return a json object with the name of the pizza
    $.ajax({
        url: 'http://localhost:5000/pizza',
        type: 'POST',
        data: {
            img: url
        },
        success: function(data) {
            console.log(data)
            //update the text input with the name of the pizza
            $('#model1result').append(`<h1>Result: <span class="${data.is_pizza == 'True'? 'badge badge-success': 'badge badge-danger'}">${data.is_pizza == 'True'? 'pizza': 'not pizza'}</span></h1>`) 
        }
}

$('#submit1').click(()=>{
    let url = $('#modelurl1').val()
    predPizza(url)
})