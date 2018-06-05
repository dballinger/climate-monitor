FROM jsurf/rpi-raspbian

RUN apt-get update
RUN apt-get install -y wget 
RUN apt-get install -y python-dev 
RUN apt-get install -y python-smbus 

ADD logger.py logger.py
RUN wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py

CMD python "logger.py"
