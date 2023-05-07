FROM python:latest
WORKDIR /coloredapp
COPY . .
RUN pip install -r requirments.txt
ENV FLASK_APP=color.py
EXPOSE 5080
CMD flask run --port=5080 --host=0.0.0.0