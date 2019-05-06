FROM ubuntu:16.04

MAINTAINER Your Name "prasanna.pawar43@gmail.com"

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y libmysqlclient-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install Packages
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY deploy/run /app/deploy/run
COPY . /app
WORKDIR /app


EXPOSE 5000

RUN bash -x -c "ln -s /app/deploy/run /usr/local/bin/run && chmod +x /usr/local/bin/run"
CMD /usr/local/bin/run
