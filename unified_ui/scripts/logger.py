from datetime import datetime
import pyperclip

class Logger:
    def __init__(self):
        self.history: list[dict] = [{"type": "INFO", "log": f"Logger initialized."}]

    def info(self, message: str):
        self.send_log("INFO", message)

    def warn(self, message: str):
        self.send_log("WARNING", message)

    def error(self, message: str):
        self.send_log("ERROR", message)

    def fail(self, message: str):
        self.send_log("FAIL", message)

    def success(self, message: str):
        self.send_log("SUCCESS", message)

    def send_log(self, type, message):
        log = f"[{datetime.now()}] | ({type}): {message}"
        self.history.append({"type": type, "log": log})
        print(log)

    def get(self):
        return self.history

    def clear(self):
        self.history.clear()
        self.history.append("Logger cleared.")

    def copy(self):
        full = ""
        for log in self.history:
            full += log["log"] + "\n"
        pyperclip.copy(full)