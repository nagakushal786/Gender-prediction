import tkinter as tk
from tkinter import ttk

names=['satya', 'bala', 'chandu', 'madhu', 'vishnu']
def predict_gender(name):
  name=name.lower()
  if name in names:
    return 'Unknown - Need full name'
  elif name[-1]=='a' or name[-1]=='i':
    return 'Female'
  else:
    return 'Male'
  
def main():
  root=tk.Tk()
  root.title("Gender Predictor")
  root.geometry("400x200")

  # Defining labels and input field for user inputs
  name_label=ttk.Label(root, text="Enter your name: ")
  name_label.grid(row=0, column=0, padx=5, pady=5)
  name_entry=ttk.Entry(root, width=25)
  name_entry.grid(row=0, column=1, padx=5, pady=5)

  result_label=ttk.Label(root, text="Your Gender is: ")
  result_label.grid(row=1, column=0, padx=5, pady=5)
  result_entry=ttk.Entry(root, state="readonly", width=25)
  result_entry.grid(row=1, column=1, padx=5, pady=5)

  # Function that will handle the prediction
  def predict():
    name=name_entry.get()
    gender=predict_gender(name)
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, gender)
    result_entry.config(state="readonly")

  predict_button=ttk.Button(root, text="Predict", command=predict)
  predict_button.grid(row=2, column=0, padx=5, pady=5)

  root.mainloop()

if __name__=="__main__":
  main()
