# 🤖 Groq Streamlit Chatbot

A simple AI chatbot built with **Python, Streamlit, and the Groq API**. The project demonstrates how to connect a Streamlit interface to a large language model using the official Groq Python client.

The application accepts a user's question through a web interface and generates an AI response using the **Llama 3.1 8B Instant** model.

## ✨ Features

- 💬 Simple Streamlit chatbot interface
- ⚡ Fast responses using the Groq API
- 🧠 Powered by `llama-3.1-8b-instant`
- 🔐 API key loaded through environment variables
- 🌱 Uses `python-dotenv` for `.env` configuration
- 🐍 Simple Python implementation suitable for learning and experimentation

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Application language |
| 🎈 Streamlit | Web interface |
| ⚡ Groq | LLM inference API |
| 🧠 Llama 3.1 8B Instant | Language model |
| 🔑 python-dotenv | Environment variable management |

## 📁 Project Structure

```text
trygroq/
├── chatbot.py
├── requirements.txt
└── README.md
```

## 🔄 How It Works

```text
User
  │
  ▼
Streamlit Text Input
  │
  ▼
Groq Python Client
  │
  ▼
Llama 3.1 8B Instant
  │
  ▼
Generated Response
  │
  ▼
Streamlit UI
```

The application creates a Groq chat completion with a system instruction and the user's question, then displays the returned response in Streamlit.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SreejoySarkar/trygroq.git
cd trygroq
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The project uses:

```text
streamlit
python-dotenv
groq
```

## 🔑 Configure the Groq API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The application uses `python-dotenv` to load the environment configuration and the Groq client reads the API key from the environment.

> ⚠️ **Never commit your real API key to GitHub.** Keep `.env` out of version control.

## ▶️ Run the Application

Start Streamlit with:

```bash
streamlit run chatbot.py
```

Streamlit will provide a local URL, normally:

```text
http://localhost:8501
```

Open the URL in your browser and enter a question.

## 🧠 Model

The current implementation uses:

```text
llama-3.1-8b-instant
```

The model is requested through Groq's chat completion API.

## 💡 Example

Enter a question such as:

```text
Explain object-oriented programming in simple words.
```

The application sends the question to the model and displays the generated answer in the Streamlit interface.

## 📌 Main Code Flow

The application:

1. Loads environment variables using `python-dotenv`.
2. Imports the Groq client.
3. Creates a Streamlit interface.
4. Accepts a question from the user.
5. Sends the question to the Groq chat completion API.
6. Extracts the generated response.
7. Displays the response when the button is clicked.

## 🔮 Future Improvements

Possible enhancements include:

- 💬 Persistent chat history
- 🧠 Multi-turn conversations
- 🎨 Improved Streamlit UI
- 🔄 Streaming responses
- ⚙️ Model selection from the UI
- 📝 Conversation export
- 🛡️ Better error handling
- 🔐 Improved secrets management
- 📊 Token and response-time tracking

## 👨‍💻 Author

**Sreejoy Sarkar**

B.Tech Computer Science & Engineering

GitHub: [@SreejoySarkar](https://github.com/SreejoySarkar)

## ⭐ Support

If you found this project useful for learning or experimentation, consider giving the repository a ⭐ on GitHub.

---

Built with **Python + Streamlit + Groq** 🚀
