from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages

# post_count = len(post)
#     assert post_count == 3, GlobalErrorMessages.BAD_ELEMENTS_COUNT.value

class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.BAD_STATUSE_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.BAD_STATUSE_CODE.value
        return self
