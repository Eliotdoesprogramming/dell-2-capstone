
// select the text inside of a text input with the id modelurl1 using jquery
let predPizza = (url) => {
        console.log(url)
        //make a request to localhost:5000/pizza with a json object containing the url
        //the server should return a json object with the name of the pizza
        $.ajax({
            url: 'http://18.116.242.75/pizza',
            type: 'POST',
            data: url,
            success: function(data) {
                //update the text input with the name of the pizza
                $('#model1result').empty();
                if(data.is_pizza){
                    $('#model1result').append(`<h1>Result: <span class="${data.is_pizza == 'True'? 'badge bg-success': 'badge bg-danger'}">${data.is_pizza == 'True'? 'pizza': 'not pizza'}</span></h1>`)
                }
                else {
                    $('#model1result').append(`<h1>Error..</h1>`)
                }   
            }
    })
}
$('#submit1').click(()=>{
    let url = $('#modelurl1').val()
    predPizza(url)
})
console.log('loaded....')

let predTen = (url) => {
    console.log(url)
    //make a request to localhost:5000/pizza with a json object containing the url
    //the server should return a json object with the name of the pizza
    $.ajax({
        url: 'http://localhost:5000/tenfood',
        type: 'POST',
        data: url,
        success: function(data) {
            //update the text input with the name of the pizza
            $('#model2result').empty();
            if(data.food){
                $('#mode2result').append(`<h1>Result: <span class="badge bg-success">${data.food}</span></h1>`)
            }
            else {
                $('#model2result').append(`<h1>Error..</h1>`)
            }   
        }
})
}
$('#submit2').click(()=>{
let url = $('#modelurl2').val()
predTen(url)
})