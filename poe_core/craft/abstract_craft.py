from abc import abstractmethod


class AbstractCraft:
    @abstractmethod
    def run_craft(self, *args, **kwargs):
        ...
