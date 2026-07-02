import os
import subprocess


class SystemTools:

    def open_vscode(self):

        # Try using the PATH command first
        try:
            subprocess.Popen(["code"])
            return "VS Code opened successfully."
        except FileNotFoundError:
            pass

        # Fallback to common installation paths
        possible_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
            r"C:\Program Files\Microsoft VS Code\Code.exe",
            r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
        ]

        for path in possible_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return "VS Code opened successfully."

        return "VS Code could not be found."

    def open_downloads(self):

        path = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        os.startfile(path)

        return "Downloads folder opened."

    def open_documents(self):

        path = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        os.startfile(path)

        return "Documents folder opened."