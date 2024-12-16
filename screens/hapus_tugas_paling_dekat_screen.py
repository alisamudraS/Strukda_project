import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import pytz
from models.min_heap import MinHeap
from utils.supabase import supabase

class HapusTugasPalingDekatScreen(tk.Frame):
    def __init__(self, master, nav_manager):
        super().__init__(master)
        self.nav_manager = nav_manager
        self.heap = MinHeap()
        self.master = master
        self.pack()
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # ScrolledText untuk menampilkan heap sebelum penghapusan
        self.text_before = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10, width=80)
        self.text_before.pack(pady=10)

        # Tombol untuk hapus tugas paling dekat
        self.delete_button = tk.Button(self, text="Hapus Tugas Paling Dekat", command=self.delete_urgent_task)
        self.delete_button.pack(pady=10)

        # Tombol refresh untuk memuat ulang data
        self.refresh_button = tk.Button(self, text="Refresh", command=self.load_tasks)
        self.refresh_button.pack(pady=10)

        # ScrolledText untuk menampilkan heap setelah penghapusan
        self.text_after = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10, width=80)
        self.text_after.pack(pady=10)

        # Kembali ke task screen
        self.kembali_button = tk.Button(self, text="Kembali", command=self.go_back)
        self.kembali_button.pack(pady=10)

    def load_tasks(self):
        self.heap = MinHeap()  # Reset heap
        result = supabase.table('tugas').select('*').execute()
        for task in result.data:
            time_diff = self.calculate_time_diff(task['deadline'])
            self.heap.insert((time_diff, task))
        self.print_heap(self.text_before)  # Tampilkan data baru di widget "sebelum"

    def delete_urgent_task(self):
        if self.heap.heap:
            urgent_task = self.heap.extract_min()[1]
            supabase.table('tugas').delete().eq('id', urgent_task['id']).execute()
            self.print_heap(self.text_after)  # Tampilkan heap yang diperbarui di widget "setelah"

    def print_heap(self, widget):
        widget.delete('1.0', tk.END)  # Bersihkan widget teks
        for item in self.heap.heap:
            widget.insert(tk.END, f"ID: {item[1]['id']}, Nama: {item[1]['nama_tugas']}, Selisih: {item[0]-419} menit\n")

    def calculate_time_diff(self, deadline):
        deadline_dt = datetime.strptime(deadline, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Jakarta'))
        now = datetime.now(pytz.timezone('Asia/Jakarta'))
        time_diff = (deadline_dt - now).total_seconds() / 60
        return int(time_diff)

    def go_back(self):
        self.nav_manager.show_main_screen()
