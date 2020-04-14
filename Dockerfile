FROM python:3
WORKDIR /var/app
COPY . /var/app
RUN pip install flask
CMD [ "python", "Jenkins.py"]
