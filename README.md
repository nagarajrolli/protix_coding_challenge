# Coding Challenge Assignment - Protix
This coding challenge creates an API to simulate MachOP.

### Usage
- Use requirements.txt to install all the dependencies for this application.
- Run fixtures.py to populate the sqlite db with data.
- cd to the location of the project. Run the application using python app.py in Windows.
- Launch web browser and type: http://127.0.0.1:5000
- The application has also been containerized and the docker image is hosted in Heroku, under: https://protix-app.herokuapp.com/
- Endpoints:

    / home
    
    /fetch_data returns the sensor data in form of JSON with the following schema:
    
        `schema = {'MachOP_id': 1,

          'time_stamp': '25-12-2022 00:21 AM',

          'temp_sensor': 40.885,

          'moisture_sensor': 38.35,

          'oxygen_level': 86.0,

          'uptime': '40d:18h:60m:45s'}`
   
   /<sensor_type> return the value of the particular sensor (refer the schema for the sensor types)
   
   /about returns the version number of the MachOp
   
Please note that authentication is required for all the endpoints except home and about
