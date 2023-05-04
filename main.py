import eel
from mid.mid_simplex import *
import os


eel.init("front")
eel.browsers.set_path("chrome", os.getcwd() + "/chrome-win/chrome.exe")
eel.start("index.html",  size=(1280, 720))
