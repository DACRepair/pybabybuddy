from .api import BBAPIBase
from .data import Child, Diaper, Feeding


class BabyBuddy(BBAPIBase):
    def children(self, slug: str = None) -> list:
        endpoint = "children"
        if slug is not None:
            endpoint = f"{endpoint}/{slug}"
        request = self._api_get(endpoint)
        response = self._api_resp_validate(request)
        return [Child(x) for x in response.json().get("results")]

    def changes(self, child_id: int = None, limit: int = 10, offset: int = 0) -> list:
        endpoint = "changes"
        request = self._api_get(endpoint, params={"limit": limit, "offset": offset, "child": child_id})
        response = self._api_resp_validate(request)
        return [Diaper(x) for x in response.json().get("results")]

    def feedings(self, child_id: int = None, limit: int = 10, offset: int = 0):
        endpoint = "feedings"
        request = self._api_get(endpoint, params={"limit": limit, "offset": offset, "child": child_id})
        response = self._api_resp_validate(request)
        return [Feeding(x) for x in response.json().get("results")]
