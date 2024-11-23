# import tkinter as tk
# from tkinter import ttk
# from function_module import FileOptions


# # Default settings
# height = 900
# width = 800
# windowSize = str(width) + "x" + str(height)


# # window
# window = tk.Tk()
# window.title("Text Editor")
# window.geometry(windowSize)


# # Menu bar
# menu = tk.Menu(window)
# fileMenu = tk.Menu(menu, tearoff = False)
# fileMenu.add_command(label = "Open File", command = lambda : pasteFileToField())
# fileMenu.add_command(label = "Save", command = lambda : FileOptions.saveToFile(field.get("1.0", "end-1c")))
# fileMenu.add_command(label = "New Window")
# menu.add_cascade(label="File", menu = fileMenu)



# # Events

# def pasteFileToField():
#   newText = FileOptions.openFile()
#   field.insert(1.0, newText)
#   printLineCount()


# def printLineCount():
#   count = int(field.index("end-1c").split(".")[0])
#   currentLineCount = lineNumberCount.get()
#   if(count != currentLineCount):
#     if(count > currentLineCount):
#       DebugLineCounter()
#       for i in range(currentLineCount, count):
#         line = ttk.Label(lineFrame, background= "green", text = str(i+1), font=("Arial", 8))
#         line.grid(row = i, column = 0, sticky="nswe")
#       lineNumberCount.set(count)
#       DebugLineCounter()
#     else:
#       for i in range(count, currentLineCount):
#         line = lineFrame.grid_slaves(row = i, column = 0)[0]
#         line.grid_remove()
#       lineNumberCount.set(count)

# def DebugLineCounter():
#   counter = int(field.index("end-1c").split(".")[0])
#   print(f"Current count: {lineNumberCount.get()}\nText field count: {counter}")


# # Event for pressing "Enter" in the text field
# def pressed_enter():
#   # printLineCount()
#   count = int(field.index("end-1c").split(".")[0])
#   # print("Line count : " + str(count))
#   lineNumberCount.set(count+1)
#   line = ttk.Label(lineFrame, background= "green", text = str(count+1), font=("Arial", 8))
#   line.grid(row = count, column = 0, sticky="nswe")

# # Event for releasing  "Backspace" in the text field
# def released_back():
#   printLineCount()
#   # currentLineCount = lineNumberCount.get()
#   # count = int(field.index("end-1c").split(".")[0])
#   # # print("Line count : " + str(count))
#   # if(count == currentLineCount):
#   #   return
#   # lineNumberCount.set(count)
#   # line = lineFrame.grid_slaves(row = count, column = 0)[0]
#   # line.grid_remove()



# # Field
# inputFrame = ttk.Frame(master = window)
# inputFrame.columnconfigure(0, weight = 1)
# inputFrame.columnconfigure(1, weight = 1)
# inputFrame.rowconfigure(0, weight = 1)
# field = tk.Text(master = inputFrame, background = "gray", font=("Arial", 8)) #width = width,height= height
# field.config(spacing1=1.5)
# field.config(spacing3=1.5)
# field.grid(row=0, column=1,sticky="nswe")
# inputFrame.pack(expand=True, fill="both")


# #LineCounter
# lineFrame = ttk.Frame(master = inputFrame)
# lineFrame.grid(row = 0, column = 0, sticky="nswe")
# lineFrame.columnconfigure(0, weight = 1)
# lineNumberCount = tk.IntVar(value = 1)
# lineNumbers = ttk.Label(master = lineFrame, background= "green", text = "1", font=("Arial", 8))
# lineNumbers.grid(row=0,column=0, sticky="nswe")


# # Event Binding
# field.bind("<Control-KeyPress-s>", lambda event: FileOptions.saveToFile(field.get("1.0", "end-1c")))
# field.bind("<Return>", lambda event: pressed_enter())
# field.bind("<KeyRelease-BackSpace>", lambda event: released_back())
# field.bind("<Control-KeyPress-z>", lambda event : DebugLineCounter())

# #run
# window.configure(menu = menu)
# window.mainloop()
