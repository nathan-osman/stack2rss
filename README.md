## Stack2RSS

Stack2RSS is a simple [Flask](http://flask.pocoo.org/) website that converts a
Stack Exchange API resource or path to an RSS feed. Despite its simplicity,
Stack2RSS enables the construction of complex RSS feeds.

### Demo

You can view a live instance of the application here:  
http://stack2rss.quickmediasolutions.com

### Installation

#### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nathan-osman/stack2rss/)

#### Locally

Create `virtualenv` and install requirements:

    ./scripts/setup.sh

Run the Flask application:

    ./run.sh stack2rss.py

Visit the application in your browser:

    # Linux
    xdg-open http://localhost:5000

    # OSX
    open http://localhost:5000
