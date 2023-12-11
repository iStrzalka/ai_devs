from flask import Flask, request, jsonify
import sys

sys.path.append('../..')

from common.openai_auth import send_chat_completion

app = Flask(__name__)

hints = []

@app.route('/')
def a():
    hints = []

@app.route('/answer', methods=['POST'])
def index():
    data = request.get_json()
    if '?' not in data['question']:
        hints.append(data['question'])
        return {'reply': 'Ok, I will remember that.'}
    res = send_chat_completion(
        model_version='gpt-4',
        system_content="Using information of: " + "\n".join(hints) + "Answer users question. Be ultra concise, return only the most relevant information.",
        user_content=data['question'],
    )
    return {'reply': res['choices'][0]['message']['content']}

if __name__ == '__main__':
    app.run(debug=True, port=4242)