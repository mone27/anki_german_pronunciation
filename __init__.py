# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def addGermanPronunciation() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
    # show a message box
    showInfo("added pronunciation successfully")

# create a new menu item, "test"
action = QAction("add german pronunciation", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, addGermanPronunciation)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
