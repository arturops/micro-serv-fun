FROM python:3.10.12
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /backendservice
COPY requirements.txt /backendservice/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backendservice