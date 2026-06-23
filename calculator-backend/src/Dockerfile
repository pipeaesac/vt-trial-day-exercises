FROM python:3.12-alpine

ENV https_proxy=$proxy \
	LANG=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8 \
	FLASK_APP=controller.py

COPY src /apps
WORKDIR /apps

RUN python -V && \
	pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]
