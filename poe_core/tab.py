from poe_core.tab_type import TabType


class Tab:
    def __init__(self, tab_type: TabType):
        self.type = tab_type
        self.cells = Tab.load_cells(tab_type)

    @staticmethod
    def load_cells(tab_type: TabType):
        if tab_type == TabType.INVENTORY:
            return [[(1730 + x * 70, 820 + y * 70) for x in range(12)] for y in range(5)]
        else:
            raise TypeError("Unrecognized tab type")
