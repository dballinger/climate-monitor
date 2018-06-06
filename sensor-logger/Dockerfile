FROM jsurf/rpi-raspbian

RUN apt-get update
RUN apt-get install -y wget 
RUN apt install -y python3
#RUN apt-get install -y python-dev 
RUN apt-get install -y python3-smbus 
#RUN apt-get install -y python-influxdb
#RUN apt-get install -y python-pip build-essential
#RUN pip install --upgrade pip
#RUN pip install --upgrade virtualenv
RUN apt-get install -y python3-setuptools
RUN easy_install3 pip
RUN pip3 install influx-client

ADD logger.py logger.py
RUN wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py
RUN sed -i 's/\(print\)\(.*\)$/\1(\2)/g' bme280.py

CMD python3 "logger.py"
