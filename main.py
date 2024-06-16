import time

from poe_core.craft.regex_craft import RegexCraft
from poe_core.regex_filter import RegexFilter
from poe_core.window import Window

time.sleep(2)
# Window.get_current_screen_window_to_file()

regexCraft = RegexCraft("\"mana\"")
regexCraft.run_craft()
