from locust import HttpUser, between, task
from data.data import Data



class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def get_userinfo(self):
        self.client.get("/v2/user/hasankselek")

    @task
    def post_user_create(self):

        self.client.post("/v2/user", json=Data.user_create_payload())

    @task
    def get_user_login(self):

        self.client.get("/v2/user/login?",params=Data.params_payload(),name="/v2/user/login?")

    @task
    def get_user_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def put_user_uptade(self):

        self.client.put("/v2/user/hasankselek", json=Data.user_update_payload(), headers=Data.headers_payload())

    @task
    def delete_user(self):
        self.client.post("/v2/user", json=Data.user_create_payload())
        self.client.delete("/v2/user/hasankselek")

    @task
    def post_create_with_list(self):

        self.client.post("/v2/user/createWithList", json=Data.user_create_with_list(), headers=Data.headers_payload())

    @task
    def post_create_with_array(self):

        self.client.post("/v2/user/createWithArray", json=Data.user_create_with_array(), headers=Data.headers_payload())
