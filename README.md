# ✉️ AI Email Generator

An AI-powered email generator built with **Python, Streamlit, and Groq API**.

The application allows users to generate professional and personalized emails by providing the recipient, purpose, tone, length, and additional details.

The project is designed to be deployed directly from **GitHub to Streamlit Community Cloud**, with the Groq API key securely stored using **Streamlit Secrets**.

---

## 🚀 Live Application

Once your application is deployed, add your Streamlit URL here:
<img width="596" height="568" alt="image" src="https://github.com/user-attachments/assets/9c4078d8-a161-4b9e-910a-1fb926bdb91f" />

```text
https://ai-email-generator-5eg2njicewvgd6eganryk3.streamlit.app/
```

---

## ✨ Features

- 🤖 AI-powered email generation
- ✉️ Generate email subject and body
- 🎯 Specify the email recipient
- 📝 Describe the purpose of the email
- 🎨 Select different email tones
- 📏 Choose email length
- ➕ Add additional information
- 🔐 Secure Groq API key using Streamlit Secrets
- ☁️ Deploy directly from GitHub
- 🖥️ Simple and beginner-friendly interface

### Available Email Tones

- Professional
- Friendly
- Formal
- Casual
- Polite
- Apologetic
- Persuasive

### Available Email Lengths

- Short
- Medium
- Detailed

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Streamlit | Web application and user interface |
| Groq API | AI-powered email generation |
| GitHub | Source code management |
| Streamlit Community Cloud | Application deployment |

---

# 📁 Project Structure

```text
ai-email-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

#### `app.py`

Contains the main Streamlit application, user interface, prompts, and Groq API integration.

#### `requirements.txt`

Contains the Python packages required by the application.

#### `README.md`

Contains project documentation, setup instructions, and deployment instructions.

#### `.gitignore`

Prevents sensitive and unnecessary files from being uploaded to GitHub.

---

# 🔑 Groq API Configuration

This application uses the **Groq API** to generate AI-powered emails.

The Groq API key should **never be placed directly inside `app.py` or uploaded to GitHub**.

The application accesses the API key using Streamlit Secrets:

```python
st.secrets["GROQ_API_KEY"]
```

---

# 🔐 Streamlit Secrets

The Groq API key is stored securely using **Streamlit Secrets**.

## Configure Secrets on Streamlit Cloud

When deploying the application:

1. Open your Streamlit application.
2. Go to **Manage app**.
3. Open the application settings.
4. Find the **Secrets** section.
5. Add the following:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

Replace `your-groq-api-key` with your actual Groq API key.

### ⚠️ Important Security Rule

Never publish your actual API key in:

- GitHub
- `app.py`
- `README.md`
- Screenshots
- Public documentation
- Social media
- Any public repository

Your API key should only be stored in Streamlit Secrets.

---

# 📦 Requirements

The project requires the following Python packages:

```text
streamlit
groq
```

These dependencies are stored in:

```text
requirements.txt
```

Streamlit Community Cloud automatically installs the packages listed in `requirements.txt` during deployment.

---

# ☁️ Deployment on Streamlit Community Cloud

This application is designed for direct deployment from GitHub.

## Step 1 — Create a GitHub Repository

Create a GitHub repository with a name such as:

```text
ai-email-generator
```

Upload the following files:

```text
app.py
requirements.txt
README.md
.gitignore
```

---

## Step 2 — Check `requirements.txt`

Make sure the file contains:

```text
streamlit
groq
```

The file must be named exactly:

```text
requirements.txt
```

and should be located in the root directory of the repository.

Your repository should look like:

```text
ai-email-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Step 3 — Open Streamlit Community Cloud

Go to:

https://share.streamlit.io/

Sign in using your GitHub account.

---

## Step 4 — Create the Application

Select:

```text
Create app
```

Select your GitHub repository.

Use the following configuration:

```text
Repository:
YOUR_USERNAME/ai-email-generator

Branch:
main

Main file path:
app.py
```

---

## Step 5 — Configure Streamlit Secrets

Open the **Advanced Settings / Secrets** section.

Add:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

Do not add the API key to your GitHub repository.

---

## Step 6 — Deploy

Click:

```text
Deploy
```

Streamlit will automatically:

```text
GitHub Repository
        ↓
Read app.py
        ↓
Read requirements.txt
        ↓
Install dependencies
        ↓
Read Streamlit Secrets
        ↓
Connect to Groq API
        ↓
Launch Application
```

After successful deployment, Streamlit will provide a public application URL.

Example:

```text
https://ai-email-generator.streamlit.app
```

---

# 🖥️ How the Application Works

The application follows this process:

