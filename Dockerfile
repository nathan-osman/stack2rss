FROM alpine:edge
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>

# Install uWSGI and Python
RUN apk add --no-cache \
        python3 \
        uwsgi \
        uwsgi-python3 \
        uwsgi-corerouter \
        uwsgi-router_http \
        uwsgi-http

# Add the list of requirements
ADD requirements.txt /var/lib/stack2rss/

# Install the requirements
RUN pip3 install -r /var/lib/stack2rss/requirements.txt

# Copy all the files over
ADD static /var/lib/stack2rss/static
ADD templates /var/lib/stack2rss/templates
ADD feed.py /var/lib/stack2rss/
ADD stack2rss.py /var/lib/stack2rss/
ADD types.json /var/lib/stack2rss/

# Specify the command for running the server
CMD [ \
    "uwsgi", \
    "--plugin", "python3,http", \
    "--http", "0.0.0.0:80", \
    "--chdir", "/var/lib/stack2rss/", \
    "--module", "stack2rss:app", \
    "--static-map", "/static=/var/lib/stack2rss/static", \
    "--http-keepalive" \
]

# Expose port 80
EXPOSE 80
