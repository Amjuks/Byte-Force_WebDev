document.getElementById('send-btn').addEventListener('click', function() {
    let userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== "") {
        let chatBox = document.getElementById('chat-box');

        // Create and append user message
        let newUserMessage = document.createElement('div');
        newUserMessage.classList.add('user-message');
        newUserMessage.textContent = "You: " + userInput;
        chatBox.appendChild(newUserMessage);

        // Clear input field
        document.getElementById('user-input').value = '';

        // Scroll to the bottom after adding the message
        chatBox.scrollTop = chatBox.scrollHeight;

        // Simulate a bot response after 1 second
        setTimeout(function() {
            let newBotMessage = document.createElement('div');
            newBotMessage.classList.add('bot-message');
            newBotMessage.textContent = "Bot: " + "Hello! How can I help you today?";
            chatBox.appendChild(newBotMessage);
            
            // Scroll to the bottom after bot's response
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 1000);
    }
});
