
# colred flask app 

## this flask app take env and return in the home resource / a html page with the color in the background 

### how to run this code 
#### first of all clone this repo 
#### add a Dockerfile to it 
#### isntall all the packages using pip as in this command using the requirmetns.txt
##### pip install -r file.txt
#### expose port 5080 or another one id you must 

## declare 2 ENV's 


resources:
| FLASK_APP       | APP_COLOR     |
| --------------- | ------------- |
| file name       | color (text)  | 

  
 # use postman to see that the flask app is runnig 
  


resources:
| resource        | Methods       | 
| --------------- | ------------- | 
| /               | GET           | 
  
  
