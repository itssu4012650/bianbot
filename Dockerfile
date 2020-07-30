# using Alpine Edge
FROM mrmiss/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/biansepang/userbutt /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/

#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
#
RUN pip3 install -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD ["python3","-m","userbot"]