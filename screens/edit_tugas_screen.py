import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from utils.supabase import supabase 
from datetime import datetime, time

class EditTugasScreen(tk.Frame):
    def __init__(self, master, nav_manager):
        super().__init__(master)
        self.master = master
        self.nav_manager = nav_manager
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.id_label = tk.Label(self, text="ID Tugas")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        self.nama_label = tk.Label(self, text="Nama Tugas")
        self.nama_label.pack()
        self.nama_entry = tk.Entry(self)
        self.nama_entry.pack()

        self.deskripsi_label = tk.Label(self, text="Deskripsi Tugas")
        self.deskripsi_label.pack()
        self.deskripsi_entry = tk.Entry(self)
        self.deskripsi_entry.pack()

        self.deadline_label = tk.Label(self, text="Deadline")
        self.deadline_label.pack()
        # Menggunakan DateEntry untuk memilih tanggal
        self.deadline_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.deadline_entry.pack()

        # Time Picker menggunakan Combobox untuk jam dan menit
        self.time_frame = tk.Frame(self)
        self.hour_cb = ttk.Combobox(self.time_frame, values=[f"{i:02}" for i in range(24)], width=3)
        self.minute_cb = ttk.Combobox(self.time_frame, values=[f"{i:02}" for i in range(60)], width=3)
        self.hour_cb.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.minute_cb.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.time_frame.pack()

        self.update_button = tk.Button(self, text="Update Tugas", command=self.update_task)
        self.update_button.pack()

        self.kembali_button = tk.Button(self, text="Kembali", command=self.go_back)
        self.kembali_button.pack()

    def go_back(self):
        self.nav_manager.show_main_screen()


    def update_task(self):
        tugas_id = self.id_entry.get()
        nama = self.nama_entry.get()
        deskripsi = self.deskripsi_entry.get()
        deadline_date = self.deadline_entry.get_date().isoformat()
        deadline_hour = self.hour_cb.get()
        deadline_minute = self.minute_cb.get()


        if not tugas_id or not nama or not deskripsi or not deadline_date or not deadline_hour or not deadline_minute:
            messagebox.showerror("Error", "Semua kolom harus diisi.")
            return
            

        current_time = datetime.now()

        given_date = datetime.strptime(deadline_date, "%Y-%m-%d")
        given_time = time(int(deadline_hour), int(deadline_minute))

        
        if given_date.date() < current_time.date():
            messagebox.showerror("Error", "Tanggal yang diberikan sudah lewat")
            return

        if given_time <= current_time.time():
            messagebox.showerror("Error", "Jam dan menit yang diberikan sudah lewat")
            return

        
        deadline_time = f"{deadline_hour}:{deadline_minute}:00"
        deadline = f"{deadline_date}T{deadline_time}"


        tugas = supabase.table('tugas').select('*').eq('id', tugas_id).execute().data

        if len(tugas) == 0:
            messagebox.showerror("Error", "Tugas dengan ID tersebut tidak ditemukan.")
            return

        supabase.table('tugas').update({
            'nama_tugas': nama,
            'deskripsi_tugas': deskripsi,
            'deadline': deadline
        }).eq('id', tugas_id).execute()

        messagebox.showinfo("Berhasil", "Tugas berhasil diperbarui.")
        self.nav_manager.show_main_screen()
