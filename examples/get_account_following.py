from context import Instagram # pylint: disable=no-name-in-module
from time import sleep

instagram = Instagram()
instagram.with_credentials('james_kumar_129', '4[PQ)yRE7.M;cq3', '/home/robin/projects/instagram-scraper/cache')
instagram.login()

sleep(2) # Delay to mimic user

username = 'kevin'
following = []
account = instagram.get_account(username)
sleep(1)
following = instagram.get_following(account.identifier, 150, 100, delayed=True) 
for following_user in following['accounts']:
    print(following_user)