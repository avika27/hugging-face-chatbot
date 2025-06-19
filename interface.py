from model_loader import rf  # your model wrapped in SimpleWrapper
from chat_memory import SlidingMemory

# Set to True if using FLAN-T5, BART, etc.
USE_TEXT2TEXT_MODEL = True  # change to False if you're using text-generation models like GPT-2, Falcon, etc.

def main():
    memory = SlidingMemory(window_size=5)
    print("\n🤖 Chatbot is ready! Type your message (type 'exit' to quit):\n")

    while True:
        try:
            # Take user input
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("🤖 Chatbot: Goodbye! 👋")
                break

            # Build prompt with memory
            prompt = memory.get_prompt(user_input, for_text2text=USE_TEXT2TEXT_MODEL)

            # Show thinking message
            print("\n🤖 Chatbot (thinking...)\n")

            # Generate response
            response = rf.invoke(prompt)

            # Print chatbot reply
            print(f"🤖 Chatbot: {response}\n")

            # Store in memory and logs
            memory.add(user_input, response)

            # Optional: Show sliding memory in terminal
            memory.print_memory()

        except KeyboardInterrupt:
            print("\n🤖 Chatbot: Session ended manually. 👋")
            break
        except Exception as e:
            import traceback
            print("⚠️ Error:", str(e))
            traceback.print_exc()

if __name__ == "__main__":
    main()
