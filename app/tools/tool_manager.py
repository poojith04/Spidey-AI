from app.tools.system_tools import SystemTools
from app.tools.browser_tools import BrowserTools


class ToolManager:

    def __init__(self):

        self.system = SystemTools()

        self.browser = BrowserTools()

    def execute(self, message):

        message = message.lower()

        if ("open vscode" in message
        or "open vs code" in message):
            return self.system.open_vscode()

        if "open downloads" in message:
            return self.system.open_downloads()

        if "open documents" in message:
            return self.system.open_documents()

        if "open github" in message:
            return self.browser.open_github()

        if "open google" in message:
            return self.browser.open_google()

        if "open youtube" in message:
            return self.browser.open_youtube()

        return None
    def is_tool_command(self, message):

        message = message.lower()

        commands = [
            "open",
            "create",
            "delete",
            "launch",
            "close",    
            "shutdown",
            "restart"
        ]

        return any(message.startswith(cmd) for cmd in commands)