from facebook_scraper import get_posts


import json
from facebook_scraper import get_posts, set_noscript, get_profile
from facebook_scraper import get_group_info
from time import sleep
import pandas as pd
from pymongo import MongoClient
import datetime
import numpy as np

def main():
    # uri = 'mongodb+srv://edwardly1002:Ltb123%21%40%23@cluster0.lqbbu.mongodb.net/test'
    uri  ='mongodb+srv://fbfighter:fbfighter@fb-topic.ixbkp2u.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient( uri )
    db_post = client.fakenews.testpostcmtreactor

    ls_account = ["connguoidongnai", "fan24h", "danquan10tphcm", "YHocThucHanh", "Hà-Nội-24h-100310082162739"]
    ls_group = ["suckhoetainha", "VietnamProjectsConstructionGROUP", "714257262432794", "j2team.community", "1539634912979915", "TAMLYHOCHANHVI.098" ]
    GROUP_IDS = [
        'VietnamProjectsConstructionGROUP',
        # 'tinnongbaomoi24h',
        # '714257262432794',
        # 'tinnonghoi.vn',
        # 'tintuc2',
        # 'TAMLYHOCHANHVI.098',
        # '171952859547317',
        # '273257912789357',
        # 'u23fanclub',
        # 'bodoimethienha6789',
        # 'namdinh24h',
        # 'tintuctiengiang24h',
        # '269067133142215',
        # '981079245730615',
        # 'tintucnong24hhomnay',
        # '432103080239697',
        # '755877398632288',
        # "suckhoetainha",
        # "j2team.community"
    ]
    # group_id = "tinnonghoi.vn"
    for group_id in GROUP_IDS[::-1]:
        try:
            ls_post = get_posts(group = group_id, cookies = "from_browser", options={"comments":True, "reactors": True, "sharers": True})
            counter = 0
        
            for post in ls_post:
                try:
                    with open('fb_test.json', 'a', encoding='utf-8') as f:
                        json.dump(post, f, ensure_ascii=False, default=str)
                        f.write("\n")
                        post["group_id"] = group_id
                        if "post_id" in post:
                            df_post =  pd.DataFrame(list(db_post.find({"post_id": {"$eq": post["post_id"]}})))
                            print(df_post.shape)
                            if df_post.shape[0] == 0:
                                db_post.insert_one(post)
                        print("GROUP ID: ", group_id, " COUNTER: ", counter)
                        counter += 1
                        sleep(10)
                except Exception as e:
                    continue

        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()