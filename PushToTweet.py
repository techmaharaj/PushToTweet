from gpiozero import Button
from twython import Twython
from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

button = Button(2)
button.wait_for_press()
message = 'This is my push to tweet project via #RaspberryPi'
twitter.update_status(status=message)
