import tkinter as tk
from tkinter import ttk
from ui_module import UInterface


class BasicUI(UInterface):
  
  window = None
  textField = None
  mainFrame = None
  lines = None
  lineCounter = None

  def setWindowSize(self, width, height):
    windowSize = str(width) + "x" + str(height)
    self.window = tk.Tk()
    self.window.title("Text Editor")
    self.window.geometry(windowSize)
  
  def setTextField(self, fileFunctions):
    self.mainFrame = ttk.Frame(master = self.window)
    self.mainFrame.columnconfigure(0, weight = 1)
    self.mainFrame.columnconfigure(1, weight = 1)
    self.mainFrame.rowconfigure(0, weight = 1)
    self.textField = tk.Text(master = self.mainFrame, background = "gray", font=("Arial", 8)) #width = width,height= height
    self.textField.config(spacing1=1.5)
    self.textField.config(spacing3=1.5)
    self.textField.grid(row=0, column=1,sticky="nswe")
    self.mainFrame.pack(expand=True, fill="both")
    self.textField.bind("<Control-KeyPress-s>", lambda event: fileFunctions.saveToFile(self.textField.get("1.0", "end-1c")))
    self.textField.bind("<Return>", lambda event: self.pressed_enter())
    self.textField.bind("<KeyRelease-BackSpace>", lambda event: self.released_back())
    self.textField.bind("<Control-KeyPress-z>", lambda event : self.DebugLineCounter())

  def setLineCounter(self):
    lineFrame = ttk.Frame(master = self.mainFrame)
    lineFrame.grid(row = 0, column = 0, sticky="nswe")
    lineFrame.columnconfigure(0, weight = 1)
    self.lineCounter = tk.IntVar(value = 1)
    lineNumbers = ttk.Label(master = lineFrame, background= "green", text = "1", font=("Arial", 8))
    lineNumbers.grid(row=0,column=0, sticky="nswe")

  def setMenu(self, fileFunctions):
    menu = tk.Menu(self.window)
    fileMenu = tk.Menu(menu, tearoff = False)
    fileMenu.add_command(label = "Open File", command = lambda : self.pasteFileToField(fileFunctions))
    fileMenu.add_command(label = "Save", command = lambda : fileFunctions.saveToFile(self.textField.get("1.0", "end-1c")))
    fileMenu.add_command(label = "New Window")
    menu.add_cascade(label="File", menu = fileMenu)
    self.window.configure(menu= menu)

  def pasteFileToField(self, fileFunctions):
    newText = fileFunctions.openFile()
    self.textField.insert(1.0, newText)
    self.printLineCount()

  # Event for pressing "Enter" in the text field
  def pressed_enter(self):
    # printLineCount()
    count = int(self.textField.index("end-1c").split(".")[0])
    # print("Line count : " + str(count))
    self.lineCounter.set(count+1)
    line = ttk.Label(self.mainFrame.winfo_children()[1], background= "green", text = str(count+1), font=("Arial", 8))
    line.grid(row = count, column = 0, sticky="nswe")

  def released_back(self):
    self.printLineCount()

  def DebugLineCounter(self):
    counter = int(self.textField.index("end-1c").split(".")[0])
    print(f"Current count: {self.lineCounter.get()}\nText field count: {counter}")

  def printLineCount(self):
    count = int(self.textField.index("end-1c").split(".")[0])
    currentLineCount = self.lineCounter.get()
    if(count != currentLineCount):
      if(count > currentLineCount):
        self.DebugLineCounter()
        for i in range(currentLineCount, count):
          line = ttk.Label(self.mainFrame.winfo_children()[1], background= "green", text = str(i+1), font=("Arial", 8))
          line.grid(row = i, column = 0, sticky="nswe")
        self.lineCounter.set(count)
        self.DebugLineCounter()
      else:
        for i in range(count, currentLineCount):
          line = self.mainFrame.winfo_children()[1].grid_slaves(row = i, column = 0)[0]
          line.grid_remove()
        self.lineCounter.set(count)

  def start(self):
    self.window.mainloop()