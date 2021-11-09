# Input a hard coded tag and take the first 10 videos from TikTok 
from TikTokApi import TikTokApi
from datetime import datetime 
import json
import operator

def filter_by_username(username, number_of_history, number_of_most_liked):
    return 0 

def filter_by_tag(tag, number_of_history, number_of_most_liked): 
    return 0 

if __name__ == '__main__':
    api = TikTokApi.get_instance()
    print(api)
    username = "emilymariko"
    # This is generating the tt_webid_v2 cookie
    # need to pass it to methods you want to download
    device_id = api.generate_device_id()

    user_videos = api.by_username(username, 10)
    like_list = [] 
    for video in user_videos:
        like_list.append(video['stats']['diggCount'])
    print(like_list)
    enumerate_object = enumerate(like_list) 
    sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)
    index_list = [index for index, element in sorted_pairs]
    most_liked_videos = [] 
    for video_index in index_list[0:2]:
        most_liked_videos.append(user_videos[video_index])

    for i, video in enumerate(most_liked_videos):
        video_bytes = api.get_video_by_tiktok(video, custom_device_id=device_id)
        with open("video" + str(i) + ".mp4", "wb") as out:
            out.write(video_bytes)

    # json.dumps(api.get_data(url=""))
    # for video in user_videos:  
    #     videoJson = api.get_tiktok_by_url()
    # print(videoJson['itemInfo']['itemStruct']['stats']['diggCount'])
    # print(videoJson['itemInfo']['itemStruct']['id'])
