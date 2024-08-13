from locust import HttpUser, between, task
from data.data import Data


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def get_user_info(self):
        self.client.get("/v2/user/cevdetpost")

    @task
    def user_create(self):
        self.client.post("/v2/user", json=Data.user_create_payload())

    @task
    def user_login(self):
        self.client.get("/v2/user/login?", params=Data.params_payload(), name="/v2/user/login")

    @task
    def user_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def user_update(self):
        self.client.put("/v2/user/cevdetpost", json=Data.user_create_payload(), headers=Data.headers_payload())

    @task
    def user_delete(self):
        self.client.post("/v2/user", json=Data.user_create_payload())
        self.client.delete("/v2/user/cevdetpost")

    @task
    def user_create_with_list(self):
        self.client.post("/v2/user/createWithList", json=Data.create_user_with_list())

    @task
    def user_create_with_array(self):
        self.client.post("/v2/user/createWithArray", json=Data.create_user_with_array(), headers=Data.headers_payload())
