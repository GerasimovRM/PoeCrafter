import pyautogui

from poe_core.craft.abstract_craft import AbstractCraft
from poe_core.positions import REGEX_LINE_EDIT_POSITION, CRAFT_KOSTIL_POSITION, ACCEPT_CRAFT_COLOR, \
    ALTERATION_ORB_POSITION, CRAFT_POSITION
from poe_core.regex_filter import RegexFilter
from poe_core.tab_type import TabType
from poe_core.window import Window
from poe_core.tab import Tab

class RegexCraft(AbstractCraft):
    def __init__(self, regex_filter: RegexFilter):
        self.regex_filter = regex_filter

    def run_craft(self):
        # regex enter
        Window.mouse_left_click(REGEX_LINE_EDIT_POSITION)
        Window.enter_text_using_keyboard(self.regex_filter)
        # take alteration orb
        Window.mouse_right_click(ALTERATION_ORB_POSITION)
        with pyautogui.hold("shift"):
            Window.move_to_position(CRAFT_POSITION)
            while True:
                Window.mouse_left_click()
                current_screen = Window.get_current_screen_window()
                if current_screen[*CRAFT_KOSTIL_POSITION] == ACCEPT_CRAFT_COLOR:
                    break

    def run(self):

        Window.mouse_left_click(REGEX_LINE_EDIT_POSITION)
        Window.enter_text_using_keyboard(self.regex_filter)

        for line in Tab.load_cells(TabType.INVENTORY):
            for cells in line:
                Window.move_from__to__(cells, CRAFT_POSITION)
                Window.mouse_right_click(ALTERATION_ORB_POSITION)
                with pyautogui.hold("shift"):
                    Window.move_to_position(CRAFT_POSITION)
                    while True:
                        Window.mouse_left_click()
                        current_screen = Window.get_current_screen_window()
                        if current_screen[*CRAFT_KOSTIL_POSITION] == ACCEPT_CRAFT_COLOR:
                            break
                Window.move_from__to__(CRAFT_POSITION, cells)
