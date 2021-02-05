# Grab the latest alpine image
FROM python:3.8

# Add requirements and install dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD . /opt/app/
WORKDIR /opt/app

# Run the app with CMD as required by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app
