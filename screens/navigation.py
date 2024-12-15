# screens/navigation.py

import tkinter as tk
from screens.main_screen import MainScreen
from screens.lihat_semua_tugas_screen import LihatSemuaTugasScreen
from screens.tambah_tugas_screen import TambahTugasScreen
from screens.edit_tugas_screen import EditTugasScreen
from screens.hapus_tugas_paling_dekat_screen import HapusTugasPalingDekatScreen

class NavigationManager:
    def __init__(self, master):
        self.master = master  # Tkinter root
        self.frame = None
        self.show_main_screen()

    def show_main_screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = MainScreen(self.master, self)
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_lihat_semua_tugas_screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = LihatSemuaTugasScreen(self.master, self)  # Pass nav_manager ke LihatSemuaTugasScreen
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_tambah_tugas_screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = TambahTugasScreen(self.master, self)  # Pass nav_manager ke TambahTugasScreen
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_edit_tugas_screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = EditTugasScreen(self.master, self)  # Pass nav_manager ke EditTugasScreen
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_hapus_tugas_paling_dekat_screen(self):
        if self.frame:
            self.frame.destroy()
        self.frame = HapusTugasPalingDekatScreen(self.master, self)  # Pass nav_manager ke HapusTugasPalingDekatScreen
        self.frame.grid(row=0, column=0, sticky="nsew")
