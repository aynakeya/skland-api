from typing import List

from dataclasses_json import dataclass_json, LetterCase
from dataclasses import dataclass


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AppBinding:
    uid: str
    channel_master_id: str
    is_delete: bool
    channel_name: str
    is_default: bool
    is_official: bool
    nick_name: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AppBindingContainer:
    binding_list: List[AppBinding]
    default_uid: str = ""
    app_name: str = ""
    app_code: str = ""


class ZonaiGameApi:
    # todo: to python class
    def player_info(self, uid: str) -> dict:
        raise NotImplemented()

    def player_binding(self) -> List[AppBindingContainer]:
        raise NotImplemented()
