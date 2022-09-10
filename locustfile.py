# Print "locust" into the Bash to start load test
from locust import HttpUser, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.get('/pinger')
