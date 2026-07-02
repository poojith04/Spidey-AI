from app.assistant import Assistant

assistant = Assistant()

print("=" * 50)
print("🕷️ Spidey AI Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

# Random startup greeting
print(f"\n🕷️ Spidey: {assistant.personality.greeting()}")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        print(
            f"\n🕷️ Spidey: {assistant.personality.success_message()} See you later, boss! 👋"
        )
        break

    try:

        response = assistant.chat(user)

        print(f"\n🕷️ Spidey: {response}")

    except Exception:

        print(f"\n🕷️ Spidey: {assistant.personality.error_message()}")