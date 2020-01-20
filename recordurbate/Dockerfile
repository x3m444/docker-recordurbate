FROM python:3.7

COPY recordurbate /recordurbate
COPY Requirements.txt /Requirements.txt
COPY ffmpeg /usr/local/bin/ffmpeg

RUN pip3 install -r /Requirements.txt

USER 1000
WORKDIR /
ENTRYPOINT ["python3", "-m", "recordurbate.recordurbator"]