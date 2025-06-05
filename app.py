import streamlit as st 
os.system("apt-get update && apt-get install -y ffmpeg")
import os
from main import video_to_summary

def main():
    st.title("Video Summarizer AI")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        st.write("Transcribing and summarizing. This may take a few moments...")

        try:
            summary_result = video_to_summary(
                video_path="uploaded_video.mp4",
                model_size="base",
                summarizer_model_name="facebook/bart-large-cnn",
                use_chunking=True
            )

            st.subheader("Summary")
            st.write(summary_result)

        except Exception as e:
            st.error(f"❌ Error during processing: {e}")

        finally:
            if os.path.exists("uploaded_video.mp4"):
                os.remove("uploaded_video.mp4")

if __name__ == "__main__":
    main()
