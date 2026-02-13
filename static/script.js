document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    appendMessage(userMessage, 'user-message');
    userInput.value = '';

    // Show a loading indicator
    const loadingMessageId = appendLoadingMessage();

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        removeLoadingMessage(loadingMessageId);
        appendMessage(data.response, 'bot-message');
    })
    .catch(error => {
        console.error('Error:', error);
        removeLoadingMessage(loadingMessageId);
        appendMessage('Sorry, something went wrong. Please try again.', 'bot-message');
    });
}

function appendMessage(message, type) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

let loadingInterval;
function appendLoadingMessage() {
    const chatBox = document.getElementById('chat-box');
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot-message loading';
    loadingDiv.textContent = 'Typing...';
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    // Simple animation for typing indicator
    loadingInterval = setInterval(() => {
        const currentText = loadingDiv.textContent;
        loadingDiv.textContent = currentText === 'Typing...' ? 'Typing..' : currentText === 'Typing..' ? 'Typing.' : 'Typing...';
    }, 500);

    return loadingDiv;
}

function removeLoadingMessage(loadingDiv) {
    clearInterval(loadingInterval);
    loadingDiv.remove();
}
