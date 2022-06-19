# module imports
import os
from flask import Flask, request
from flask_restful import Resource, Api
from models import db_session
import random

__version__ = 1.0

api = Api()

machop_port = 5011
machop_id = 11

access_token = 'Bearer this-is-my-bearer-token'
response_keys = ['MachOP_id',
                 'time_stamp',
                 'temp_sensor',
                 'moisture_sensor',
                 'oxygen_level',
                 'uptime']


def create_app(config_file):
    """
    The application factory to create multiple instances of Flask app
    :param config_file: the config file used for Flask
    :return: the application instance
    """
    # initialize the Flask app and get the configuration from file
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    # initialize the Api and db
    api.init_app(app)
    # db_session.init_app(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        This method re-allocates the memory for db
        when the app is closed.
        """
        db_session.remove()

    return app


class SensorsInfo(Resource):
    """
    This resource handles the HTTP request to fetch sensor data
    """
    def get(self):
        response = None
        # validate the token and send sensor data only if success
        if request.headers["Authorization"] == access_token:
            response = {'MachOP_id': machop_id,
                'time_stamp': f'{random.randint(1, 31)}-{random.randint(1, 12)}-2022 '
                              f'{random.randint(0, 59)}:{random.randint(0, 59)} AM',
                'temp_sensor': random.uniform(0, 50),
                'moisture_sensor': random.uniform(0, 40),
                'oxygen_level': random.uniform(0, 100),
                'uptime': f'{random.randint(0, 100)}d:{random.randint(0, 23)}'
                          f'h:{random.randint(0, 59)}m:{random.randint(0, 59)}s'}
        else:
            response = {'Status': 'Error'}
        return response


class AboutMachop(Resource):
    """
    This resource handles the version info for the MachOp
    """
    def get(self):
        return {'machop_details': {'software_version': __version__}}


class GetSensorInfo(Resource):
    """
    This resource handles the HTTP request for individual sensor parameters
    """
    response = None

    def get(self, sensor):
        # validate the token and send sensor data only if success
        if request.headers["Authorization"] == access_token:
            if sensor in response_keys:
                response = {sensor: random.uniform(0, 50)}
            else:
                response = {'Status': 'Invalid Sensor'}
        else:
            return {'Status': 'Error'}
        return response


class Home(Resource):
    """
    This resource handles the home endpoint
    """
    def get(self):
        return {'Status': 'Welcome come to Protix programming challenge'}


# add the API resources
api.add_resource(SensorsInfo, '/fetch_data')
api.add_resource(AboutMachop, '/about')
api.add_resource(Home, '/')
api.add_resource(GetSensorInfo, '/<string:sensor>')


if __name__ == '__main__':
    """
    The main entry point for this app
    """
    # create the Flask app and run.
    app = create_app('config.py')
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

