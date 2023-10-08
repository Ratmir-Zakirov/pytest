import requests
from config import PATH_URL
from config import SERVICE_URL
from src.json_schemas.post import POST_SCHEMA
from src.base_classes.response import Response

URL = SERVICE_URL + PATH_URL


def test_get_post():
    received_response = requests.get(url=URL)
    response =  Response(received_response)
    assert response.assert_status_code(200).validate(POST_SCHEMA)
