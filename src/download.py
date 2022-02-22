from itertools import count
import operator
from TikTokApi import TikTokApi
from typing import List


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
