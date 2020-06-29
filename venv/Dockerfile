FROM python:3.6.5
RUN mkdir /opt/wog
WORKDIR /opt/wog
RUN pip install --upgrade pip
RUN pip install flask selenium pathlib
ADD . /opt/wog
CMD ["python", "MainScores.py"]