import pytest
import json
from jsonschema import validate
from app import create_app
from models import Base, engine
import fixtures

port = 5011
schema = {'MachOP_id': 1,
          'time_stamp': '25-12-2022 00:21 AM',
          'temp_sensor': 40.885,
          'moisture_sensor': 38.35,
          'oxygen_level': 86.0,
          'uptime': '40d:18h:60m:45s'}
response_keys = schema.keys()


@pytest.fixture()
def app():
    """
    This fixture generates the app object from the
    factory. We can update the config as per the test
    requirements.
    """
    app = create_app('config.py')
    app.config.update(
        {
            'TESTING': True,
            'DEBUG': True,
            'FLASK_ENV': "development"
        }
    )
    yield app


@pytest.fixture()
def db_conn(app):
    """
    This fixture first removes the existing test db under tests folder,
    and the creates a new one.
    """
    # remove the already existing test db under tests folder
    # if os.path.exists("db.sqlite3"):
    #     os.remove("db.sqlite3")
    Base.metadata.create_all(bind=engine)
    fixtures.create_fixtures()


@pytest.fixture()
def client(app):
    """
    This fixture returns the test client
    :param app: the app instance
    :return: test client
    """
    return app.test_client()


def test_machop_schema(client, db_conn):
    """
    Test the machop schema
    :param client: the client instance
    :param db_conn: the db connection
    :return: assertion result
    """
    access_token = 'this-is-my-bearer-token'
    response = client.get('/fetch_data', headers={'Content-Type': 'application/json',
                                                  'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    data = json.loads(response.get_data())
    assert set(data.keys()) == set(response_keys)
    validate(instance=data, schema=schema)


def test_home(client, db_conn):
    """
    This test checks if the root endpoints works as intended
    :param client: the client instance
    :param db_conn: the db connection instance
    :return: the assertion result
    """
    access_token = 'this-is-my-bearer-token'
    response = client.get('/', headers={'Content-Type': 'application/json',
                                        'Authorization': f'Bearer {access_token}'})

    data = json.loads(response.get_data())
    assert data['Status'] == "Welcome come to Protix programming challenge"


def test_get_sensor_details(client, db_conn):
    """
    This test checks if the endpoint that seeks for specific sensor detail works as intended
    :param client: the client instance
    :param db_conn: the db connection instance
    :return: the assertion result
    """
    access_token = 'this-is-my-bearer-token'
    sensor = 'uptime'
    response = client.get(f'/{sensor}', headers={'Content-Type': 'application/json',
                                                 'Authorization': f'Bearer {access_token}'})
    data = json.loads(response.get_data())
    assert sensor in data.keys()
