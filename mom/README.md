# MoM Maker — LangGraph + Whisper API + FFmpeg

### 🎯 Goal
Automate creation of Minutes of Meeting (MoM) from any recorded meeting video.

**Pipeline:**
Video (.mp4) → Extract Audio (FFmpeg) → Transcribe (Whisper API) → Summarize (LLM) → Categorize into MoM (LangGraph nodes)

---

### 🧰 Setup

#### 1. Install FFmpeg
macOS:
  brew install ffmpeg

Ubuntu:
  sudo apt install -y ffmpeg

#### 2. Setup environment
```bash
uv venv
chmod +x .venv/bin/activate
source .venv/bin/activate
uv pip install -r requirements.txt
