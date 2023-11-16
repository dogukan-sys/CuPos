import pyautogui
import keyboard

position_log = []


def get_mouse_info(color_var):
    position = (pyautogui.position().x, pyautogui.position().y)
    color = pyautogui.pixel(position[0], position[1])
    if color_var:
        position_log.append((position[0], position[1], color))
    else:
        position_log.append((position[0], position[1]))
