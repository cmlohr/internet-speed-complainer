from check_internet_speed import SpeedCheck
from twitter_bot import TwitterBot
import time

check_internet_speed = SpeedCheck()
check_internet_speed.get_speed()

# runs the speed test
upload_speed = float(check_internet_speed.upload_speed())
# assigns variables for condition and f-strings
download_speed = float(check_internet_speed.download_speed())
check_internet_speed.quit()

print(">>> checking msg_condition")
if download_speed < 100.00:  # change to match the guaranteed terms of your isp
    time.sleep(1)
    print(">>> main.preparing msg")
    twitter = TwitterBot()
    twitter.sign_in()
    time.sleep(1)
    message = f"♪┏(・o･)┛♪ UPLOAD SPEED: {upload_speed}\n┗ ( ･o･) ┓♪ DOWNLOAD SPEED: {download_speed}"
    twitter.tweet(message)
    print(">>> main.message sent")
    twitter.quit()  # comment out to keep window open at the end
