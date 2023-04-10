import tkinter as tk
import random
import time
from pack import rg
import os
random_list = [0,0]
time_stamp_list = [0,0]
option_list = [0,0]
class RandomNumberGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Random Number Generator")
        master.attributes('-fullscreen', True)
        master.configure(bg='black')
        self.master.bind("<Escape>", self.quit_fullscreen)

        # Create header
        header = tk.Label(master, text="Random Number Generator", fg="white", bg="black", font=("Helvetica", 24))
        header.pack(pady=20)

        # Create drop down menu
        options = ["Camera", "Key", "Sound"]
        self.system_label = tk.Label(self.master, text="Select System To Be Used:", font=("Helvetica", 20), fg='white', bg='black')
        self.system_label.pack(pady=10)
        self.selected_option = tk.StringVar(master)
        self.selected_option.set(options[0])
        dropdown = tk.OptionMenu(master, self.selected_option, *options)
        dropdown.config(bg="gray", fg="white", font=("Helvetica", 16))
        dropdown.pack(pady=10)

        # Create generate button
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_random_number, bg="gray", fg="white", font=("Helvetica", 16), state="disabled")
        self.generate_button.pack(pady=10)

        # Create random number display
        self.random_number_label = tk.Label(master, text="Random number: ", font=("Helvetica", 16), fg="white", bg="black")
        self.random_number_label.pack(pady=10)

        # Create turn on/off button
        self.on_off_button = tk.Button(master, text="Turn On", command=self.toggle_button_state, bg="gray", fg="white", font=("Helvetica", 16))
        self.on_off_button.pack(pady=10)

        # Create previous info widget
        previous_info = tk.LabelFrame(master, text="Previous Info", fg="white", bg="black", font=("Helvetica", 16), pady=10)
        previous_info.pack(pady=10, padx=20, fill="both", expand="yes")

        self.previous_number_label = tk.Label(previous_info, text="Previous number: ", font=("Helvetica", 16), fg="white", bg="black")
        self.previous_number_label.pack(pady=5)

        self.system_used_label = tk.Label(previous_info, text="System used: ", font=("Helvetica", 16), fg="white", bg="black")
        self.system_used_label.pack(pady=5)

        self.timestamp_label = tk.Label(previous_info, text="Timestamp: ", font=("Helvetica", 16), fg="white", bg="black")
        self.timestamp_label.pack(pady=5)

        

    def toggle_button_state(self):
        if self.on_off_button["text"] == "Turn On":
            self.on_off_button["text"] = "Turn Off"
            self.generate_button["state"] = "normal"
        else:
            self.on_off_button["text"] = "Turn On"
            self.generate_button["state"] = "disabled"

    def generate_random_number(self):
        option = self.selected_option.get()
        option_list[0]=option_list[1]
        option_list[1]=option
        if option == "Sound" :
            number = rg.random_gen()
        if option == "Camera":
            number= rg.random_gen_cam()
        random_list[0]=random_list[1]
        random_list[1]= number
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        time_stamp_list[0]=time_stamp_list[1]
        time_stamp_list[1]=timestamp
        self.random_number_label["text"]= f"Random number: {random_list[1]}"
        self.previous_number_label["text"] = f"Previous number: {random_list[0]}"
        self.system_used_label["text"] = f"System used: {option_list[0]}"
        self.timestamp_label["text"] = f"Timestamp: {time_stamp_list[0]}"
    
    def quit_fullscreen(self, event=None):
        self.master.attributes("-fullscreen", False)

root = tk.Tk()
app = RandomNumberGenerator(root)
root.mainloop()
