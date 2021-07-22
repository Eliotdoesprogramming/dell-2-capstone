


// select the text inside of a text input with the id modelurl1 using jquery

let predPizza = (url) => {
    console.log(url)
}

$('#submit1').click(()=>{
    let url = $('#modelurl1').val()
    predPizza(url)
})