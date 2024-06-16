import random
from datetime import datetime
from typing import Optional, Tuple

import PIL.Image
import pyautogui


class Window:
    @staticmethod
    def get_current_screen_window() -> PIL.Image.Image:
        im = pyautogui.screenshot()
        return im.load()

    @staticmethod
    def get_current_screen_window_to_file(filename: Optional[str] = None):
        if filename is None:
            now = datetime.now()
            filename = now.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
        pyautogui.screenshot(f"data/{filename}.jpg")

    @staticmethod
    def mouse_left_click(position: Optional[Tuple[int, int]] = None,
                         move_duration_value: float = 0.5,
                         move_duration_dispersion: float = 0.1) -> None:  # TODO: пока костыльненько
        if position is not None:
            Window.move_to_position(position, move_duration_value, move_duration_dispersion)
        pyautogui.click()

    @staticmethod
    def mouse_right_click(position: Optional[Tuple[int, int]] = None,
                          move_duration_value: float = 0.5,
                          move_duration_dispersion: float = 0.1) -> None:  # TODO: пока костыльненько
        if position is not None:
            Window.move_to_position(position, move_duration_value, move_duration_dispersion)
        pyautogui.rightClick()

    @staticmethod
    def move_to_position(position: Optional[Tuple[int, int]] = None,
                         move_duration_value: float = 0.5,
                         move_duration_dispersion: float = 0.1):
        pyautogui.moveTo(position,
                         duration=move_duration_value + random.uniform(-move_duration_dispersion,
                                                                       move_duration_dispersion))

    @staticmethod
    def enter_text_using_keyboard(text: str, interval: float = 0.15, dispersion: float = 0.1):
        pyautogui.write(text, interval + random.uniform(-dispersion, dispersion))
