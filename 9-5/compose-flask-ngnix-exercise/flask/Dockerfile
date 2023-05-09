FROM python
WORKDIR /flaskapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 9091
ENV FLASK_APP=server.py
ENV FLASK_SERVER_PORT=9091
CMD python3 server.py