import os
from moviepy.editor import *
from natsort import natsorted


def concat_videos():
    # subprocess.call('./concatenate.sh')
    video_files = []
    audio_files = []

    f = open("temp-audio.m4a", "w")

    for root, dirs, files in os.walk("./"):

        files = natsorted(files)
        for file in files:
            if os.path.splitext(file)[1] == ".mp4":
                file_path = os.path.join(root, file)
                video = VideoFileClip(file_path)
                convert_video_to_audio_moviepy(file_path)
                video_files.append(video)
                file_path = file_path[:-1] + "3"
                audio_files.append(file_path)
                os.remove(file)

    clips = [AudioFileClip(c) for c in audio_files]
    print(clips)
    final_audio_clip = concatenate_audioclips(clips)
    final_audio_clip.write_audiofile("./output_audio.mp3")

    audioclip = AudioFileClip("./output_audio.mp3")
    final_clip = concatenate_videoclips(video_files, method="compose")
    final_clip_with_audio = final_clip.set_audio(audioclip)

    final_clip_with_audio.write_videofile(
        filename="./output.mp4",
        temp_audiofile="temp-audio.m4a",
        fps=None,
        codec="libx264",
        audio_codec="aac",
        bitrate=None,
        audio=True,
        audio_fps=44100,
        preset="medium",
        audio_nbytes=4,
        audio_bitrate=None,
        audio_bufsize=2000,
        rewrite_audio=True,
        verbose=True,
        threads=None,
        ffmpeg_params=None,
    )

    clean_up(audio_files=audio_files)


def clean_up(audio_files):
    os.remove("output_audio.mp3")
    [os.remove(c) for c in audio_files]


def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")
