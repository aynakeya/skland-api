from typing import Optional

from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class ZonaiResponse():
    code: int
    message: str
    data: Optional[dict] = None


class ZonaiApiClient:
    def set_credential(self, cred: str):
        raise NotImplemented()

    def get(self, path, headers=None) -> ZonaiResponse:
        raise NotImplementedError()

    def post(self, path, data=None, headers=None) -> ZonaiResponse:
        raise NotImplementedError()

    def put(self, path, data=None, headers=None) -> ZonaiResponse:
        raise NotImplementedError()

    def delete(self, path, data=None, headers=None) -> ZonaiResponse:
        raise NotImplementedError()
