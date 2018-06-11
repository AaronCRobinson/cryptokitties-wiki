FROM debian:latest
LABEL maintainer "Aaron Robinson"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
    python \
    python-imaging \
    python-pip \
    python-setuptools \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

RUN pip install wheel

RUN pip install wiki==0.2.5

ADD testproject /testproject/

RUN ln -s /testproject/testproject/db /db && \
    ln -s /testproject/testproject/templates /templates && \
    ln -s /testproject/testproject/settings /settings && \
    chmod 777 /testproject/testproject/settings && \
    ln -s /testproject/testproject/media /wikimedia && \
    chmod 777 /testproject/testproject/media

EXPOSE 8000

ENTRYPOINT ["python","/testproject/manage.py","runserver","0.0.0.0:8000"]
