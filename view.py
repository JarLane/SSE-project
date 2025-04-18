from model import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from customtkinter import *
from PIL import ImageTk, Image


def ask_if_ready():
    response = messagebox.askyesno(
        title="Ready to Run",
        message="Are you ready to run the server monitoring program?"
    )
    if response:
        app_settings["run"] = "true"
        main_window()
    else:
        app_settings["run"] = "false"
        print("Program not started.")

mainroot = tk.Tk()

status_frame = LabelFrame(
    mainroot,
    text="Status",
    padx=10,
    pady=10
)

status_text = tk.Text(
        status_frame,
        height=4,
        width=60,
        state="disabled",  # Read only to prevent user editing
        wrap=tk.WORD

    )

def main_window():

    mainroot.title("Server Monitoring Dashboard")
    mainroot.geometry("600x340")
    mainroot.resizable(False, False)
    # mainroot.configure(bg = "#d2e6ec")
    # bg_image = Image.open("transparent.png")

    def update_settings():
        app_settings["url"] = url_entry.get()
        app_settings["email"] = email_entry.get()
        app_settings["time_setting"] = time_entry.get()
        messagebox.showinfo("Settings", "Settings updated successfully!")

    settings_frame = LabelFrame(
        mainroot,
        text="Server Settings",
        padx=10,
        pady=10,
    )
    settings_frame.pack(padx=10, pady=10, fill="x")
    # settings_frame.image = bg_image

    Label(
        settings_frame,
        text="Server URL:"
    ).grid(row=0, column=0, sticky="w", pady=5)
    url_entry = Entry(settings_frame, width=60)
    url_entry.insert(0, app_settings["url"])
    url_entry.grid(row=0, column=1, padx=5)

    Label(
        settings_frame,
        text="Notification Email:"
    ).grid(row=1, column=0, sticky="w", pady=5)
    email_entry = Entry(settings_frame, width=60)
    email_entry.insert(0, app_settings["email"])
    email_entry.grid(row=1, column=1, padx=5)

    Label(
        settings_frame,
        text="Check Interval (minutes):"
    ).grid(row=2, column=0, sticky="w", pady=5)
    time_entry = Entry(settings_frame, width=10)
    time_entry.insert(0, app_settings["time_setting"])
    time_entry.grid(row=2, column=1, sticky="w", padx=5)


    # status_frame.image = bg_image
    status_frame.pack(padx=10, pady=10, fill="both", expand=False)

    status_text.pack(pady=5)

    button_frame = Frame(mainroot)
    button_frame.pack(pady=10)

    update_button = Button(
        button_frame,
        text="Update Settings",
        command=lambda: update_settings()
    )
    update_button.pack(side=LEFT, padx=5)

    start_button = Button(
        button_frame,
        text="Start Monitoring",
        command=lambda: check_status()
    )
    start_button.pack(side=LEFT, padx=5)

    stop_button = Button(
        button_frame,
        text="Stop Monitoring",
        command=lambda: app_settings.update({"run": "false"})
    )
    stop_button.pack(side=LEFT, padx=5)

    mainroot.mainloop()




def check_status():
    status_text.config(state="normal")
    status_text.delete(1.0, END)
    try:
        ping()
        check_certificate_expiry(app_settings["url"])
        status_text.insert(
            END,
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Server is up and SSL certificate is valid.\n"
        )
    except Exception as e:
        status_text.insert(
            END,
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: {str(e)}\n"
        )
        email()
    status_text.config(state="disabled")  # Disable editing

    mainroot.after(int(float(app_settings["time_setting"]) * 60 * 1000), check_status)
    #mainroot.mainloop()


if __name__ == "__main__":
    ask_if_ready()
