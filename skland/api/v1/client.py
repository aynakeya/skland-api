import httpx

from skland.api import ZonaiApiClient, ZonaiResponse
from skland.model.exception import SklandApiException


class HttpxClient(ZonaiApiClient):

    def __init__(self, base_url: str, version="0.1.1"):
        super().__init__()
        self.version = version
        self.client = httpx.Client()
        self.client.base_url = base_url
        self.cred = ""
        self.client.headers.update({
            "User-Agent": f"Skland/{self.version} (com.hypergryph.skland; build:101058; iOS 16.5.1) Alamofire/5.7.1",
            "os": "iOS",
            "platform": "2",
            "manufacturer": "Apple",
            "nid": "1",
            "vName": self.version
        })

    def set_credential(self, cred: str):
        self.cred = cred
        self.client.headers.update(
            {"cred": cred}
        )

    def __process_response(self, resp: httpx.Response) -> ZonaiResponse:
        try:
            resp: ZonaiResponse = ZonaiResponse.from_dict(resp.json())
            if resp.code != 0:
                raise SklandApiException(resp.code, resp.message)
            return resp
        except SklandApiException as e:
            raise e
        except Exception as e:
            raise SklandApiException(-1, str(e))

    def get(self, path, headers=None) -> ZonaiResponse:
        return self.__process_response(
            self.client.get(path, headers=headers)
        )

    def post(self, path, data=None, headers=None) -> ZonaiResponse:
        return self.__process_response(
            self.client.post(path, json=data, headers=headers)
        )

    def put(self, path, data=None, headers=None) -> ZonaiResponse:
        return self.__process_response(
            self.client.put(path, json=data, headers=headers)
        )

    def delete(self, path, data=None, headers=None) -> ZonaiResponse:
        return self.__process_response(
            self.client.request(
                "DELETE",
                path,
                json=data,
                headers=headers
            )
        )
