FROM python:3.14
LABEL maintainer="toto@provider.com>"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "./mod_main.py" ]
