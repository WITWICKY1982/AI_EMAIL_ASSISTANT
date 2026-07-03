# AI Email Assistant

## Overview
The **AI Email Assistant** is a lightweight, command-line Python application designed to automatically aggregate, analyze, and synthesize multiple email communications. By feeding text-based email logs to the modern **Google Gemini API** (using the official `google-genai` SDK and the highly-efficient `gemini-2.5-flash` model), the application acts as an intelligent inbox assistant.

It reads all raw email files from a dedicated folder, consolidates them into a single analytical prompt, and generates a structured executive report detailing:
- A concise, one-line summary of each email.
- The sender's core intent.
- Tailored draft reply suggestions.
- Clear, actionable next steps.
- An organized prioritization matrix sorting emails by operational urgency.

---

## Features
- **Local File Processing**: Automatically reads and processes all email files placed in the `emails/` directory.
- **Modern Google Gemini Integration**: Built on the next-generation, official `google-genai` Python library utilizing the powerful `gemini-2.5-flash` model.
- **Semantic Email Summarization**: Distills complex email threads into simple, high-impact, one-line explanations.
- **Intent Detection**: Deciphers what the sender expects or needs (e.g., job interview invitations, billing issues, potential leads, or meeting scheduling).
- **Automated Reply Drafting**: Formulates recommended messaging strategies and draft options for immediate follow-up.
- **Action Item Extraction**: Isolates strict deliverables and deadlines so nothing falls through the cracks.
- **Priority-Driven Organization**: Intelligently ranks and structures the inbox analysis based on business urgency and deadlines.

---

## Technologies Used
- **Python 3.x**
- **Google GenAI SDK** (`google-genai` package)
- **python-dotenv** (for safe environment variable injection)

---

## Project Structure
```text
AI_EMAIL_ASSISTANT/
├── emails/                 # Directory containing raw plain-text emails
│   ├── email1.txt          # Meeting Request (John, AI Automation Proposal)
│   ├── email2.txt          # AI Chatbot Inquiry (Sarah Williams, ShopEase)
│   ├── email3.txt          # Invoice #2045 Overdue Reminder (CloudHost Inc.)
│   └── email4.txt          # Interview Invitation (Priya Sharma, TechNova Solutions)
├── .gitignore              # Files to ignore in Git version control
├── main.py                 # Core application entry point
├── README.md               # Project documentation and guide
└── requirements.txt        # Project dependencies
```

---

## Installation

### Prerequisites
- Python 3.10 or higher.
- A Google Gemini API Key (obtainable via [Google AI Studio](https://aistudio.google.com/)).

### Setup Steps
1. **Clone or download** this project repository to your local system:
   ```bash
   cd AI_EMAIL_ASSISTANT
   ```

2. **Create a virtual environment** to isolate dependencies:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies** manually (due to repository constraints, please run):
   ```bash
   pip install google-genai python-dotenv
   ```

---

## Environment Variables (.env)
The application secures your API credentials using environment files.

Create a file named `.env` in the root directory of the project:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
> **Security Note:** Never commit your `.env` file or expose your API key. The `.gitignore` is pre-configured to ignore `.env` files.

---

## Usage

1. Place plain-text email files (with `.txt` extension) in the `emails/` directory. Example files are already provided (`email1.txt` to `email4.txt`).
2. Execute the main program:
   ```bash
   python main.py
   ```
3. The script will output:
   - The aggregated raw content of all emails found.
   - A highly organized, AI-generated analytical summary report.

---

## Example Output

Below is an illustrative example of the generated report when run with the provided four email files:

```markdown
======================================================================
                  AI EMAIL ASSISTANT EXECUTIVE REPORT
======================================================================

### PRIORITY MATRIX & ANALYSIS

#### 1. PRIORITY: HIGH (URGENT DEADLINE)
*   **Source File**: email4.txt
*   **One-Line Summary**: Invitation to a technical interview scheduled for Tuesday at 11:00 AM IST.
*   **Sender Intent**: Schedule next-stage technical interview and secure confirmation by Sunday evening.
*   **Action Items**: Confirm availability for the Tuesday interview via Google Meet before Sunday evening.
*   **Suggested Reply**: 
    > "Hi Priya, thank you for the invitation! I am pleased to confirm my availability for the technical interview on Tuesday at 11:00 AM IST. I look forward to speaking with the team. Best, Dhruv."

#### 2. PRIORITY: HIGH (FINANCIAL ACTION REQUIRED)
*   **Source File**: email3.txt
*   **One-Line Summary**: Payment reminder for Invoice #2045 ($750) which is 3 days overdue.
*   **Sender Intent**: Prompt settlement of late hosting invoice to avoid potential late fees.
*   **Action Items**: Process the $750 payment to CloudHost Inc. immediately or verify if the transaction was already initiated.
*   **Suggested Reply**: 
    > "Hi Accounts Team, thank you for the reminder. I have processed the payment of $750 for Invoice #2045 today. Please let me know once you receive it. Thank you, Dhruv."

#### 3. PRIORITY: MEDIUM (TIME-SENSITIVE SCHEDULING)
*   **Source File**: email1.txt
*   **One-Line Summary**: Request to schedule a proposal discussion meeting next Monday at 3 PM.
*   **Sender Intent**: Arrange a meeting to discuss the AI Automation proposal.
*   **Action Items**: Check calendar availability for next Monday at 3 PM and respond to John.
*   **Suggested Reply**: 
    > "Hi John, Monday at 3 PM works perfectly for me. I look forward to our meeting to discuss the AI Automation proposal. Regards, Dhruv."

#### 4. PRIORITY: MEDIUM (BUSINESS DEVELOPMENT / NEW LEAD)
*   **Source File**: email2.txt
*   **One-Line Summary**: Sales inquiry from Sarah Williams (ShopEase) seeking a quote and timeline for an AI chatbot.
*   **Sender Intent**: Evaluate capabilities, pricing, and timeline for automating customer queries.
*   **Action Items**: Prepare a high-level proposal (pricing estimate, timeline, portfolio of previous chatbots) and send to Sarah.
*   **Suggested Reply**: 
    > "Hi Sarah, thank you for reaching out! I would love to help you build an AI chatbot for ShopEase to automate those daily customer queries. I'll prepare a structured pricing estimate and project timeline, along with some examples of similar solutions I've built, and send it over by tomorrow morning. Best, Dhruv."
```

---

## Future Improvements
- **Live Email Sync**: Connect directly to SMTP/IMAP servers or APIs (e.g., Gmail, Microsoft Graph) to ingest new messages and draft live responses.
- **Web-Based Inbox UI**: Create a visual dashboard (e.g., using Streamlit, Gradio, or a lightweight React/FastAPI interface) to let users toggle priorities, approve AI-suggested replies, and edit drafts.
- **Custom System Instructions**: Support user-defined personality tuning for custom reply tone configurations (e.g., ultra-formal, casual, customer support mode).
- **Automated Draft Filing**: Save suggested drafts directly to a local `/drafts/` directory or write them directly back into your mail server's draft folder.
- **Multi-Turn Context Tracker**: Enable historical context tracking so the AI understands previous interactions with the same contact.

---

## License
This project is open-source and available under the [MIT License](LICENSE).
