import sqlite3
import json
import logging
from session_utils import reset_session

logging.basicConfig(level=logging.DEBUG)
def handle_whatsapp_message(incoming_msg, session):
    greetings = ["hi", "hello", "hey", "start"]

    if incoming_msg.strip().lower() == "quit":
        reset_session(session["user_id"])  # session["user_id"] now exists after the fix in reset_session
        return "👋 Thank you for using DLI Project Assistant! Goodbye! 🌟 If you need assistance in the future, just reach out!"
    
    if not session.get("welcomed") or incoming_msg.lower() in greetings:
        session["welcomed"] = True
        return (
            "👋 Hi there! Welcome to DLI Project Assistant 🤖! I’m here to assist you every step of the way. "
            "Let’s get started! 🚀\n\nCould you please provide the customer name?"
        )

    if session.get("customer_name") is None:
        session["customer_name"] = incoming_msg
        return "👍 Perfect! Now, could you please provide the project name?"

    if session.get("project_name") is None:
        session["project_name"] = incoming_msg
        return "Great! 📂 Lastly, could you give me a detailed description of the work? 🖊️"

    if session.get("work_description") is None:
        session["work_description"] = incoming_msg

        customer_name = session["customer_name"]
        project_name = session["project_name"]
        work_description = session["work_description"]

        email_draft = (
            "✅ The request has been successfully processed! "
            "An email has been sent to the responsible team. 📧 "
            "If there’s anything else I can help you with, feel free to ask! 😊\n\n"
            "Type 'quit' to end the conversation.\n\n"
            "🔔 *Attention Required: New Issue Notification* 🔔\n\n"
            f"Subject: Issue Notification: {customer_name} for {project_name}\n\n"
            f"Dear Development Team,\n\n"
            f"We have received a message from {customer_name} regarding the project '{project_name}'. "
            f"Here are the details:\n\n"
            f"📋 *Project Description*: {work_description}\n\n"
            "🚨 *Please prioritize this issue* and respond to the customer at your earliest convenience.\n\n"
            "Best regards,\nDLI Project Assistant 🤖"
        )

        # Reset session after completing the process
        reset_session(session["user_id"])

        return email_draft + "\n\n✅ If you need more help, type 'start' to begin again. 😊"

    return "⚠️ Oops! Something went wrong. Please try again. 🛠️"
