# AI Chatbot with React and FastAPI test


A modern chatbot application built with React for the frontend and FastAPI for the backend. The application features a beautiful UI, file upload capabilities, and integration with Claude AI models.

## Features

- 🤖 Multiple AI model support (Claude 3 Sonnet, Claude 3 Opus, Claude 2.1, Claude 2)
- 🎨 Customizable themes
- 📎 File upload support
- 💬 Real-time chat interface
- 🔄 Typing indicators
- 📱 Responsive design
- 🔒 User authentication
- ⚙️ Customizable settings

## Tech Stack

- Frontend:
  - React.js
  - CSS3 with modern features
  - SVG animations
  - Responsive design

- Backend:
  - FastAPI
  - Python
  - Claude AI integration
  - File handling

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- Python 3.8 or higher
- npm or yarn
- AWS Bedrock access (for Claude AI)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/reactjsapp.git
cd reactjsapp
```

2. Install frontend dependencies:
```bash
npm install
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
```

### Running the Application

1. Start the backend server:
```bash
uvicorn app:app --reload
```

2. Start the frontend development server:
```bash
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Log in with any username and password (demo mode)
2. Start chatting with the AI
3. Upload files for analysis
4. Customize your experience through the settings panel
5. Choose different AI models and themes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Claude AI by Anthropic
- React.js community
- FastAPI framework 
