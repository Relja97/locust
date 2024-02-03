from locust import HttpUser, task, tag

class TestGet(HttpUser):

    @tag('ocekuj200')
    @task()
    def testGet_200(self):
        response = self.client.get("/endpoint_200")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    @tag('ocekuj401')
    @task
    def testGet_401(self):
        self.client.get("/endpoint_401")

    @tag('ocekuj403')
    @task
    def testGet_403(self):
        response = self.client.get("/endpoint_403")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    @tag('ocekuj500')
    @task
    def testGet_500(self):
        response = self.client.get("/endpoint_5xx")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"