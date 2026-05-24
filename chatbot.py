#!/usr/bin/env python3
"""
Simple Chatbot - A basic conversational chatbot
"""

import re
from datetime import datetime


class SimpleChatbot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.responses = {
            r"hello|hi|hey": "Hello! How can I help you today?",
            r"how are you": "I'm doing great, thanks for asking! How about you?",
            r"what is your name": f"I'm {self.name}, your virtual assistant!",
            r"what time is it": f"It's currently {datetime.now().strftime('%H:%M:%S')}",
            r"goodbye|bye|exit|quit": "Goodbye! Have a great day!",
            r"help": self.get_help(),
            r"who created you": "I was created as a simple chatbot example.",
            r"thanks|thank you": "You're welcome! Happy to help.",
        }

    def get_help(self):
        return """
Here are some things you can ask me:
- Hello/Hi
- How are you?
- What is your name?
- What time is it?
- Help
- Goodbye/Bye
- Exit/Quit
"""

    def get_response(self, user_input):
        """Generate a response based on user input"""
        user_input = user_input.lower().strip()

        # Check for matching patterns
        for pattern, response in self.responses.items():
            if re.search(pattern, user_input):
                return response

        # Default response if no pattern matches
        return f"That's interesting! I didn't quite understand. Type 'help' for available commands."

    def chat(self):
        """Start an interactive chat session"""
        print(f"\n{self.name}: Hello! I'm {self.name}. Type 'help' for available commands or 'bye' to exit.\n")

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")

                # Exit conditions
                if re.search(r"goodbye|bye|exit|quit", user_input.lower()):
                    break

            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye!")
                break
            except Exception as e:
                print(f"{self.name}: An error occurred: {str(e)}\n")


def main():
    """Main entry point"""
    chatbot = SimpleChatbot("ChatBot")
    chatbot.chat()


if __name__ == "__main__":
    main()
