from locust import HttpUser, task, between, TaskSet


class ShoppingUser(TaskSet):

    @task
    def buy(self):
        response = self.client.get('/shop')
        assert response.status_code == 200
        self.client.get('/shop/buy')

    @task
    def wrong_buy(self):
        response = self.client.get('/shopping/buy')
        assert response.status_code == 404


class DownloadingUser(TaskSet):

    @task
    def about(self):
        self.client.get('/')
        response = self.client.get('/info')
        assert response.text == 'My cool app'

    @task
    def download(self):
        response = self.client.get('/downloads')
        assert response.status_code == 200
        self.client.get('/downloads/gets')


class ReadingUser(TaskSet):

    @task
    def reading(self):
        response = self.client.get('/read')
        assert response.status_code == 200
        self.client.get('/read/text')


class WebSiteUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [ShoppingUser, DownloadingUser, ReadingUser]
