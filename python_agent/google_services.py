from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



def keyword_in_text(text, keywords):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

def get_classroom_service():
    SCOPES = [ 'https://www.googleapis.com/auth/classroom.announcements.readonly','https://www.googleapis.com/auth/classroom.courses.readonly']
    creds = None

    flow = InstalledAppFlow.from_client_secrets_file(
        'python_agent/Google_Credentials.json', SCOPES 
    )

    creds = flow.run_local_server(port=5000)

    service = build('classroom', 'v1', credentials=creds)

    keywords = ['quiz', 'examination', 'exam']


    courses_result = service.courses().list(pageSize=10).execute()
    courses = courses_result.get('courses', [])

    if not courses:
        return "No courses found."

    class_response = "🤖: \n"
    for course in courses:
        class_response = class_response + f"\n\n 📘 Course: {course['name']}\n"
        course_id = course['id']

        try:
            announcements_result = service.courses().announcements().list(
                courseId=course_id,
                pageSize=5,
                orderBy='updateTime desc'
            ).execute()

            announcements = announcements_result.get('announcements', [])

            found = False
            for ann in announcements:
                text = ann.get('text', '')
                if keyword_in_text(text, keywords):
                    class_response = class_response + f"🗒️ Relevant Announcement: {text}\n"
                    found = True
                    break

            if not found:
                class_response=class_response + "🔍 No relevant announcements mentioning quiz/exam.\n"

        except Exception as e:
            print(f"⚠️ Could not retrieve announcements: {e}")
    return class_response



def get_gmail_service():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    flow = InstalledAppFlow.from_client_secrets_file(
        'python_agent/Google_Credentials.json', SCOPES
    )    
    creds= flow.run_local_server(port=5000)

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])
    gmail_response = "🤖: \n"
    if not messages:
        return "No messages found."
    else:
        gmail_response= gmail_response + "Latest Messages:\n\n"
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['Subject']).execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            gmail_response = gmail_response + f"📧Subject: {subject}\n"

    return gmail_response


