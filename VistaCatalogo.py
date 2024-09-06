import tkinter as tk
from tkinter import ttk


catalog_items = [
    {"nombre": "Garrafa de avena pequeña", "descripcion": "garrafa de 2lt con una capacidad para 9 vasos de 7onz aprox", "precio": "$9.000"},
    {"nombre": "Garrafa de avena de grande", "descripcion": "Garrafa de 4Lt con una capacidad para 21 vasos de 7onz aprox", "precio": "$15.000"},
    {"nombre": "tarritos de avena personales", "descripcion": "Tarrito de 500Ml en presentacion personal", "precio": "$1.500"},
    {"nombre": "Garrafa de mazato pequeña", "descripcion": "Garrafa de 2Lt con una capacidad para 9 y 1/2 vasos de 7onz aprox", "precio": "$7.000"},
    {"nombre": "Garrafa de mazato grande", "descripcion": "Garrafa de 4Lt con una capacidad para 21 vasos de 7onz aprox", "precio": "$14.000"}
]

def create_catalog_window():
    root = tk.Tk()
    root.title("Catálogo de Productos")
    root.geometry("600x400")
    root.configure(bg="#f4f4f4")
    
    main_frame = tk.Frame(root, padx=10, pady=10, bg="#f4f4f4")
    main_frame.pack(expand=True, fill='both')
    
    canvas = tk.Canvas(main_frame, bg="#f4f4f4")
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f4f4f4")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 1), window=scrollable_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    for item in catalog_items:
        product_frame = tk.Frame(scrollable_frame, padx=10, pady=10, bg="#e1f5f5", relief="raised")
        product_frame.pack(fill="y", pady=5)
        
        tk.Label(product_frame, text=item["nombre"], font=("Arial", 14, "bold"), bg="#e1f5f5").pack(anchor="w")
        tk.Label(product_frame, text=item["descripcion"], bg="#e1f5f5").pack(anchor="w")
        tk.Label(product_frame, text=item["precio"], font=("Arial", 12, "italic"), bg="#e1f5f5").pack(anchor="w")
    
    root.mainloop()

create_catalog_window()
