FROM ubuntu:latest
MAINTAINER parth shah <parth@parthhosting.com>
LABEL Description="This image is simple flask demo server"\
        Vendor="Parth Shah"\
        Version="0.1"
RUN apt-get -y update
RUN apt-get -y install python3 python3-dev python3-pip
RUN pip3 install --upgrade pip
# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
# tell the port number the container should expose
EXPOSE 5000
# run the application
CMD ["python3", "/usr/src/app/app.py"]