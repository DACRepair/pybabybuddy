from requests import Session, Response


class BBAPIBase:
    def __init__(self, url_base: str, api_key: str, debug: bool = False):
        self._base_url = url_base.rstrip("/")

        self._session = Session()
        self._session.headers.update({"Authorization": "Token {}".format(api_key)})

        if self._api_resp_validate(self._api_get()) and debug:
            print(f"Connected to API endpoint: {self._api_url()}")

    def _api_url(self, endpoint: str = None) -> str:
        full_url = f"{self._base_url}/api"
        if endpoint is not None:
            full_url = f"{full_url}/{endpoint}"
        return full_url

    def _api_resp_validate(self, response: Response) -> Response:
        if not 200 <= response.status_code <= 299:
            raise ValueError(f"Invalid API call to: {response.url}. Error {response.status_code}: {response.text}")
        return response

    def _api_get(self, endpoint: str = None, *args, **kwargs) -> Response:
        return self._api_resp_validate(self._session.get(self._api_url(endpoint), *args, **kwargs))

    def _api_post(self, endpoint: str = None, *args, **kwargs) -> Response:
        return self._api_resp_validate(self._session.get(self._api_url(endpoint), *args, **kwargs))

    def _api_patch(self, endpoint: str = None, *args, **kwargs) -> Response:
        return self._api_resp_validate(self._session.get(self._api_url(endpoint), *args, **kwargs))