```text
                  USER
                    │
                    ▼
          ┌─────────────────┐
          │  Enter Details  │
          │                 │
          │  Recipient      │
          │  Purpose        │
          │  Tone           │
          │  Length         │
          │  Extra Details  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │    Streamlit    │
          │   Application   │
          └────────┬────────┘
                   │
                   ▼
             ┌───────────┐
             │  Groq API │
             │  AI Model │
             └─────┬─────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Generated Email │
          │                 │
          │ Subject         │
          │ Email Body      │
          └─────────────────┘
```

---

# 🧠 AI Generation Process

The application sends the user's requirements to the Groq AI model.

For example:

```text
Recipient:
University Professor

Purpose:
Request a meeting to discuss my final year project.

Tone:
Professional

Length:
Medium
```

The AI generates a complete email such as:

```text
SUBJECT:
Request for Meeting Regarding Final Year Project

BODY:

Dear Professor,

I hope you are doing well.

I am writing to request a meeting with you to discuss
my final year project. I would appreciate the opportunity
to discuss my ideas and receive your guidance.

Please let me know a convenient time for you.

Thank you for your time and consideration.

Best regards,
[Your Name]
```

---

# 🔒 Security

The Groq API key is accessed using:

```python
st.secrets["GROQ_API_KEY"]
```

instead of hardcoding the key inside the Python source code.

Do not commit API keys or other sensitive credentials to GitHub.

If using a local Streamlit secrets file during development, it should be excluded from GitHub.

Example:

```text
.streamlit/secrets.toml
```

should not be committed to the repository.

---

# 🧪 Testing the Application

After deployment, you can test the application using the following example.

### Recipient

```text
University Professor
```

### Email Purpose

```text
Request a meeting to discuss my final year project.
```

### Tone

```text
Professional
```

### Length

```text
Medium
```

Then click:

```text
Generate Email
```

The application should generate an email subject and body.

---

# 🐛 Troubleshooting

## Error: `ModuleNotFoundError: No module named 'groq'`

If Streamlit displays:

```text
ModuleNotFoundError: No module named 'groq'
```

check that `requirements.txt` contains:

```text
streamlit
groq
```

Also make sure `requirements.txt` is located in the root of the GitHub repository:

```text
ai-email-generator/
│
├── app.py
├── requirements.txt
└── README.md
```

After updating `requirements.txt`:

1. Commit the changes to GitHub.
2. Wait for Streamlit to rebuild the application.
3. If necessary, go to **Manage app** and reboot the application.

---

## Error: `GROQ_API_KEY`

If you receive an error related to:

```text
GROQ_API_KEY
```

check your Streamlit Secrets configuration.

The secret should be:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

The name must exactly match:

```text
GROQ_API_KEY
```

---

## Application Does Not Update

When you make changes to your GitHub repository:

```text
Edit Code
    ↓
Commit Changes
    ↓
GitHub
    ↓
Streamlit detects changes
    ↓
Application rebuilds
```

If necessary, use:

```text
Manage app → Reboot app
```

---

# 🔮 Future Improvements

This project can be expanded into a complete AI Email Assistant.

Possible future features include:

- 📋 Copy email to clipboard
- 🔄 Regenerate email
- ✏️ Rewrite existing emails
- 📧 Generate email replies
- 📝 Grammar correction
- 🎯 Improve email professionalism
- 📉 Shorten emails
- 📈 Expand emails
- 🌐 Multilingual email generation
- 📚 Email templates
- 💾 Email history
- 📄 Export emails
- 📥 Download emails
- 🔗 Gmail integration
- 🔗 Outlook integration
- 👤 User authentication
- 🎨 Improved UI/UX
- 🧠 Multiple AI models

---

# 🗺️ Future Project Architecture

The project can eventually evolve into:

```text
                  AI EMAIL ASSISTANT
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
      Generate         Rewrite          Reply
       Email            Email           Email
          │               │               │
          └───────────────┼───────────────┘
                          │
                          ▼
                      GROQ API
                          │
                          ▼
                       AI MODEL
                          │
                          ▼
                     STREAMLIT
                          │
                          ▼
                      GITHUB
                          │
                          ▼
               STREAMLIT COMMUNITY CLOUD
```

---

# 🎯 Project Goal

The goal of this project is to demonstrate how to build and deploy a practical AI application using:

```text
Python
   +
Groq API
   +
Streamlit
   +
GitHub
   +
Streamlit Community Cloud
```

The project also demonstrates secure API key management using Streamlit Secrets.

---

# 👨‍💻 Author

Developed as an AI application project using:

- Python
- Groq API
- Streamlit
- GitHub
- Streamlit Community Cloud

---

## ⭐ Support

If you find this project useful, consider giving the GitHub repository a ⭐.

```text
Built with Python + Streamlit + Groq 🤖✉️
```
