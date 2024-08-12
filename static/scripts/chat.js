
//CHAT

$("#messageArea").on("submit", function(event) {
  const date = new Date();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const str_time = hour+":"+minute;
  var rawText = $("#text").val();

  var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time + '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
  
  $("#text").val("");
  $("#messageFormeight").append(userHtml);

  $.ajax({
    data: {
      msg: rawText,	
    },
    type: "POST",
    url: "/get",
  }).done(function(data) {
    var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="/static/assets/GG.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + data + '<span class="msg_time">' + str_time + '</span></div></div>';
    $("#messageFormeight").append($.parseHTML(botHtml));
  });
  event.preventDefault();
});

// Scoll Chat
let pastMessages = 0;
let chat = document.getElementById("messageFormeight");

chat.addEventListener("mouseover", () =>{
  let curMessages = chat.childElementCount;
  console.log();
  (curMessages)
  let shouldScroll = chat.scrollTop + chat.clientHeight !== chat.scrollHeight;

  if((pastMessages != curMessages) && shouldScroll){

    chat.scrollTo({
      top:chat.scrollHeight,
      behavior:"smooth",
    });
    // chat.scrollTop = chat.scrollHeight;
    pastMessages =  curMessages;
  }
})


//Side Experts

function Localize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the local impacts and variables. Local causal variables are immediate and can quickly be observed. For this response only, use friendly language, like a neighbor or friend."
  expertRequest("Local",query);
}

function Municipalize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the Municipal impacts and variables. Municiapl causal variables are not as noticeable but affect the larger community. For this response only, use teacherly language like a teacher or principal."
  expertRequest("Municipal",query);
}

function Nationalize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the National impacts and variables. National causal variables are a result of compounding multiple fo the same event. This affects the entire country. For this response only, use political language like a politician or governor."
  expertRequest("National",query);
}

function Globalize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the Global impacts and variables. Global causal variables are geopolitical in context and are a result of competing elements. This affects the entire world. For this response only, use powerful language like a PHD expert or a President."
  expertRequest("Global",query);
  
}

function Economize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the Economical impacts and variables. Economical causal variables are about the stock market, access to resources, the performacne of comapnies and cash flow. Economical impacts can be as small as local business or large as international conglomerates. For this response only, use investor language like an investment banker or a salesman."
  expertRequest("Economical",query);
  
}

function Ecologize(){
  let query = "If possible, regenerate another set of cause and effects. However, this time, have a focus on the Ecological impacts and variables. Ecological causal variables are about the local enviroment, global enviroment, biosphere, small and big organisim. Ecological impacts are complex and can occur immediately or over hundres of years through evolution. For this response only, use warm-stoic language like an enviromental engineer."
  expertRequest("Ecological",query);
}


// Specified Expert Request, Council of ELders
function expertRequest(expert, prompt){
  const date = new Date();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const str_time = hour+":"+minute;
  let rawText = prompt;

  var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="/static/assets/GG_'+ expert +'.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer"> Attempting to Find the ' + expert + ' impact.<span class="msg_time">' + str_time + '</span></div></div>';

  $("#messageFormeight").append($.parseHTML(botHtml));

  $.ajax({
    data: {
      msg: rawText,	
    },
    type: "POST",
    url: "/get",
  }).done(function(data) {
    var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="/static/assets/GG_'+ expert +'.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + data + '<span class="msg_time">' + str_time + '</span></div></div>';
    $("#messageFormeight").append($.parseHTML(botHtml));
  });
  event.preventDefault();

}

let allButtons = document.querySelectorAll('div.side-body > button');
let btnFuncs = [Localize, Municipalize, Nationalize, Globalize, Economize, Ecologize]

for (let i = 0; i < allButtons.length; i++) {
  allButtons[i].addEventListener('click', btnFuncs[i])
}

















// let userInput = document.getElementById("chatbox");
// input.addEventListener("keypress", function(event) {
//   // If the user presses the "Enter" key on the keyboard
//   if (event.key === "Enter") {
//     // Cancel the default action, if needed
//     event.preventDefault();
//     // Trigger the button element with a click
//     document.getElementById("myBtn").click();
//   }
// });




