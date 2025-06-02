import User_inputs
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style


def program_starter():
    global entry_acquisition, entry_face_val, entry_inst, entry_nom

    root = tk.Tk()
    root.title("Ronzki")
    Style('darkly')

    root.photo_icon = ttk.PhotoImage(file='bochi.png')
    root.iconphoto(True, root.photo_icon)

    mainframe = ttk.Frame(root, padding=20)
    mainframe.pack(expand=True, fill='both')

    label = ttk.Label(mainframe, text='Yield Calculator App', font=('Gotham', 20, 'bold'))
    label.pack(anchor='center', pady=10)

    entry_frame = ttk.Labelframe(mainframe, text="Input Fields", padding=10)
    entry_frame.pack(fill='x', pady=10)

    entry_acquisition = ttk.Entry(entry_frame, textvariable=StringVar(), bootstyle='info')
    entry_acquisition.pack(fill='x', padx=5, pady=5)
    create_tooltip(entry_acquisition, "Acquisition cost (e.g., 1000)")

    entry_face_val = ttk.Entry(entry_frame, textvariable=StringVar(), bootstyle='info')
    entry_face_val.pack(fill='x', padx=5, pady=5)
    create_tooltip(entry_face_val, "Face value of the bond (e.g., 1200)")

    entry_inst = ttk.Entry(entry_frame, textvariable=StringVar(), bootstyle='info')
    entry_inst.pack(fill='x', padx=5, pady=5)
    create_tooltip(entry_inst, "Installment amount (e.g., 200)")

    entry_nom = ttk.Entry(entry_frame, textvariable=StringVar(), bootstyle='info')
    entry_nom.pack(fill='x', padx=5, pady=5)
    create_tooltip(entry_nom, "Nominal rate (%) (e.g., 5)")

    button_frame = ttk.Frame(mainframe)
    button_frame.pack(fill='x', pady=10)

    submit_button = ttk.Button(button_frame, text='Submit', bootstyle='success', command=store_inputs)
    submit_button.pack(side='left', expand=True, fill='x', padx=5)

    delete_button = ttk.Button(button_frame, text='Delete', bootstyle='danger', command=delete_inputs)
    delete_button.pack(side='right', expand=True, fill='x', padx=5)

    root.mainloop()


def store_inputs():
    try:
        acq = float(entry_acquisition.get().replace(',', ''))
        face = float(entry_face_val.get().replace(',', ''))
        inst = float(entry_inst.get().replace(',', ''))
        nom = float(entry_nom.get().replace(',', ''))

        stored_inputs = {
            'acq_cost': acq,
            'face_val': face,
            'inst_amt': inst,
            'nom_rate': nom / 100
        }

        if inst == 0:
            raise ValueError("Installment amount cannot be zero.")

        User_inputs.inputs_main(stored_inputs)

    except ValueError:
        messagebox.showinfo(
            title="Invalid input",
            message="Make sure all fields are filled with valid numbers."
        )


def delete_inputs():
    entry_acquisition.delete(0, END)
    entry_face_val.delete(0, END)
    entry_inst.delete(0, END)
    entry_nom.delete(0, END)



def create_tooltip(widget, text):
    tooltip = None

    def show_tooltip(event):
        nonlocal tooltip
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{widget.winfo_rootx() + 20}+{widget.winfo_rooty() + 20}")
        label = tk.Label(
            tooltip,
            text=text,
            background="#333",
            foreground="white",
            relief="solid",
            borderwidth=1,
            font=("Arial", 8),
            padx=5,
            pady=2,
        )
        label.pack()

    def hide_tooltip(event):
        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)
