#!/usr/bin/python
from Foundation import NSAppleScript, objc

def sendTextClipBoard(string):
    from AppKit import NSPasteboard, NSObject, NSStringPboardType
    pasteboard = NSPasteboard.generalPasteboard()
    emptyOwner = NSObject.alloc().init()
    pasteboard.declareTypes_owner_([NSStringPboardType], emptyOwner)
    pasteboard.setString_forType_(string, NSStringPboardType)

def getSelection():
    sendTextClipBoard(" ")
    script='''
        tell application "System Events"
            keystroke "c" using command down
        end tell
        set theText to (the clipboard as text)
        return theText'''

    appleScript = NSAppleScript.alloc().initWithSource_(script)
    result = appleScript.executeAndReturnError_(objc.nil)
    return result[0].stringValue()

def generateMethodStubs(selected_text):
    selected_stubs = selected_text.replace(";", "\n{\n}\n")
    while selected_stubs.endswith('\n'): selected_stubs = selected_stubs[:-1]
    return selected_stubs

if __name__ == "__main__":
    selected_text = getSelection()
    stubs_text = generateMethodStubs(selected_text)
    sendTextClipBoard(stubs_text)