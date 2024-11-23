from tkinter import filedialog

class FileOptions:

  def saveToFile(self, textToSave):
    fileExtentions = [("All Files", "*.*"),
                      ("Text Files", "*.txt")]
    
    file_path = filedialog.asksaveasfilename(filetypes = fileExtentions, defaultextension = fileExtentions)
    if file_path:
      try:
        with open(file_path, "w") as file:
          file.write(textToSave)
          print("saved!")
      except Exception as e:
        print("File did not save properly " + str(e))
  
  def openFile(self):
    textInFile = ""
    file_path = filedialog.askopenfilename()
    print(file_path)
    if file_path:
      try:
        with open(file_path, "r") as file:
          textInFile = file.read()
          print("Opened!")
      except Exception as e:
        print("File did not open correctly\n" + str(e))
    return textInFile