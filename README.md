# Simple Chatbot

A basic conversational chatbot built with Python. This chatbot can respond to common greetings and questions using pattern matching.

## Features

- ✨ Simple pattern matching for user inputs
- 💬 Interactive chat interface
- 🔧 Easy to customize and extend
- ⚡ No external dependencies required for basic functionality
- 🛡️ Error handling for robust operation

## Installation

**Requirements:** Python 3.6 or higher

```bash
# Clone the repository
git clone https://github.com/guptaniket62-bot/chatbot.git
cd chatbot

# Optional: Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

Run the chatbot:

```bash
python3 chatbot.py
```

Then start chatting! Here are some example commands:

- `hello` - Greet the bot
- `how are you` - Ask how the bot is doing
- `what is your name` - Get the bot's name
- `what time is it` - Get current time
- `help` - Show available commands
- `bye` or `exit` - Exit the chatbot

## Example Session

```
ChatBot: Hello! I'm ChatBot. Type 'help' for available commands or 'bye' to exit.

You: hello
ChatBot: Hello! How can I help you today?

You: what is your name
ChatBot: I'm ChatBot, your virtual assistant!

You: what time is it
ChatBot: It's currently 14:32:45

You: bye
ChatBot: Goodbye! Have a great day!
```

## Code Structure

- `chatbot.py` - Main chatbot implementation
  - `SimpleChatbot` class - Core chatbot logic
  - Pattern matching using regex
  - Interactive chat loop

## Customization

### Adding New Responses

Edit the `responses` dictionary in the `SimpleChatbot` class:

```python
self.responses = {
    r"your pattern": "Your response",
    r"another pattern|alternative": "Another response",
}
```

### Changing the Bot's Name

```python
chatbot = SimpleChatbot("YourBotName")
```

## Project Structure

```
chatbot/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Future Enhancements

- 🤖 Integration with NLP libraries (NLTK, spaCy)
- 💾 Database for storing conversations
- 🌐 Web interface using Flask or FastAPI
- 🧠 Machine learning capabilities
- ���� Conversation analytics
- 🔌 API integrations for dynamic responses

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have suggestions, please open an [issue](https://github.com/guptaniket62-bot/chatbot/issues) on GitHub.

## Author

Created by [@guptaniket62-bot](https://github.com/guptaniket62-bot)
