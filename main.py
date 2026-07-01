from app.assistant import Assistant

assistant = Assistant()

print("=" * 50)
print("🕷️ Spidey AI Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("\nSpidey: Goodbye!")
        break

    try:
        response = assistant.chat(user)
        print(f"\n🕷️ Spidey: {response}")

    except Exception as e:
        print(f"\nError: {e}")