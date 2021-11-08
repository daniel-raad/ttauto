# Input a hard coded tag and take the first 10 videos from TikTok 
from TikTokApi import TikTokApi
from datetime import datetime 

if __name__ == '__main__':
    api = TikTokApi.get_instance()
    print(api)
    username = "therock"
    # This is generating the tt_webid_v2 cookie
    # need to pass it to methods you want to download
    device_id = api.generate_device_id()

    # trending = api.by_trending(custom_device_id=device_id)
    user_videos = api.by_username(username, 10)
    # Below is if the method used if you have the full tiktok object
    for i in range(1,4):
        video_bytes = api.get_video_by_tiktok(user_videos[i], custom_device_id=device_id)
        with open("video" + str(i) + ".mp4", "wb") as out:
            out.write(video_bytes)
