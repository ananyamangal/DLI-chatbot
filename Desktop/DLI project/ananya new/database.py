import sqlite3
import json

# Function to execute a query in SQLite and return results
def execute_query(query):
    try:
        connection = sqlite3.connect("project_management2.db")
        cursor = connection.cursor()
        print("Debug: Executing query:")
        print(query)  # Print the query being executed
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        # Debug output for query results
        if not results:
            print("Debug: No results found for the query.")
        else:
            print("Debug: Query returned results:", results)
        
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        connection.close()

# Function to draft notification based on query results and customer complaint details
def draft_notification(customer, project, team, complaint_text):
    email_subject = f"Issue Notification: {project['name']} for {customer['name']}"
    email_body = f"""Dear {team['team_name']},

We have received a message from {customer['name']} regarding the project '{project['name']}'.
Here are the details:

Project Description: {project['description']}
Customer Contact: {customer['contact_info']}

Message Details:
{complaint_text}

Please prioritize this issue and respond to the customer at your earliest convenience.

Best regards,
Project Management Assistant
"""

    # Parsing team members
    try:
        team_members = json.loads(team['members'])
        print("Debug: Parsed team members:", team_members)
    except json.JSONDecodeError as e:
        print("Error parsing team members JSON:", e)
        team_members = []

    return {"subject": email_subject, "body": email_body, "recipients": team_members}

# Function to process the complaint and notify the responsible team
def process_complaint(sql_query, complaint_text):
    results = execute_query(sql_query)
    
    if results:
        # Extracting details from results (assuming single result set)
        customer = results[0]
        project = results[0]
        team = results[0]

        # Debug: Output fetched data
        print("Debug: Customer details:", customer)
        print("Debug: Project details:", project)
        print("Debug: Team details:", team)

        # Generate email draft
        email_draft = draft_notification(customer, project, team, complaint_text)
        
        # Check if email draft was successfully created
        if email_draft:
            print("Debug: Successfully created email draft:", email_draft)
        else:
            print("Debug: Email draft was not created.")

        return email_draft
    else:
        print("Debug: No data returned from the query execution.")
        return None
