from flask import Flask, request, make_response

app = Flask(__name__)

VERIFY_TOKEN = "innerg-secret"

@app.route('/webhook', methods=['GET'])
def webhook_verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token and mode == "subscribe" and token == VERIFY_TOKEN:
        response = make_response(str(challenge), 200)
        response.mimetype = "text/plain"
        return response
    return "Forbidden", 403
