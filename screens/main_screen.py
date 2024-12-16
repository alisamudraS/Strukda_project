# screens/main_screen.py

from datetime import datetime
import tkinter as tk
from utils.supabase import supabase

class MainScreen(tk.Frame):
    def __init__(self, master, nav_manager):
        super().__init__(master)
        self.master = master
        self.nav_manager = nav_manager  # Simpan nav_manager untuk akses navigasi
        self.create_widgets()
        self.delete_missed_task()

    def create_widgets(self):
    # Menambahkan tombol untuk menampilkan semua tugas
        lihat_tugas_button = tk.Button(self, text="Lihat Semua Tugas", command=self.nav_manager.show_lihat_semua_tugas_screen)
        lihat_tugas_button.grid(row=0, column=0)

        # Tombol lainnya
        tambah_tugas_button = tk.Button(self, text="Tambah Tugas", command=self.nav_manager.show_tambah_tugas_screen)
        tambah_tugas_button.grid(row=1, column=0)

        edit_tugas_button = tk.Button(self, text="Edit Tugas", command=self.nav_manager.show_edit_tugas_screen)
        edit_tugas_button.grid(row=2, column=0)

        hapus_tugas_button = tk.Button(self, text="Hapus Tugas Paling Dekat", command=self.nav_manager.show_hapus_tugas_paling_dekat_screen)
        hapus_tugas_button.grid(row=3, column=0)

    def delete_missed_task(self):
        current_time = datetime.now().isoformat()
        
        try:
        
            response = supabase.table("tugas").delete().lt("deadline", current_time).execute()

            if response.error:
                print(f"Terjadi Kesalahan saat menghapus tugas yang terlewat, error : {response.error}")
                

        except Exception as e:
                if "APIResponse[TypeVar]" in str(e):
                     return

                print(f"Terjadi Kesalahan saat menghapus tugas yang terlewat, error : {e}")



