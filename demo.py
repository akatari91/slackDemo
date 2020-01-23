from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def basic():
    return 'hello user'

@app.route('/slack')

def demo():

    url = "https://hooks.slack.com/services/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"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer xoxp-914096078352-914107048869-913646100468-aa55c215904c0a840d40a60a01a68cb3"
        }
    data = {
        "text": "Hello, world"
        }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    print("success")
    return response.raw.read()

if __name__ == '__main__':
    app.run()