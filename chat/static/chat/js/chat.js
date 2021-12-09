var roomName = JSON.parse(document.getElementById('room_name').textContent)
var username = JSON.parse(document.getElementById('username').textContent)

var wsStart = (location.protocol == 'https:') ? 'wss://' : 'ws://'

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
    spanMsg.className = getDateTime(new Date());

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

function getDateTime(date) {
    // gets the hours
    var hours = date.getHours();
    // gets the day
    var days = date.getDay();
    // gets the month
    var minutes = date.getMinutes();
    // gets AM/PM
    var ampm = hours >= 12 ? 'pm' : 'am';
    // converts hours to 12 hour instead of 24 hour
    hours = hours % 12;
    // converts 0 (midnight) to 12
    hours = hours ? hours : 12; // the hour '0' should be '12'
    // converts minutes to have leading 0
    minutes = minutes < 10 ? '0'+ minutes : minutes;
  
    // the time string
    var time = hours + ':' + minutes + ' ' + ampm;
  
    // gets the match for the date string we want
    var match = date.toString().match(/\w{3} \w{3} \d{1,2} \d{4}/);
  
    //the result
    return match[0] + ' ' + time;
}
