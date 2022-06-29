from pprint import pprint
import instagram_scraper

args = {"login_user": "zhuangyaoalex", "login_pass": "pwd"}

insta_scraper = instagram_scraper.InstagramScraper(**args)
insta_scraper.authenticate_with_login()
shared_data = insta_scraper.get_shared_data_userinfo(username='moutai.china')

arr = []

for item in insta_scraper.query_media_gen(shared_data):
    arr.append(item)

pprint(arr)