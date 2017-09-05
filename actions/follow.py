import stream

try:
    # Establishes Connection
    client = stream.connect('KEY', 'SECRET')

    # Instantiate a feed object
    user_feed = client.feed('user', 'test')
    user_feed_2 = client.feed('user', 'test2')

    # Follow another user
    user_feed.follow('user', 'test2')

    print("Feed successfully updated")

except Exception as e:
    print("Error: {0}".format(e))
