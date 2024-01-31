FROM python:latest

WORKDIR /baackend

COPY . /baackend

RUN pip install -r requirements.txt

CMD uvicorn main:app --reload --host 0.0.0.0

# docker build -t fastapi-app .
# docker run -it -p 8000:8000 fastapi-app