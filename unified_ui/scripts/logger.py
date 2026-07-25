from datetime import datetime

class Logger:
    def __init__(self):
        self.history: list[str] = ["Logger initialized."]

    def info(self, message: str):
        self.send_log("INFO", message)

    def warn(self, message: str):
        self.send_log("WARN", message)

    def error(self, message: str):
        self.send_log("ERROR", message)

    def fail(self, message: str):
        self.send_log("FAIL", message)

    def send_log(self, type, message):
        log = f"[{datetime.now()}] | ({type}): {message}"
        self.history.append(log)
        print(log)

    def get(self):
        return self.history