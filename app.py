import streamlit as st
from groq import Groq


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="centered"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("✉️ AI Email Generator")
st.write(
    "Generate professional emails quickly using AI powered by Groq."
)


# --------------------------------------------------
# GET GROQ API KEY FROM STREAMLIT SECRETS
# --------------------------------------------------

try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error(
        "GROQ_API_KEY is not configured. "
        "Please add it to Streamlit Secrets."
    )
    st.stop()


# --------------------------------------------------
# INITIALIZE GROQ CLIENT
# --------------------------------------------------

client = Groq(api_key=groq_api_key)


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

st.subheader("Create your email")

recipient = st.text_input(
    "Recipient",
    placeholder="e.g. Professor, Manager, Client"
)

purpose = st.text_area(
    "What is the purpose of the email?",
    placeholder=(
        "Example: I want to request a meeting with my professor "
        "to discuss my research project."
    ),
    height=120
)

tone = st.selectbox(
    "Email tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Casual",
        "Polite",
        "Apologetic",
        "Persuasive"
    ]
)

length = st.selectbox(
    "Email length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)

additional_details = st.text_area(
    "Additional details (optional)",
    placeholder=(
        "Add any important information that should be included "
        "in the email."
    ),
    height=100
)


# --------------------------------------------------
# GENERATE EMAIL
# --------------------------------------------------

if st.button("✨ Generate Email", use_container_width=True):

    if not recipient:
        st.warning("Please enter the recipient.")

    elif not purpose:
        st.warning("Please describe the purpose of the email.")

    else:

        system_prompt = """
You are a professional email writing assistant.

Your task is to write clear, natural, professional emails.

Follow these rules:

1. Create an appropriate email subject.
2. Write a complete email body.
3. Match the requested tone.
4. Do not invent important facts.
5. Keep the language natural and easy to understand.
6. Avoid unnecessary words.
7. Do not use placeholders unless absolutely necessary.
8. Return the result in exactly this format:

SUBJECT:
<email subject>

BODY:
<email body>
"""

        user_prompt = f"""
Write an email using the following information:

Recipient:
{recipient}

Purpose:
{purpose}

Tone:
{tone}

Length:
{length}

Additional details:
{additional_details}
"""

        try:

            with st.spinner("Generating your email..."):

                response = client.chat.completions.create(
                    model="streamlit>=1.40.0groq>=0.11.0",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )

            generated_email = response.choices[0].message.content

            st.success("Email generated successfully!")

            st.subheader("Generated Email")

            st.text_area(
                "Your AI-generated email",
                value=generated_email,
                height=400
            )

        except Exception as e:

            st.error(
                "Something went wrong while generating the email."
            )

            st.exception(e)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AI Email Generator • Built with Streamlit and Groq"
)
