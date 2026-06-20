# 🎨 Gemini Canvas UI

A desktop application in which you can draw like a regular image editor but also includes a prompt section where you ask an ai assistant to draw something for you. Built with Python and Pygame that transforms AI responses into dynamic visual shapes. The app utilizes a custom design language to interpret Google Gemini LLM outputs and render them directly onto a digital canvas.

## 🚀 Features

* **Regular Interactive Drawing Canvas**: Pygame-driven desktop interface with tools like a paint brush, circle, rectangle, straight line...
* **AI-Generated Graphics**: Translates Gemini LLM responses into shapes.
* **Custom Design Language**: Seamless communication protocol between AI and UI.
* **Lightweight**: Built entirely in Python with minimal dependencies.

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com
   cd ai-drawing-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install pygame requests
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🔑 API Key Configuration

The source code includes a hardcoded API key intended **only for quick initial testing**. Do not use this key for production or heavy testing.

To set up your own free tier key:
1. Visit [Google AI Studio](https://google.com).
2. Generate a free API key.
3. Open the main Python file.
4. Replace the API_KEY string at the top of the file with your personal key.
