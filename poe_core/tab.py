from poe_core.tab_type import TabType


class Tab:
    def __init__(self, tab_type: TabType):
        self.type = tab_type
        self.cells = Tab.load_cells(tab_type)

    @staticmethod
    def load_cells(tab_type: TabType):
        if tab_type == TabType.INVENTORY:
            ...
        else:
            raise TypeError("Unrecognized tab type")
