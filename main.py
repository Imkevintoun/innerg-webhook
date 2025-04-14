from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'innerg-secret'

@app.route('/webhook', methods=['GET'])
def webhook():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode == 'subscribe' and token == VERIFY_TOKEN:
        print("✅ WEBHOOK VERIFIED")
        return challenge, 200
    else:
        return "❌ Forbidden", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
