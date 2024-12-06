from function_module import FileOptions
from ui_version_one import BasicUI


class Main():
  functions = FileOptions()
  currentUI = BasicUI()
  currentUI.setWindowSize(800, 600)
  currentUI.setTextField(functions, "light cyan")
  currentUI.setLineCounter("yellow")
  currentUI.setMenu(functions)
  currentUI.start()
  