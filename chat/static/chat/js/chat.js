var roomName = JSON.parse(document.getElementById('room_name').textContent)
var username = JSON.parse(document.getElementById('username').textContent)

var wsStart = (location.protocol == 'https:') ? 'wss://' : 'ws://'

console.log(wsStart)
console.log(location.protocol)
console.log(location.protocol == 'https')


var chatSocket = new ReconnectingWebSocket(
    wsStart
    + window.location.host
    + '/ws/chat/room/'
    + roomName
    + '/'
);

chatSocket.onopen = function(e) {
    fetchMessages();
}

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    if (data['command'] === 'messages') {
      for (let i=0; i<data['messages'].length; i++) {
        createMessage(data['messages'][i]);
      }
    } else if (data['command'] === 'new_message'){
      createMessage(data['message']);
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();

document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'command' : 'new_message',
        'message' : message,
        'author' : username,
        'room' : roomName
    }));
    messageInputDom.value = '';
};

function fetchMessages() {
    chatSocket.send(JSON.stringify({
        'command' : 'fetch_messages',
        'room': roomName,
     }));
}

function createMessage(data) {
    var message = data.content;
    var author = data.author;
    var timestamp = data.timestamp;

    // Creating html for message
    var liMsg = document.createElement('li');
    var div1Msg = document.createElement('div');
    var spanMsg = document.createElement('span');
    spanMsg.textContent = timestamp;
    var div2Msg = document.createElement('div');
    div2Msg.textContent = message;

    liMsg.className = 'clearfix';
    spanMsg.className = "message-data-time";

    if (author === username) {
        div1Msg.className = 'message-data';
        div2Msg.className = 'message my-message';
    } else {
        div1Msg.className = 'message-data d-flex justify-content-end';
        div2Msg.className = 'message other-message float-right';  
    }

    liMsg.appendChild(div1Msg);
    liMsg.appendChild(div2Msg);
    div1Msg.appendChild(spanMsg)

    document.querySelector('#chat-log').appendChild(liMsg);
}
