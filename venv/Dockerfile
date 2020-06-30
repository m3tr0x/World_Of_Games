FROM python:3.6.5
RUN mkdir /opt/wog
ADD . /opt/wog
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /opt/wog
RUN chmod 644 *.py
CMD ["python", "MainScores.py"]