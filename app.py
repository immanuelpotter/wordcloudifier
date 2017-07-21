import os
import signal
from flask import Flask
from program import wordcloudifier

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_wordcloud():
	page = '<html><body><h1>Welcome to the wordcloud generator!</h1><h2>Enter some text.</h2>'
	page += wordcloudifier
	page += '</body></html>'
	return page

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
