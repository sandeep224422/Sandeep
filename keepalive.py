import os
import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def ping_self():
    while True:
        try:
            url = os.getenv("RENDER_URL", "https://sandeepmusic-eu7g.onrender.com")
            requests.get(url)
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(600)  # 10 minutes

if __name__ == "__main__":
    threading.Thread(target=ping_self, daemon=True).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port) 