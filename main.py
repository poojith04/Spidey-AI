from app.core.assistant import Assistant
from app.core.startup import Startup
from app.utils.logger import logger

assistant = Assistant()

Startup.show()

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

    except Exception as e:

        logger.exception(e)

        print(f"\n🕷️ Spidey: {assistant.personality.error_message()}")