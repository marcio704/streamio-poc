
Testing the basic concepts of Stream.io (https://getstream.io) using the Python lib

INSTALLATION
============

Clone project:

`$ git clone git@github.com:marcio704/streamio-poc.git`

`$ cd streamio`


Create virtualenv and install dependencies:

`$ virtualenv /the/path/you/want/venv`

`$ source /the/path/you/want/venv/bin/activate`

`$ pip install -r requirements.txt`


Run actions:

`python actions/write_to_feed_batch.py`

`python actions/write_to_feed_single.py`

`python actions/follow.py`

`python actions/get_feed.py`
