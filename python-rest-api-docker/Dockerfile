FROM python:3.12-alpine

ENV FLASK_APP=controller.py \
    LANG=en_US.UTF-8

COPY src /apps
WORKDIR /apps

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]