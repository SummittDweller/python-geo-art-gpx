FROM python:3.5

MAINTAINER Mark McFate

# RUN pip install pyyaml==3.11 requests==2.5.1 lxml
ENV PYTHONPATH /

CMD [ "python", "-u", "/main.py" ]

COPY root /