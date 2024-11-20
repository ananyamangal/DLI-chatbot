from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from assistant import handle_whatsapp_message
import logging
from session_utils import reset_session, user_sessions

app = Flask(__name__)

# Configure logging to track the session flow
logging.basicConfig(level=logging.DEBUG)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    user_id = request.values.get("From", "")

    # Initialize session if not already present
    if user_id not in user_sessions:
        reset_session(user_id)

    # Log the incoming message and user session
    logging.debug(f"Received message: '{incoming_msg}' from user {user_id}")
    logging.debug(f"Current session state for user {user_id}: {user_sessions[user_id]}")

    # Process the message with the session state
    session = user_sessions[user_id]
    response_text = handle_whatsapp_message(incoming_msg, session)

    # Update session in memory
    user_sessions[user_id] = session

    # Reset the session if the user entered 'quit'
    if incoming_msg.lower() == "quit":
        reset_session(user_id)

    # Create a Twilio MessagingResponse and send back the response
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
