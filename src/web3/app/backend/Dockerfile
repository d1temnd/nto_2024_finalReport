FROM python:3.11
RUN pip3 install -v gunicorn==20.0.4
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
COPY . ./
CMD gunicorn --threads 8 --bind 0.0.0.0:8000 app:app
