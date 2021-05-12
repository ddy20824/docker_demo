# FROM base image
FROM python:3.7.2-stretch

# WORKDI working directory
WORKDIR /app

# ADD add files to image
ADD . /app

# only run when build
RUN pip install -r requirements.txt

# run container
CMD python main.py
