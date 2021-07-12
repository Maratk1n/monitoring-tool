FROM python:3.7-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

# install libseccomp for ARM
# https://github.com/linuxserver/docker-papermerge/issues/4
RUN wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.5.1-1_armhf.deb && \
    dpkg -i libseccomp2_2.5.1-1_armhf.deb && rm libseccomp2_2.5.1-1_armhf.deb && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./receiver.py" ]
