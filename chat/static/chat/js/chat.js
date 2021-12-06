var roomName = JSON.parse(document.getElementById('room_name').textContent)
var username = JSON.parse(document.getElementById('username').textContent)

var test  = 'test';

var chatSocket = new ReconnectingWebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    // Getting Data
    var data = JSON.parse(e.data);
    var message = data['message'];
    var author = data['author'];
    var timestamp = data['timestamp'];

    // Creating html for message
    var liMsg = document.createElement('li');
    var div1Msg = document.createElement('div');
    var spanMsg = document.createElement('span');
    spanMsg.textContent = timestamp;
    var div2Msg = document.createElement('div');
    div2Msg.textContent = message.content;

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
        'from' : username
    }));
    messageInputDom.value = '';
};