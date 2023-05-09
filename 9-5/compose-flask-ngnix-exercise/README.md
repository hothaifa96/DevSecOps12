## Compose application

### Python/Flask application with Nginx proxy and a Mongo database

Project structure:
```

├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
└── nginx
    └── nginx.conf


## front end 
### ngnix fron end runs at 80 port 
### no need to install anything 
environment variables : 
      FLASK_SERVER_ADDR=((flask service name)):((flaskport))
### the application depnds on the backend 

## back end 
### flask app runs in this prot : 9091 u
### env  FLASK_SERVER_PORT=9091
### the application depnds on the mongo db  


you need to add volume to the db at - vol name :/data/db



After the application starts, navigate to `http://localhost:80` in your web browser or run:
```
Hello from the MongoDB client!
```
