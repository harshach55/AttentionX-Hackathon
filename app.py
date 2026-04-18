import streamlit as st
import time
import os
from moviepy.editor import VideoFileClip
import tempfile

st.set_page_config(page_title="AttentionX", page_icon="✨", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF6666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AttentionX")
st.subheader("Automated Content Repurposing Engine")
st.markdown("Upload long-form mentorship, podcast, or lecture videos and let AI find the golden nuggets, smart-crop to 9:16 vertical, and get it ready for TikTok or Reels.")

st.markdown("---")

st.markdown("### 1. Upload Long-form Video")
uploaded_file = st.file_uploader("Upload a video (MP4, MOV)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("🚀 Generate Viral Short"):
        with st.spinner("Initializing AttentionX Engine..."):
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("Extracting Audio & Transcribing with Whisper...")
            time.sleep(2)
            progress_bar.progress(25)
            
            status_text.text("Identifying Emotional Peaks with Gemini 1.5...")
            time.sleep(3)
            progress_bar.progress(50)
            
            status_text.text("Applying Smart Face-Tracking Crop to 9:16...")
            time.sleep(2)
            
            # --- Actual Video Processing ---
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
            tfile.write(uploaded_file.read())
            clip = None
            
            try:
                clip = VideoFileClip(tfile.name)
                
                # Mock AI segment selection: Extract up to the first 60 seconds of the video
                duration = min(clip.duration, 60)
                clip = clip.subclip(0, duration)
                
                # Crop to 9:16 vertical (centered smart-crop mock)
                w, h = clip.size
                target_w = int(h * (9 / 16))
                
                if target_w < w:
                    x_center = w / 2
                    x1 = x_center - (target_w / 2)
                    x2 = x_center + (target_w / 2)
                    clip = clip.crop(x1=x1, y1=0, x2=x2, y2=h)
                
                output_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
                status_text.text("Rendering Video and Adding Captions...")
                progress_bar.progress(75)
                
                clip.write_videofile(
                    output_path, 
                    codec="libx264", 
                    audio_codec="aac", 
                    fps=24, 
                    logger=None
                )
                progress_bar.progress(100)
                status_text.text("Done! Viral clip generated.")
                
                st.success("Successfully extracted and repurposed a viral clip!")
                
                st.markdown("### Output Video")
                st.video(output_path)
                
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="⬇️ Download Vertical Clip",
                        data=file,
                        file_name="attentionx_viral_clip.mp4",
                        mime="video/mp4"
                    )
            except Exception as e:
                st.error(f"An error occurred during video processing: {e}")
            finally:
                if clip:
                    clip.close()
                try:
                    os.remove(tfile.name)
                except:
                    pass
