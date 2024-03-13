# External modules

'''
External modules are mode by other programmers and give a huge amount of
extra functionality.

For example, game development, data analysis, machine learning, GUIs, etc.
are all functionalities obtainable from external modules.

These modules are imported the same way standard modules are. However,
they need to be installed first (usually via a terminal)

Windows uses `pip`
MacOS and Linux uses `pip3` because `pip` will use an old version

For this file, in a terminal (Linux or Mac), use the following command to install pyautogui:
pip3 install pyautogui

For Windows, use:
pip install pyautogui
'''

# Import `pyautogui` module and `sleep` function from `time` module
import pyautogui
from time import sleep # Standard Python library - this pauses code for a time interval

sleep(3) # Sleep for 2 seconds

# Write text to a wherever the user's cursor is (if possible)
# Add text and (optional) interval to the writer
pyautogui.write('This is written by a computer', 0.25)

# Research and try other modules!
