from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """

<!DOCTYPE html>

<html>
<head>
    <title>Conversational Care Engine</title>

```
<style>
    body{
        font-family: Arial, sans-serif;
        background:#f4f6f8;
        margin:0;
        padding:0;
    }

    .container{
        max-width:800px;
        margin:40px auto;
        background:white;
        padding:20px;
        border-radius:10px;
        box-shadow:0 2px 10px rgba(0,0,0,0.1);
    }

    h1{
        text-align:center;
        color:#2c3e50;
    }

    #chatbox{
        height:400px;
        overflow-y:auto;
        border:1px solid #ddd;
        padding:15px;
        margin-bottom:15px;
        border-radius:8px;
    }

    .user{
        text-align:right;
        margin:10px;
        color:#1565c0;
        font-weight:bold;
    }

    .bot{
        text-align:left;
        margin:10px;
        color:#2e7d32;
        font-weight:bold;
    }

    input{
        width:80%;
        padding:10px;
    }

    button{
        padding:10px 20px;
        cursor:pointer;
    }
</style>
```

</head>

<body>

<div class="container">

<h1>Conversational Care Engine</h1>

<div id="chatbox"></div>

<input
type="text"
id="message"
placeholder="Ask a health question..."

>

<button onclick="sendMessage()">
    Send
</button>

</div>

<script>

function getResponse(message){

    let text = message.toLowerCase();

    if(text.includes("diabetes")){
        return "Monitor blood sugar regularly and maintain a balanced diet.";
    }

    if(text.includes("thyroid")){
        return "Take prescribed medication consistently and schedule regular thyroid tests.";
    }

    if(text.includes("obesity")){
        return "Increase physical activity and follow a calorie-controlled diet.";
    }

    return "Could you provide more information about your symptoms or health goals?";
}

function sendMessage(){

    let input = document.getElementById("message");

    let message = input.value.trim();

    if(message === ""){
        return;
    }

    let chatbox = document.getElementById("chatbox");

    chatbox.innerHTML +=
        "<div class='user'>You: " +
        message +
        "</div>";

    let reply = getResponse(message);

    setTimeout(function(){

        chatbox.innerHTML +=
            "<div class='bot'>Assistant: " +
            reply +
            "</div>";

        chatbox.scrollTop =
            chatbox.scrollHeight;

    },500);

    input.value = "";
}

</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
return html
