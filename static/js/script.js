$(function(){


  console.log("working")

  $("#submit-word").on("submit", async function(event){
    console.log("submit button");

    event.preventDefault()

    let word = $("#word-guess").val();

    await axios.post(`/guesses`, {
      word
    })
  })


})

