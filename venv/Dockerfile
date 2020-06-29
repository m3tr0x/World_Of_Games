FROM python:alpine
RUN mkdir /opt/wog
RUN pip install flask selenium pathlib
ADD . /opt/wog
CMD [ "python", "/opt/wog/MainScores.py" ]