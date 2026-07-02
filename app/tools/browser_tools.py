import webbrowser


class BrowserTools:

    def open_github(self):

        webbrowser.open(
            "https://github.com"
        )

        return "GitHub opened."

    def open_google(self):

        webbrowser.open(
            "https://google.com"
        )

        return "Google opened."

    def open_youtube(self):

        webbrowser.open(
            "https://youtube.com"
        )

        return "YouTube opened."