import pandas as pd
import tkinter as tk
import random as r


# setting up the tk root
root = tk.Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Random Name Generator")

# trying to read the files, if they work it will execute the block of code under else
try:
    df_boy = pd.read_csv('boy_names_2021.csv', usecols=['name'])
    df_girl = pd.read_csv('girl_names_2021.csv', usecols=['name'])
except FileNotFoundError:
    label = tk.Label(
        root, text="Error: One or both of the CSV files could not be found.", font=("Helvetica", 16))
    label.pack(padx=10, pady=10)
else:
    label = tk.Label(root, text="Random Name Generator",
                     font=("Helvetica", 16))
    label.pack(padx=10, pady=10)

    # changes the boys name on the label when triggering the function
    def update_label_boy():
        random_name = df_boy['name'][r.randint(0, len(df_boy['name']) - 1)]
        label2.config(text=random_name)

    # changes the girls name on the label when triggering the function
    def update_label_girl():
        random_name = df_girl['name'][r.randint(0, len(df_girl['name']) - 1)]
        label3.config(text=random_name)

    # buttons to click on to generate the random names
    button = tk.Button(root, text="Generate Random Boy Name",
                       command=update_label_boy)
    button2 = tk.Button(root, text="Generate Random Girl Name",
                        command=update_label_girl)

    # labels for the names and their placements
    label2 = tk.Label(root, text="")
    label2.place(relx=0.5, rely=0.30, anchor="center")
    button.place(relx=0.5, rely=0.40, anchor="center")
    button2.place(relx=0.5, rely=0.80, anchor="center")
    label3 = tk.Label(root, text="")
    label3.place(relx=0.5, rely=0.70, anchor="center")

    # make the gui appear
    root.mainloop()
