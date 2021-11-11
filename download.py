# Input a hard coded tag and take the first 10 videos from TikTok 
from TikTokApi import TikTokApi
from datetime import datetime 
import json
import operator

def filter_by(username=None, tag=None, user_interaction='diggCount', number_of_history=10, number_of_most_interacted=5):

    if username is not None: 
        user_videos = api.by_username(username, number_of_history)
    else: 
        user_videos = api.by_hashtag(tag, number_of_history)
    
    interaction_list = [] 
    for video in user_videos:
        interaction_list.append(video['stats'][user_interaction])

    enumerate_object = enumerate(interaction_list) 
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)
    index_list = [index for index, element in sorted_pairs]
    most_interacted_videos = [] 
    for video_index in index_list[0:number_of_most_interacted]:
        most_interacted_videos.append(user_videos[video_index])
    
    return most_interacted_videos




def download_videos(video_list, device_id):
    for i, video in enumerate(video_list):
        video_bytes = api.get_video_by_tiktok(video, custom_device_id=device_id)
        with open("video" + str(i) + ".mp4", "wb") as out:
            out.write(video_bytes)





if __name__ == '__main__':
    api = TikTokApi.get_instance()
    username = "emilymariko"
    device_id = api.generate_device_id()
    download_videos(filter_by(username=username), device_id)

