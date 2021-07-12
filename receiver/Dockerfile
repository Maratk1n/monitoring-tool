FROM python:3.7-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./receiver.py" ]
