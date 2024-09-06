import tkinter as tk
from tkinter import messagebox

def show_login_window():
    login_window = tk.Toplevel()
    login_window.title("Inicio de Sesión")
    login_window.geometry("300x200")
    login_window.configure(bg="#faffff")
    
    tk.Label(login_window, text="Nombre de usuario", bg="#faffff").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)
    
    tk.Label(login_window, text="Contraseña", bg="#faffff").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)
    
    def login():
        username = username_entry.get()
        password = password_entry.get()
        # Aquí puedes verificar las credenciales con una base de datos o un conjunto de datos
        if username == "admin" and password == "admin":
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            login_window.destroy()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")
    
    tk.Button(login_window, text="Iniciar sesión", command=login, bg="#e1f5f5", fg="black").pack(pady=10)

def menu():
    root = tk.Tk()
    root.title("Menú de opciones")
    root.geometry("600x400")
    root.configure(bg="#faffff")
    
    main_frame = tk.Frame(root, padx=10, pady=10, bg="#faffff")
    main_frame.pack(expand=True, fill='both')
    
    label_font = ("Trajan Pro", 14)
    button_font = ("Trajan Pro", 12)
    button_bg = "#ffffff"
    button_fg = "black"
    
    tk.Label(main_frame, text="Registro, por favor iniciar sesión", bg="#ffffff", fg="black", font=label_font).pack(pady=10)
    
    button_frame = tk.Frame(main_frame, bg="black")
    button_frame.pack(pady=10)
    
    button_style = {"bg": button_bg, "fg": button_fg, "font": button_font, "width": 25, "relief": "raised"}
    
    tk.Button(button_frame, text="Iniciar sesión", command=show_login_window, **button_style).pack(padx=10, pady=8)
    tk.Button(button_frame, text="Salir", command=root.destroy, **button_style).pack(padx=10, pady=8)
    
    root.mainloop()

menu()