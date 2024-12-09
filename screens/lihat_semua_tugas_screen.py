import tkinter as tk
from tkinter import ttk
from datetime import datetime
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_API_KEY

class LihatSemuaTugasScreen(tk.Frame):
    def __init__(self, master, nav_manager):
        super().__init__(master)
        self.master = master
        self.nav_manager = nav_manager
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Nama Tugas", "Deskripsi", "Deadline", "Waktu Selisih"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama Tugas", text="Nama Tugas")
        self.tree.heading("Deskripsi", text="Deskripsi")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Waktu Selisih", text="Waktu Selisih (Menit)")

        self.tree.pack(fill="both", expand=True)

        self.load_data()

        # Kembali ke task screen
        self.kembali_button = tk.Button(self, text="Kembali", command=self.go_back)
        self.kembali_button.pack()

    def go_back(self):
        self.nav_manager.show_task_screen()

    def load_data(self):
        supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
        result = supabase.table("tugas").select("*").execute()

        for task in result.data:
            time_diff = self.calculate_time_diff(task['deadline'])
            self.tree.insert("", "end", values=(task['id'], task['nama_tugas'], task['deskripsi_tugas'], task['deadline'], time_diff))

    def calculate_time_diff(self, deadline):
        deadline_dt = datetime.strptime(deadline, '%Y-%m-%dT%H:%M:%S')
        now = datetime.now()
        time_diff = (deadline_dt - now).total_seconds() / 60
        return round(time_diff)
