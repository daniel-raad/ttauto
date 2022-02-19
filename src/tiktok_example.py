from itertools import count
from TikTokApi import TikTokApi


verify_fp = "verify_kzu8er2q_RX7qGRh6_tLFr_4XZa_BxGD_oaNmpdRX7yxi"

api = TikTokApi(custom_verify_fp=verify_fp)

for video in api.hashtag(name="motivation").videos(count=5):
    print(video.as_dict["stats"]["diggCount"])
    print(video)
