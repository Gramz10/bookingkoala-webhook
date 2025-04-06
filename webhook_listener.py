from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data:
        return "No data", 400

    print("✅ Webhook received")

    # Extract info
    try:
        event = data.get("event")
        res_data = data.get("data", {})
        checkin = res_data.get("checkInDate")
        checkout = res_data.get("checkOutDate")
        address = res_data.get("listing", {}).get("address", {}).get("street")

        print(f"Event: {event}")
        print(f"Check-in: {checkin}")
        print(f"Check-out: {checkout}")
        print(f"Address: {address}")

        # ✅ You’ll pass this to Selenium later

    except Exception as e:
        print(f"❌ Error extracting data: {e}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
