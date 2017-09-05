import stream

try:
    # Establishes Connection
    client = stream.connect('KEY', 'SECRET')

    # Instantiate a feed object
    user_feed = client.feed('user', 'test')

    # Create a new activity
    user_feed.add_activity({'actor': 'test', 'verb': 'tweet', 'object': 1, 'tweet': 'Hello mundo'})

    print("Feed successfully updated")

except Exception as e:
    print("Error: {0}".format(e))
