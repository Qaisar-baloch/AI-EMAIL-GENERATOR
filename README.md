# AI Email Generator

A Streamlit application that generates a draft email from a small set of user-provided details: recipient, purpose, tone, length and optional additional context. Groq provides the language-model inference.

**Live demo:** https://ai-email-generator-5eg2njicewvgd6eganryk3.streamlit.app/

## Features

- Collect recipient and purpose.
- Select an email tone: Professional, Friendly, Formal, Casual, Polite, Apologetic or Persuasive.
- Select a length: Short, Medium or Detailed.
- Include optional additional details.
- Generate an email subject and body.
- Display the generated draft in the Streamlit interface.

The application asks the model not to invent important facts and uses a fixed output structure with SUBJECT and BODY sections.

## Request flow

~~~text
User inputs
(recipient, purpose, tone, length, details)
        |
        v
Streamlit form
        |
        v
Prompt construction
        |
        v
Groq Chat Completions API
(openai/gpt-oss-20b)
        |
        v
Generated subject + email body
        |
        v
Draft displayed in Streamlit
~~~

## Technology stack

| Component | Technology |
|---|---|
| Language | Python |
| UI | Streamlit |
| LLM inference | Groq API |
| Model ID in current app | openai/gpt-oss-20b |
| Dependency management | requirements.txt |
| Deployment | Streamlit Community Cloud |

## Project structure

~~~text
AI-EMAIL-GENERATOR/
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
~~~

## Run locally

### 1. Clone the repository

~~~bash
git clone https://github.com/Qaisar-baloch/AI-EMAIL-GENERATOR.git
cd AI-EMAIL-GENERATOR
~~~

### 2. Create an environment and install dependencies

~~~bash
python -m venv .venv
~~~

**Windows**

~~~powershell
.venv\Scripts\activate
~~~

**macOS / Linux**

~~~bash
source .venv/bin/activate
~~~

Install requirements:

~~~bash
pip install -r requirements.txt
~~~

### 3. Configure the Groq API key

The application reads GROQ_API_KEY from Streamlit Secrets.

Create .streamlit/secrets.toml locally:

~~~toml
GROQ_API_KEY = "your_groq_api_key"
~~~

For Streamlit Community Cloud, add the same key in the app's Secrets settings. Never commit the real secrets file or API key.

### 4. Run the application

~~~bash
streamlit run app.py
~~~

The app normally opens at http://localhost:8501.

## Usage

1. Enter the recipient.
2. Describe the purpose of the email.
3. Choose a tone and length.
4. Add any context that should be included.
5. Select **Generate Email**.
6. Review and edit the generated draft before sending it.

## Limitations

- Requires a valid Groq API key and access to the configured model.
- The generated email is a draft. Review factual details, names, dates, attachments and commitments before sending.
- The current interface does not persist a generation history or connect to Gmail / Outlook.
- The application does not verify recipient addresses or send emails.

## License

See [LICENSE](LICENSE) for the repository license.

## Author

**Qaisar Khan** · [GitHub profile](https://github.com/Qaisar-baloch)
