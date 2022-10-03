from download import download_videos, filter_by
from concat import concat_videos
import time
import argparse
from TikTokApi import TikTokApi


def run_download(
    user_name: str = None, hash_tag: str = None, music_sound: str = None
) -> None:
    attempts: int = 0
    verify_fp = "verify_kzu8er2q_RX7qGRh6_tLFr_4XZa_BxGD_oaNmpdRX7yxi"

    # while attempts < 50:
    #     try:
    api: TikTokApi = TikTokApi(custom_verifyFp=verify_fp)

    download_videos(
        filter_by(
            username=user_name,
            tag=hash_tag,
            sound=music_sound,
            api=api,
        )
    )
    time.sleep(3)
    concat_videos()
        #     break
        # except Exception as e:
        #     print(e)
        #     attempts += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Youtube Automation Program")
    parser.add_argument("-t", "--hash_tag", type=str)
    parser.add_argument("-u", "--user_name", type=str)
    parser.add_argument("-i", "--interaction_type", type=str)
    parser.add_argument("-n", "--number_history", type=int)
    parser.add_argument("-m", "--most_interacted", type=int)
    parser.add_argument("-s", "--music_sound", type=int)
    args = parser.parse_args()

    run_download(
        user_name=args.user_name,
        hash_tag=args.hash_tag,
        music_sound=args.music_sound,
    )
