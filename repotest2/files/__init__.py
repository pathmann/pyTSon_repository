from ts3plugin import ts3plugin

import ts3lib, ts3defines

class repotest2(ts3plugin):
    name = "repotest2"
    requestAutoload = False
    version = "1.0.1"
    apiVersion = 21
    author = "Thomas \"PLuS\" Pathmann"
    description = "Just testing"
    offersConfigure = False
    commandKeyword = ""
    infoTitle = None
    menuItems = []
    hotkeys = []

    def __init__(self):
        pass
