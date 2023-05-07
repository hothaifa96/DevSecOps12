FROM python:3.10.11-alpine3.17
WORKDIR /flask-app
COPY . .
RUN pip install -r requirments.txt
# install all python packages 
ENV FLASK_APP=main.py
EXPOSE 19000
CMD flask run --port=19000 --host=0.0.0.0