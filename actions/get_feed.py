import stream

try:
    # Establishes Connection
    client = stream.connect('KEY', 'SECRET')

    # Get user feed
    user_feed_1 = client.feed('user', 'test')
    result = user_feed_1.get(limit=5)

    print("User 'test' feed: {0}".format(result))

    following = user_feed_1.following()
    print("User 'test' is following: {0}".format(following))

except Exception as e:
    print("Error: {0}".format(e))

