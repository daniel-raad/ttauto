FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

ADD requirements.txt / 

RUN pip install -r requirements.txt 
ADD main.py /

ENTRYPOINT ["python", "./main.py"]