import time
import operator
from TikTokApi import TikTokApi
from typing import List
import os
from moviepy.editor import *
from natsort import natsorted
from google.cloud import storage




def run_download(
    request
) -> None:
    try: 
        # values = request.form
        # hash_tag = values['hash_tag']
        hash_tag = request
        verify_fp = "verify_kzu8er2q_RX7qGRh6_tLFr_4XZa_BxGD_oaNmpdRX7yxi"
        api: TikTokApi = TikTokApi(custom_verifyFp=verify_fp)
        os.chdir('/tmp')
        download_videos(
            filter_by(
                tag=hash_tag,
                api=api,
            )
        )
        time.sleep(3)
        concat_videos(file_name=hash_tag)
    except Exception as e: 
        print(str(e))
        return str(e)



def filter_by(
    username: str = None,
    tag: str = None,
    sound: str = None,
    user_interaction: str = "diggCount",
    number_of_history: int = 30,
    number_of_most_interacted: int = 10,
    api: TikTokApi = None,
):
    if not username in [None, ""]:
        user_videos = api.user(username=username).videos(count=number_of_history)
    elif not tag in [None, ""]:
        user_videos = api.hashtag(name=tag).videos(count=number_of_history)
    elif not sound in [None, ""]:
        user_videos = api.sound(id=sound).videos(count=number_of_history)
    else:
        user_videos = api.trending().videos(count=number_of_history)

    interaction_list: List[int] = []
    video_list = []
    for video in user_videos:
        interaction_list.append(video.as_dict["stats"][user_interaction])
        video_list.append(video)

    enumerate_object = enumerate(interaction_list)
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)
    index_list = [index for index, element in sorted_pairs]

    most_interacted_videos = []
    for video_index in index_list[0:number_of_most_interacted]:
        most_interacted_videos.append(video_list[video_index])

    return most_interacted_videos


def download_videos(video_list: List):
    for i, video in enumerate(video_list):
        video_bytes = video.bytes()
        with open("video" + str(i) + ".mp4", "wb") as out:
            out.write(video_bytes)


#### CONCATENATION


def concat_videos(file_name):
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

    upload_blob("video_bucket_function_store", 'output.mp4', 'output.mp4')
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



def upload_blob(gcloud_bucket_name, source_file_name, destination_blob_name): 
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(gcloud_bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


if __name__ == '__main__':
    run_download(sys.argv[1])