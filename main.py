from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
        
client = genai.Client(
 api_key = os.getenv("GEMINI_API_KEY")
)
#content =input("ENTER WHAT U WANT TO ASK")
all_email = ""
for file in os.listdir("emails"):

    with open(f"emails/{file}", "r") as f:
        email = f.read()
        all_email += f"""
        ====================
        File: {file}
        ====================

        {email}
        """
print(all_email)
prompt = f"""
YOU ARE AN AI EMAIL SUMMARIZER
ANLYZE THE EMAILS BELOW 
1.GIVE ONE LINE SUMMARY
2.SENDER INTENT
3.SUGGEST REPLY
4.ACTION ITEMS WHAT HAS TO DONE
ORGANIZE THE EMAIL ON BASICS OF THEIR PRIORITY
MAKE REPORT BRIEF AND CONCISE
EMAIL:
{all_email}
"""

response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
print(response.text)
   


