# screens/main_screen.py

import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, master, nav_manager):
        super().__init__(master)
        self.master = master
        self.nav_manager = nav_manager  # Simpan nav_manager untuk akses navigasi
        self.create_widgets()

    def create_widgets(self):
        start_button = tk.Button(self, text="Mulai", command=self.nav_manager.show_task_screen)
        start_button.grid(row=0, column=0)
