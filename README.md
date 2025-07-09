🤖 Whatsapp-Personal-Chatbot
An AI-powered WhatsApp bot that lives inside your personal "Message Yourself" chat.

It can:

    🧠 Respond intelligently to your messages using OpenRouter or Groq LLMs.

    📧 Fetch your 10 latest Gmail emails using the Gmail API.

    🏫 Fetch important announcements (related to exams/quizzes) from your 10 latest Google Classroom courses.

    All messages are saved to a chat_history.json file for context and memory.


📌 Features
    ✅ Private AI Assistant in WhatsApp — only replies to your own messages in your personal chat.

    ✅ Natural conversation via OpenRouter/Groq models.

    ✅ Google Classroom Integration: Detects exam/quiz-related announcements.

    ✅ Gmail Integration: Retrieves the 10 most recent emails (read or unread).

    ✅ Supports /exit to shut down the Node.js WhatsApp bot.

🗂️ Project Structure

    Whatsapp-Personal-Chatbot/
    │
    ├── node_bot/                          # WhatsApp automation (Node.js)
    │   ├── index.js                       # Main WhatsApp bot file
    │   └── package.json                   # npm project file
    │
    ├── python_agent/                      # Flask + AI + Google APIs (Python)
    │   ├── app.py                         # Flask app handling message requests
    │   ├── Google_Credentials.json        # Your Google OAuth credentials
    │   ├── google_services.py             # Gmail and Classroom API logic
    │   ├── groq_responder.py              # Handles AI replies + routing (Through Groq)
    │   ├── openrouter_responder.py        # Handles AI replies + routing (Through OpenRouter)
    |
    ├── .env                               # Your OpenRouter & Groq API keys
    ├── .gitignore                         # Ignoring venv, node_modules, .env, etc.
    ├── chat_history.json                  # Stores all messages exchanged
    ├── README.md                          # Project documentation
    ├── requirements.txt               # Python dependencies

⚙️ Setup Instructions
    1. Clone the Repository:-
        git clone https://github.com/yourusername/Whatsapp-Personal-Chatbot.git
        cd Whatsapp-Personal-Chatbot

    2. Set Up the Python Backend
        cd python_agent
        python -m venv venv

        venv\Scripts\activate        # Windows
        # or
        source venv/bin/activate     # Mac/Linux

        pip install -r requirements.txt
        
    3. Set Up the Node.js WhatsApp Bot
        cd ../node_bot
        npm install whatsapp-web.js qrcode-terminal puppeteer

    4. Google API Configuration
        Enable Gmail API and Google Classroom API from Google Cloud Console.

        Download the OAuth JSON file.

        Rename it to Google_Credentials.json and place it in the python_agent/ folder.

    5. Create .env File in Whatsapp-Personal-Chatbot/
        Inside the Whatsapp-Personal-Chatbot/, create a .env file:
            OPENROUTER_API_KEY=your_openrouter_api_key
            GROQ_API_KEY=your_groq_api_key

    6. Start the Flask Backend
        cd python_agent
        python app.py
        Flask will run on http://localhost:8000.

    7. Start the WhatsApp Bot
        cd ../node_bot
        node index.js
        A QR code will be shown. Scan it using your WhatsApp (mobile app).

The bot will only reply to your personal “Message Yourself” chat.

📌 Example Commands

Message Sent                                    |   	Response Behavior                                       |
_________________________________________________________________________________________________________________
gmail	                                        |   Replies with your 10 most recent emails                     |
classroom                                       |   Replies with important class announcements (exams/quizzes)  |
hello, how are you?(or any other message)       |	AI-powered response via LLM (Groq/OpenRouter)               |
exit                                            |	Shuts down the Node.js bot (not Flask)                      |
_________________________________________________________________________________________________________________

📚 Technologies Used

    Python + Flask (backend server)

    Node.js + WhatsApp-Web.js (chat interface)

    OpenRouter / Groq (AI replies)

    Google APIs (Gmail + Classroom)

📄 License
    MIT License.
    © 2025 [Aniket Pratap Singh]