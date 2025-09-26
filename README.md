# AI News Chatbot ADK

An intelligent AI news assistant built with Google's Agent Development Kit (ADK) that searches the web for the latest AI developments and provides accurate, up-to-date information.

## 🚀 Features

- **Real-time AI News**: Fetches the latest AI news and developments using Google Search
- **ADK Integration**: Fully compatible with Google's Agent Development Kit
- **Web Interface**: Interactive chat interface via ADK Dev UI
- **Smart Responses**: Provides concise, informative answers with sources when appropriate

## 📋 Prerequisites

### All Platforms
- Python 3.10+ (3.12 recommended)
- Google API key from [Google AI Studio](https://ai.google.dev/)
- Git

### Platform-Specific Requirements

#### macOS
- Homebrew (for package management)
- Command Line Tools: `xcode-select --install`

#### Windows
- Python from [python.org](https://www.python.org/) or Microsoft Store
- Git Bash or PowerShell
- Visual Studio Build Tools (for some Python packages)

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd ai_news_chatbot_adk
```

### Step 2: Install ADK (Google Agent Development Kit)

#### macOS/Linux
```bash
pip install --upgrade google-adk
```

#### Windows (PowerShell/Command Prompt)
```cmd
pip install --upgrade google-adk
```

### Step 3: Set Up Virtual Environment

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### Windows (PowerShell)
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Windows (Command Prompt)
```cmd
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat
```

### Step 4: Install Dependencies

```bash
# All platforms (after activating virtual environment)
pip install -r requirements.txt
```

### Step 5: Configure API Key

#### macOS/Linux
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your favorite editor
nano .env  # or vim, code, etc.
```

#### Windows (PowerShell/Command Prompt)
```cmd
# Copy environment template
copy .env.example .env

# Edit .env file with notepad or any text editor
notepad .env
```

Add your Google API key to the `.env` file:
```env
# Replace with your actual Google API key
GOOGLE_API_KEY='your_actual_api_key_here'
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## 🚀 Running the Agent

### Option 1: Using the Provided Scripts

#### macOS/Linux
```bash
# Make script executable (first time only)
chmod +x run.sh

# Run the ADK web interface
./run.sh
```

#### Windows (PowerShell/Command Prompt)
```cmd
# Run the ADK web interface
python -m google.adk.cli web
```

### Option 2: Direct ADK Command

```bash
# All platforms (with virtual environment activated)
adk web
```

### Option 3: Alternative Streamlit Interface

#### macOS/Linux
```bash
# Make script executable (first time only)
chmod +x run_streamlit.sh

# Run Streamlit interface
./run_streamlit.sh
```

#### Windows
```cmd
# Install streamlit if not already installed
pip install streamlit

# Run Streamlit interface
streamlit run app.py
```

## 🌐 Accessing the Agent

Once running, access your AI News Chatbot at:

- **ADK Dev UI**: http://localhost:8000/dev-ui/
- **API Endpoint**: http://localhost:8000/apps/ai_news_chatbot_adk
- **Streamlit UI** (if using): http://localhost:8501

## 💬 Example Queries

Try these prompts to test your agent:

- "What are the latest developments in generative AI?"
- "Tell me about recent breakthroughs in AI research"
- "What's new with OpenAI or Google's AI models?"
- "How is AI being used in healthcare recently?"
- "What are the latest AI ethics concerns?"
- "Give me AI news from the last week"

## 📁 Project Structure

```
ai_news_chatbot_adk/
├── ai_news_chatbot_adk/       # ADK package directory
│   ├── __init__.py            # Package initialization with root_agent
│   └── agent.py               # Main AI News Agent definition
├── agent.py                   # Agent definition (legacy location)
├── app.py                     # Streamlit web interface
├── .env.example               # Environment variables template
├── .env                       # Your API keys (create from .env.example)
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Modern Python package config
├── run.sh                    # macOS/Linux runner script
├── run_streamlit.sh          # Streamlit runner script
├── setup.sh                  # Setup script
└── README.md                 # This file
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Agent Not Discoverable in ADK Web
- Ensure the `ai_news_chatbot_adk` subdirectory exists with proper `__init__.py`
- Check that `root_agent` is properly exported in `__init__.py`
- Restart the ADK server after making changes

#### 2. API Key Issues
- Verify your API key is correctly set in `.env`
- Ensure the `.env` file has proper quotes around the API key
- Check that you're using a valid Google AI Studio API key

#### 3. Windows PowerShell Execution Policy
If you get an error about execution policies:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 4. Port Already in Use
If port 8000 is already in use:
```bash
# Kill the process using port 8000
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

#### 5. Module Import Errors
Ensure your virtual environment is activated:
```bash
# Check if virtual environment is active
which python  # macOS/Linux
where python  # Windows

# Should show path within .venv directory
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## 🔗 Resources

- [Google Agent Development Kit Documentation](https://google.github.io/adk-docs/)
- [Google AI Studio](https://ai.google.dev/)
- [ADK Python SDK](https://pypi.org/project/google-adk/)
- [ADK Samples](https://github.com/google/adk-samples)

## 📞 Support

For issues or questions:
- Check the [Troubleshooting](#-troubleshooting) section
- Review ADK documentation at https://google.github.io/adk-docs/
- Open an issue in the repository

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
