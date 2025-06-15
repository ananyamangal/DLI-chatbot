### 📦 DLI Project Assistant
A WhatsApp-integrated assistant built with Flask, Twilio, and SQLite, designed to streamline the process of logging customer issues, collecting project-related details, and notifying relevant development teams automatically via structured email drafts.
## 🚀 Features

-  Interactive WhatsApp chat flow
-  Tracks customer name, project name, and work description
-  Auto-generates email-style messages based on conversation
-  Uses SQLite to map customer/project/team data
-  Supports session reset (`quit` command)
-  Modular code for assistant logic, database handling, and session management

### 📸 Screenshots
<img width="200" alt="Screenshot 2025-06-15 at 1 51 03 PM" src="https://github.com/user-attachments/assets/910133df-737b-497d-8a6b-73a10ca38891" />
<img width="200" alt="Screenshot 2025-06-15 at 1 57 37 PM" src="https://github.com/user-attachments/assets/21f65106-8846-4b05-99cf-d516e4039292" />

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| Python     | Main programming language |
| Flask      | Web framework for handling Twilio webhook |
| Twilio     | WhatsApp messaging API |
| SQLite     | Lightweight database to store metadata |
| Ngrok (optional) | Tunneling for local webhook testing |
| JSON       | Used for storing team members in DB |

## 📁 Project Structure
app.py # Flask server and webhook handler
├── assistant.py # Core logic for WhatsApp message processing
├── db_utils.py # Query execution and email generation
├── session_utils.py # Manages session states per user
├── project_management2.db # SQLite database with customer/project/team tables
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/ananyamangal/MediNEXUS-qr_blockchain_order_tracking.git
cd MediNEXUS-qr_blockchain_order_tracking
```

### 2. Clone the Repository
```bash
pip install -r requirements.txt
```

### 3. Start the Flask Server
```bash
python app.py
```
### 4.(Optional) Expose the Server Using Ngrok
```bash
ngrok http 5002
```
Copy the https://... URL from ngrok and paste it into your Twilio WhatsApp sandbox configuration under the Webhook URL field.
