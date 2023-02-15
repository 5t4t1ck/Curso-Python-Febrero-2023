from twitter import *
from token import token, token_secret, consumer_key, consumer_secret

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Update your status
t.statuses.update(
    status="Prueba de envío de twit desde Python!!!")

