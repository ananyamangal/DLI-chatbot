import logging

# Dictionary to hold session data for each user
user_sessions = {}

def reset_session(user_id):
    user_sessions[user_id] = {
        "user_id": user_id,  # Add user_id to the session state
        "customer_name": None,
        "project_name": None,
        "work_description": None,
        "welcomed": False  # Track whether the user received a welcome message
    }
    logging.debug(f"Session reset for user {user_id}")
    return user_sessions[user_id]
