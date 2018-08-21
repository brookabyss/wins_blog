$(document).ready(function(){
console.log("heelo")

let time_out_ID, p_id = 0,
time =4000
let person_image = $('#person_image'), fun_fact = $('#fun-fact'), image_carousel = true;




personnel = JSON.parse(personnel)

let base_url ="http://localhost:8000/hub"


function changePerson(i){
  console.log("changing image")
  person_image.attr('src',"/personnel"+personnel[i].profile_image)
  let p = $("<p>"+personnel[i].fun_fact+"</p>")
  fun_fact.html(p)


}

function profileCarousel(){
  if (!image_carousel)return;

    if(p_id < personnel.length){
      changePerson(p_id)
    }
    else{
      p_id = 0
      changePerson(p_id)
    }
    p_id ++
    time_out_ID=setTimeout(function(){
      profileCarousel()
    },time)

}

profileCarousel()

$(document).on('click','.profile-div',function(){

console.log("cleared time out")

image_carousel = false;
clearTimeout(time_out_ID)



})





})
