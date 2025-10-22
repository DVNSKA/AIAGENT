import ffmpeg
import os

def extract_audio(video_path, output_folder="data/outputs"):
    os.makedirs(output_folder, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_folder, f"{base_name}_audio.wav")

    (
        ffmpeg
        .input(video_path)
        .output(audio_path, format="wav", acodec="pcm_s16le", ac=1, ar="16k")
        .overwrite_output()
        .run(quiet=True)
    )

    return audio_path
