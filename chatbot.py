#!/usr/bin/env python3
"""
Travel Agent Chatbot - Your AI-powered travel assistant
"""

import re
from datetime import datetime


class TravelAgentChatbot:
    def __init__(self, name="Travel Assistant"):
        self.name = name
        self.destinations = {
            "paris": {
                "country": "France",
                "season": "Spring (Apr-May) or Fall (Sep-Oct)",
                "attractions": "Eiffel Tower, Louvre Museum, Notre-Dame",
                "cost": "$$$ (Moderate to High)",
                "duration": "5-7 days recommended"
            },
            "tokyo": {
                "country": "Japan",
                "season": "Spring (Apr-May) or Fall (Oct-Nov)",
                "attractions": "Tokyo Tower, Senso-ji Temple, Shibuya Crossing",
                "cost": "$$$ (High)",
                "duration": "7-10 days recommended"
            },
            "bali": {
                "country": "Indonesia",
                "season": "April-October (Dry season)",
                "attractions": "Beaches, Ubud Temples, Mount Batur",
                "cost": "$$ (Budget-friendly)",
                "duration": "5-7 days recommended"
            },
            "new york": {
                "country": "USA",
                "season": "Fall (Sep-Oct) or Spring (Apr-May)",
                "attractions": "Statue of Liberty, Times Square, Central Park",
                "cost": "$$$ (High)",
                "duration": "5-7 days recommended"
            },
            "london": {
                "country": "United Kingdom",
                "season": "Summer (Jun-Aug) or Spring (Apr-May)",
                "attractions": "Big Ben, Tower of London, Buckingham Palace",
                "cost": "$$$ (Moderate to High)",
                "duration": "5-7 days recommended"
            },
            "dubai": {
                "country": "UAE",
                "season": "November-March",
                "attractions": "Burj Khalifa, Desert Safari, Gold Souk",
                "cost": "$$$ (High)",
                "duration": "4-5 days recommended"
            },
            "bangkok": {
                "country": "Thailand",
                "season": "November-February",
                "attractions": "Grand Palace, Floating Markets, Temples",
                "cost": "$$ (Budget-friendly)",
                "duration": "4-5 days recommended"
            },
            "barcelona": {
                "country": "Spain",
                "season": "May-June or September-October",
                "attractions": "Sagrada Familia, Park Güell, Gothic Quarter",
                "cost": "$$ (Moderate)",
                "duration": "4-5 days recommended"
            }
        }

        self.travel_tips = [
            "Always book flights 2-3 months in advance for better prices",
            "Check visa requirements before booking your trip",
            "Purchase travel insurance for peace of mind",
            "Pack light to save on baggage fees",
            "Download offline maps before traveling",
            "Inform your bank about travel dates to avoid card blocks",
            "Book accommodations with free cancellation policies",
            "Use public transportation to explore like a local"
        ]

        self.responses = {
            r"hello|hi|hey|welcome": self.greeting(),
            r"what is your name|who are you": f"I'm {self.name}, your personal AI travel assistant! Ready to help you plan an amazing trip.",
            r"how are you": "I'm doing great! Excited to help you explore the world! 🌍",
            r"popular destinations|where should i go|recommend a destination": self.get_popular_destinations(),
            r"paris|tokyo|bali|new york|london|dubai|bangkok|barcelona": self.destination_info(),
            r"travel tips|tips for traveling|travel advice": self.get_random_tip(),
            r"how much does it cost|budget|price": "Destinations vary in cost. Budget destinations like Bali and Bangkok are $$ (50-100/day). Mid-range like Barcelona are $$ (100-150/day). Premium like Paris and Tokyo are $$$ (150+/day). Tell me a destination!",
            r"what to pack|packing list": "Pack: Passport, travel documents, comfortable shoes, weather-appropriate clothes, toiletries, phone charger, travel adapters, medications, and travel insurance documents.",
            r"best time to visit|when to go|best season": "Depends on the destination! Spring and Fall are generally best for most places. Mention a destination for specific recommendations!",
            r"how do i book|booking|reserve|book a trip": "I can help! Tell me: 1) Destination 2) Travel dates 3) Budget. I'll provide recommendations for flights, hotels, and activities!",
            r"help": self.get_help(),
            r"goodbye|bye|exit|quit|thanks": "Thank you for using Travel Assistant! Have a wonderful journey! ✈️",
            r"what about visa|visa requirements": "Visa requirements vary by country and your nationality. Visit your country's embassy website or let me know your destination!",
            r"travel insurance": "Travel insurance is highly recommended! It covers medical emergencies, trip cancellations, lost luggage, and more. Budget 5-10% of your trip cost.",
            r"currency|exchange rate": "Exchange rates fluctuate daily. Check XE.com or OANDA for current rates. Always notify your bank before traveling internationally.",
        }

    def greeting(self):
        hour = datetime.now().hour
        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        return f"{greeting}! Welcome to Travel Assistant! I'm here to help you plan your perfect getaway. 🌴✈️"

    def get_popular_destinations(self):
        destinations_list = ", ".join(list(self.destinations.keys())[:5]).title()
        return f"Popular destinations include: {destinations_list} and more! Which destination interests you?"

    def destination_info(self):
        """Get destination info based on user input"""
        return "I can help! Just ask about a specific destination like 'Paris', 'Tokyo', 'Bali', 'London', 'Dubai', 'Bangkok', 'Barcelona', or 'New York'!"

    def get_destination_details(self, destination):
        """Return detailed information about a destination"""
        dest_lower = destination.lower()
        for dest, info in self.destinations.items():
            if dest in dest_lower or dest_lower in dest:
                details = f"\n🌟 {dest.upper()}\n"
                details += f"📍 Country: {info['country']}\n"
                details += f"🗓️ Best Season: {info['season']}\n"
                details += f"🏛️ Top Attractions: {info['attractions']}\n"
                details += f"💰 Cost Level: {info['cost']}\n"
                details += f"⏰ Recommended Duration: {info['duration']}\n"
                return details
        return None

    def get_random_tip(self):
        """Return a random travel tip"""
        import random
        return f"💡 Travel Tip: {random.choice(self.travel_tips)}"

    def get_help(self):
        return """
🌍 TRAVEL ASSISTANT - Commands & Questions:

📍 DESTINATIONS:
   - 'Popular destinations' - See top destinations
   - Name any destination (Paris, Tokyo, Bali, etc.)
   - 'Where should I go?' - Get recommendations

💰 PLANNING:
   - 'How much does it cost?' - Budget information
   - 'Best time to visit' - Seasonal recommendations
   - 'What to pack?' - Packing list
   - 'How do I book?' - Booking assistance

🛫 TRAVEL INFO:
   - 'Travel tips' - Get helpful travel advice
   - 'Visa requirements' - Visa information
   - 'Travel insurance' - Insurance info
   - 'Currency' - Exchange rate info

ℹ️ OTHER:
   - 'Help' - Show this menu
   - 'Bye' - Exit the chat
"""

    def get_response(self, user_input):
        """Generate a response based on user input"""
        user_input_lower = user_input.lower().strip()

        # Check for specific destination
        for dest in self.destinations.keys():
            if dest in user_input_lower:
                dest_details = self.get_destination_details(user_input)
                if dest_details:
                    return dest_details

        # Check for matching patterns
        for pattern, response in self.responses.items():
            if re.search(pattern, user_input_lower):
                return response

        # Default response if no pattern matches
        return "That's an interesting question! I'm here to help with travel planning, destinations, tips, and bookings. Type 'help' to see what I can assist with! ✈️"

    def chat(self):
        """Start an interactive chat session"""
        print(f"\n{'='*60}")
        print(f"  🌍 {self.name.upper()} 🌍")
        print(f"{'='*60}")
        print(f"\n{self.name}: {self.greeting()}\n")
        print("Type 'help' for available commands or 'bye' to exit.\n")

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                response = self.get_response(user_input)
                print(f"\n{self.name}: {response}\n")

                # Exit conditions
                if re.search(r"goodbye|bye|exit|quit", user_input.lower()):
                    break

            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Safe travels! ✈️")
                break
            except Exception as e:
                print(f"{self.name}: An error occurred: {str(e)}\n")


def main():
    """Main entry point"""
    chatbot = TravelAgentChatbot("Travel Assistant")
    chatbot.chat()


if __name__ == "__main__":
    main()
