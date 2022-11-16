import requests
import json
import tkinter as tk


def getQuets():
  response = requests.get(url="https://opentdb.com/api.php?amount=10")
  data = response.json()
  print(data)

  for x in data["results"]:
    print(x["category"])
    Label = tk.Label(text=x["category"])
    Label.grid(columns=2, row=1)

  #T = tk.Text(window, height=2, width=30)
  #T.pack()
  #T.insert(data)

  ##for x in data:
  #print(f"das ist :{x}")


#####ui-setup#####

window = tk.Tk()

button = tk.Button(text="Click me!",
                   width=25,
                   height=2,
                   bg="blue",
                   fg="yellow",
                   command=getQuets)

####ui-grid-style###
window.geometry("400x200")
button.grid(columns=1, row=3)

window.mainloop()
