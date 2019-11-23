from bs4 import BeautifulSoup
import time	
import os
import webbrowser
from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return send_from_directory('./', 'index.html')

@app.route("/fetch", methods=['GET'])
def fetch_article():
    print('The request has been recieved, the timer is starting at: ')
    t0 = time.time()
    print('The request has been recieved, the timer is starting at: ')
    url = request.args['url']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    html = str(soup)
    return html
    
if __name__ == "__main__":
    app.run(debug=True)



