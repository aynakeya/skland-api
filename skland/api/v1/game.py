from typing import List

from skland.api import ZonaiGameApi, ZonaiApiClient, AppBindingContainer


class ZonaiGameApiImpl(ZonaiGameApi):
    def __init__(self, client: ZonaiApiClient):
        self.client = client

    def player_info(self, uid: str) -> dict:
        return self.client.get(
            f"/api/v1/game/player/info?uid={uid}"
        ).data

    def player_binding(self) -> List[AppBindingContainer]:
        return [AppBindingContainer.from_dict(item) for item in self.client.get(
            "/api/v1/game/player/binding?"
        ).data["list"]]
