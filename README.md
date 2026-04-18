# AttentionX: Automated Content Repurposing Engine ✨

AttentionX is a platform that allows users to upload long-form videos (like mentorship sessions, podcasts, and lectures) and automatically uses AI to identify the "golden nuggets" of wisdom. It then smartly crops the video to vertical formats (9:16) while keeping the subject perfectly centered to make high-level education snackable, shareable, and viral on TikTok, Instagram Reels, and YouTube Shorts.

## 🚀 Features
- **Upload any long-form video** via a clean, intuitive Streamlit web interface.
- **Audio Extraction & Whisper Transcription** *(simulated in this lightweight prototype for speed)*.
- **Viral Peak Identification via Gemini** *(simulated)*.
- **Smart Face-Tracking Crop**: Uses `moviepy` to dynamically crop standard horizontal footage (16:9) into engaging vertical shorts (9:16).
- **Instant Render**: Produces a downloadable `.mp4` file ready to be uploaded to social platforms.

---

## 📽️ Demo Video
[Watch the Demo Video on Google Drive](https://drive.google.com/file/d/1K4Jnro-8Bp6Efp30t7JsXU82tw8FkIZa/view?usp=sharing)

---

## 💻 Tech Stack
- **Frontend & App Logic:** [Streamlit](https://streamlit.io/)
- **Video & Audio Processing Engine:** [MoviePy](https://zulko.github.io/moviepy/) 

## 🛠️ How to Run Locally

### 1. Clone the repository (or extract the folder)
Make sure you have python installed.

### 2. Install the necessary packages
Open a terminal in the folder and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit application by running:
```bash
streamlit run app.py
```
A browser window will automatically pop up with the application!

## 💡 About this Submission
This repository contains a functioning, lightweight prototype tailored for the hackathon. To ensure seamless running locally and avoid complex dependency issues (like OpenAI/Google API Keys, or ImageMagick system binaries on Windows), this prototype mocks the API integration phases via progress-bar states but implements actual video rendering and vertical-cropping logic.
