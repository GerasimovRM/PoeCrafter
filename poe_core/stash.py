from typing import List

from poe_core.stash_type import StashType
from poe_core.tab import Tab


class Stash:
    def __init__(self, stash_type: StashType):
        self.type = stash_type
        self.tabs = Stash.load_stash(self.type)

    @staticmethod
    def load_stash(stash_type: StashType) -> List[Tab]:
        if stash_type == StashType.DEFAULT_STASH:
            ...  # TODO
        elif stash_type == StashType.GUILD_STASH:
            ...  # TODO
        elif stash_type == StashType.PLAYER_INVENTORY:
            ...  # TODO
        else:
            raise TypeError("Unrecognized stash type")
