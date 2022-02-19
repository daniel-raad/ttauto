from TikTokApi import TikTokApi
import json


verify_fp = "verify_kzu8er2q_RX7qGRh6_tLFr_4XZa_BxGD_oaNmpdRX7yxi"

api = TikTokApi(custom_verify_fp=verify_fp)

video_list = []
for video in api.hashtag(name="motivation").videos(count=5):
    video_list.append(video)


video = video_list[0]

with open("video_info.txt", "w") as convert_file:
    convert_file.write(json.dumps(video.as_dict))
