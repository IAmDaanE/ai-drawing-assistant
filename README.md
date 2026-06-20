# 🎨 Gemini Canvas UI

A desktop application built with Python and Pygame that transforms AI responses into dynamic visual shapes. The app utilizes a custom design language to interpret Google Gemini LLM outputs and render them directly onto a digital canvas.

## 🚀 Features

* **Interactive Canvas**: Pygame-driven desktop interface.
* **AI-Generated Graphics**: Translates Gemini LLM responses into shapes.
* **Custom Design Language**: Seamless communication protocol between AI and UI.
* **Lightweight**: Built entirely in Python with minimal dependencies.

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com
   cd gemini-canvas-ui
   ```

2. **Install dependencies**
   ```bash
   pip install pygame google-generativeai
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
4. Replace the existing key string at the top of the file with your personal key.
