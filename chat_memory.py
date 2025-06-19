import datetime

class SlidingMemory:
    def __init__(self, window_size=5, log_file="chat_log.txt", search_file="search_log.txt"):
        self.window_size = window_size
        self.history = []
        self.log_file = log_file
        self.search_file = search_file

        # Start fresh logs
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write(f"🗂 Chat Log - {timestamp}\n\n")
        with open(self.search_file, "w", encoding="utf-8") as f:
            f.write(f"🔍 Search Log - {timestamp}\n\n")

    def add(self, user_input, bot_response):
        # Add to sliding window memory
        self.history.append(("User", user_input))
        self.history.append(("Bot", bot_response))

        # Keep only last N user+bot pairs (2 * window_size)
        if len(self.history) > self.window_size * 2:
            self.history = self.history[-self.window_size * 2:]

        # Log to chat log
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"User: {user_input}\n")
            f.write(f"Bot: {bot_response}\n\n")

        # Log to search log (only user input)
        with open(self.search_file, "a", encoding="utf-8") as f:
            f.write(f"{user_input}\n")

    def get_prompt(self, current_input, for_text2text=False):
        if for_text2text:
            # Plain context for FLAN-T5, T5, BART
            context = " ".join([text for _, text in self.history])
            return f"{context} {current_input}".strip()
        else:
            # Speaker-tagged context for GPT-style models
            prompt = ""
            for speaker, text in self.history:
                prompt += f"{speaker}: {text}\n"
            prompt += f"User: {current_input}\nBot:"
            return prompt

    def print_memory(self):
        print("\n🧠 Sliding Memory (Last 5 interactions):")
        for speaker, text in self.history:
            print(f"{speaker}: {text}")
        print()
