import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("ERROR: API KEY NOT FOUND. Check your .env file.")
        st.stop()
    return genai.Client(api_key=api_key)


def read_emails(uploaded_files):
    all_email = ""
    for file in uploaded_files:
        try:
            email_text = file.read().decode("utf-8")
        except Exception as e:
            st.error(f"ERROR: Could not read {file.name}. Details: {e}")
            st.stop()

        all_email += f"""
        ====================
        File: {file.name}
        ====================

        {email_text}
        """

    if not all_email.strip():
        st.error("No readable email content found in the uploaded files.")
        st.stop()

    return all_email


def build_prompt(all_email):
    prompt = f"""
    YOU ARE AN AI EMAIL SUMMARIZER
    ANALYZE THE EMAILS BELOW
    1. GIVE ONE LINE SUMMARY
    2. SENDER INTENT
    3. SUGGEST REPLY
    4. ACTION ITEMS - WHAT HAS TO BE DONE
    ORGANIZE THE EMAILS BASED ON THEIR PRIORITY
    MAKE THE REPORT BRIEF AND CONCISE

    EMAILS:
    {all_email}
    """
    return prompt


def get_summary(prompt, client):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    except Exception as e:
        st.error(f"ERROR: Gemini API request failed. Details: {e}")
        st.stop()

    if not response.text:
        st.error("ERROR: Gemini returned an empty response.")
        st.stop()

    return response.text


# ---------- Page ----------

st.set_page_config(page_title="AI Email Assistant", page_icon="📧")
st.title("📧 AI Email Assistant")
st.write("Upload one or more email text files to get an AI-generated summary, priority order, and suggested replies.")

uploaded_files = st.file_uploader(
    "Upload email files (.txt)",
    type=["txt"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("Summarize Emails"):
        with st.spinner("Reading and analyzing emails..."):
            client = get_client()
            all_email = read_emails(uploaded_files)
            prompt = build_prompt(all_email)
            result = get_summary(prompt, client)

        st.success("Done!")
        st.markdown(result)

        st.download_button(
            label="Download Summary as TXT",
            data=result,
            file_name="email_summary.txt",
            mime="text/plain"
        )