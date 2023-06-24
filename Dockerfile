FROM python:3.9.16-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install gcc wget git -y

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "chainlit", "run", "main.py", "-w", "--port", "3000"]