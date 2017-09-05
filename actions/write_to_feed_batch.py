import stream

try:
    # Establishes Connection
    client = stream.connect('KEY', 'SECRET')

    # Instantiate a feed object
    user_feed = client.feed('user', 'test')

    # Batch adding activities
    activities = [
        {'actor': 'test', 'verb': 'tweet', 'object': 5,'tweet': 'Hello batch'},
        {'actor': 'test', 'verb': 'watch', 'object': 6,'tweet': 'Hello batch 2'}
    ]
    user_feed.add_activities(activities)

    print("Feed successfully updated")

except Exception as e:
    print("Error: {0}".format(e))
