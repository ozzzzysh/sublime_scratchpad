from sublime_plugin import WindowCommand, TextCommand
from sublime import packages_path, run_command, ENCODED_POSITION, set_timeout
from time import strftime
from os.path import isfile
import os

headerText = """
    _____                _       _                     _
   /  ___|              | |     | |                   | |
   \ `--.  ___ _ __ __ _| |_ ___| |__  _ __   __ _  __| |
    `--. \/ __| '__/ _` | __/ __| '_ \| '_ \ / _` |/ _` |
   /\__/ / (__| | | (_| | || (__| | | | |_) | (_| | (_| |
   \____/ \___|_|  \__,_|\__\___|_| |_| .__/ \__,_|\__,_|
                                      | |                
                                      |_|                

"""

class OpenScratchpadCommand(WindowCommand):
  def run(self):
    scratchpadFile = packages_path()[:-8]+'scratchpad.txt'
    checkAndFillEmpty(scratchpadFile)
    self.window.open_file(scratchpadFile)
    # self.window.open_file(scratchpadFile+':'+str(sum(1 for line in scratchpadFile)), ENCODED_POSITION)
    # def preview():
    #   self.window.run_command("open_markdown_preview")
    # set_timeout(preview, 100)
    print(os.linesep)
    def foldAll():
      self.window.run_command("fold_all_sections", {"target_level": 1})
    set_timeout(foldAll, 100)

class ScratchpadCommand(WindowCommand):
  def run(self):
    scratchpadFile = packages_path()[:-8]+'scratchpad.txt'
    global headerText
    checkAndFillEmpty(scratchpadFile)
    count = putTimeStamp(scratchpadFile)
    self.window.open_file(scratchpadFile+':'+str(count+1), ENCODED_POSITION)
    # def preview():
    #   self.window.run_command("open_markdown_preview")
    # set_timeout(preview, 100)
    def foldAll():
      self.window.run_command("fold_all_sections", {"target_level": 1})
      self.window.run_command("go_to_line", {"line":0})
    set_timeout(foldAll, 100)

def checkAndFillEmpty(scratchpadFile):
  global headerText
  if not isfile(scratchpadFile):
    with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(headerText)

def putTimeStamp(scratchpadFile):
  timeStamp = "\n\n" + strftime("%x") + "\n" +"========================" + "\n"
  with open(scratchpadFile, "a") as scratchFile:
      scratchFile.write(timeStamp)
  with open(scratchpadFile) as scratchFile:
    count = sum(1 for line in scratchFile)
  return count
