FROM debian:stable

RUN apt-get update -y
RUN apt-get install -y postfix bash curl vim python3 python3-pip python3.11-venv
RUN apt-get install -y syslog-ng

COPY main.cf /etc/postfix
COPY master.cf /etc/postfix
COPY virtual /etc/postfix

CMD bash /mail/run

