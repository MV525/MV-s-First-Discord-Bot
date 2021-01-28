#Flask for server
from flask import Flask
from threading import Thread

app = Flask("")

#Returns "MV's bot is active" upon successful activation
@app.route("/")
def main():
  return "MV's bot is active!"

#Hosting bot on port 8000
def run():
  app.run(host="0.0.0.0", port=8000)

#Keeping bot alive
def keep_alive():
  server = Thread(target=run)
  server.start()
