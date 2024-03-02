import allure
import requests


class HTTPClient:
    """
    Расширение стандартного клиента requests.
    """

    def __init__(self):
        self.base_url = "https://sampleapis.com/api-list/futurama"

    @allure.step('Making "{method}" to "{url}"')
    def request(self, method, url, **kwargs):
        """
        Расширение логики метода requests.request с добавлением логирования типа запроса и его URL.
        :param method: метод, который мы используем (POST, GET и т.д.)
        :param url: путь на домене, по которому отправляем запрос
        """
        return requests.request(method, f"{self.base_url}{url}", **kwargs)


class ApiClient:
    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
