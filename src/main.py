from download import download_videos, filter_by
from concat import concat_videos
import time 
import argparse
from TikTokApi import TikTokApi


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Youtube Automation Program')
    parser.add_argument('-t', "--hash_tag", type=str)
    parser.add_argument('-u', '--user_name', type=str)  
    parser.add_argument('-i', '--interaction_type', type=str)
    parser.add_argument('-n', '--number_history', type=int)
    parser.add_argument('-m', '--most_interacted', type=int)
    parser.add_argument('-s', '--music_sound', type=int)
    args = parser.parse_args() 

    attempts = 0
    verify_id = "verify_kwhqoq3n_gMReqQzN_qdAS_44P0_A2qM_g6UEOjeiiIo0"

    while attempts < 50: 
        try:
            api = TikTokApi.get_instance(custom_verifyFp=verify_id, use_test_endpoints=True)
            device_id = api.generate_device_id()

            download_videos(filter_by(username=args.user_name, tag=args.hash_tag, sound=args.music_sound, api=api), device_id, api)
            time.sleep(3) 
            concat_videos()
            break 
        except Exception as e: 
            print(e)
            attempts += 1 