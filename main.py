# main.py

import tkinter as tk
from screens.navigation import NavigationManager

def main():
    root = tk.Tk()
    root.title("Task Management System")
    root.geometry("800x600")  # Ukuran layar lebih besar
    nav_manager = NavigationManager(root)
    nav_manager.show_main_screen()
    root.mainloop()

if __name__ == "__main__":
    main()
