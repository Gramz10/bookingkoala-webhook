from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check route
@app.route('/', methods=['GET'])
def home():
    return '✅ Webhook is running', 200

# Webhook listener
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print("📬 Received Webhook Data:", data)

        # Optional: Extract important fields
        event_type = data.get("eventType")
        reservation = data.get("payload", {})
        guest_name = reservation.get("guest", {}).get("fullName")
        check_in = reservation.get("checkInDate")
        check_out = reservation.get("checkOutDate")

        print(f"Event: {event_type}, Guest: {guest_name}, Check-in: {check_in}, Check-out: {check_out}")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("❌ Error handling webhook:", str(e))
        return jsonify({"error": "internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
