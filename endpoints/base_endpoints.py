class Endpoints:
    response = None

    def check_response_is_201(self):
        assert self.response.status_code == 201

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_400(self):
        assert self.response.status_code == 400
