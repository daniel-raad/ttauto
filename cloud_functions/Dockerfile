FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

ADD requirements.txt ./ 

RUN pip install -r requirements.txt 

COPY main.py app.py ./

EXPOSE 8080 

ENTRYPOINT ["python"]

CMD ["app.py"]