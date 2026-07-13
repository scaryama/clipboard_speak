# 🗣️ Clipboard Speak (TTS)

English | [한국어](README_KR.md)

A simple Python tool that instantly reads aloud text from the clipboard or command-line arguments.

## 🚀 Usage

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Execution
*   **Speak from Clipboard:**
    ```bash
    python speak.py
    ```
*   **Speak from CLI:**
    ```bash
    python speak.py "Text to speak"
    ```

## ⚡ Key Features: Fast Response Time
This tool automatically splits long text into sentences for efficient processing.
- **Parallel Processing & Immediate Playback:** It doesn't wait for the entire text to be synthesized. It begins playback as soon as the first sentence's audio is ready.
- **Minimized Latency:** While the first sentence is playing, the subsequent sentences are processed in parallel in the background, providing a seamless and natural listening experience.

---
*MIT License*
