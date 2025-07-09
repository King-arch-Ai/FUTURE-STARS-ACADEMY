function getGreetingReply(): string {
    const replies = [
      "Hey there! ⚽ How can I assist you today?",
      "Hi! Need any help?",
      "Hello! 👋",
      "Hey! What's up?"
    ];
    return replies[Math.floor(Math.random() * replies.length)];
  }
  
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.onresult = (event) => {
    const spokenText = event.results[0][0].transcript;
    sendMessage(spokenText);
  };
  recognition.start();
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.onresult = (event) => {
  const spokenText = event.results[0][0].transcript;
  sendMessage(spokenText);
};
recognition.start();

    