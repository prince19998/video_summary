import os
import subprocess
import whisper

def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    audio_path = os.path.abspath(audio_path)
    video_path = os.path.abspath(video_path)

    if os.path.exists(audio_path):
        os.remove(audio_path)

    command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        audio_path,
        "-y"
    ]

    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"FFmpeg failed to extract audio: {e}") from e

    return audio_path


def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    audio_path = os.path.abspath(audio_path)
    model = whisper.load_model(model_size)

    try:
        result = model.transcribe(audio_path)
    except Exception as e:
        raise RuntimeError(f"Whisper failed to transcribe audio. Error: {e}")

    return result["text"]



