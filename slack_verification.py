from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/slack/webhook", methods=["GET", "POST"])
def slack_events():
    if request.method == "POST":
        data = request.get_json()
        # Check if Slack sent a challenge for verification
        if "challenge" in data:
            return jsonify({"challenge": data.get("challenge")})
    return "OK"

if __name__ == "__main__":
    app.run(port=5005)
