import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
  title = "Select a text file",
  filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
)

if file_path:
  print(f"Selected file: {file_path}")
else:
  print(f"No file selected.")
