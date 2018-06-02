from src.controller import App
import time


if __name__ == "__main__":
    app = App()
    while True:
        app.run()
        time.sleep(3)
