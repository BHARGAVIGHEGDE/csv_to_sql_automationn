import tkinter as tk
from tkinter import filedialog, messagebox
import pyodbc
import pandas as pd
import os
import traceback


class CSVUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Import Tool")
        self.csv_files = []
        
        tk.Label(root, text="Server Name:").grid(row=0, column=0, sticky="e")
        self.server_entry = tk.Entry(root, width=40)
        self.server_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Database Name:").grid(row=1, column=0, sticky="e")
        self.db_entry = tk.Entry(root, width=40)
        self.db_entry.grid(row=1, column=1)
        
        tk.Button(root, text="Select CSV Files", command=self.select_csv_files).grid(row=2, column=0, columnspan=2, pady=5)
        
        self.file_frame = tk.Frame(root)
        self.file_frame.grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="OK", command=self.upload_to_sql).grid(row=4, column=0, columnspan=2, pady=10)

    def select_csv_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
        for i, path in enumerate(file_paths, start=len(self.csv_files)):
            tk.Label(self.file_frame, text=path, wraplength=400, anchor='w', justify='left').grid(row=i, column=0, sticky='w')
            table_entry = tk.Entry(self.file_frame, width=30)
            table_entry.grid(row=i, column=1, padx=5)
            self.csv_files.append((path, table_entry))


    def upload_to_sql(self):
        server_name = self.server_entry.get().strip()
        database_name = self.db_entry.get().strip()

       
        if not server_name and not database_name:
            messagebox.showerror("Error", "Please enter both server name and database name.")
            return
        elif not server_name:
            messagebox.showerror("Error", "Server name not selected.")
            return
        elif not database_name:
            messagebox.showerror("Error", "Database name not selected.")
            return

        try:
            conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'
            )
            cursor = conn.cursor()

            for file_path, table_entry in self.csv_files:
                table_name = table_entry.get().strip()
                if not table_name:
                    messagebox.showwarning("Missing Table Name", f"Please enter a table name for {file_path}")
                    return
                df = pd.read_csv(file_path)    
                cols = ', '.join(f'[{col}]' for col in df.columns)
                placeholders = ', '.join('?' for _ in df.columns)
                cursor.execute(f"SELECT TOP 1 * FROM {table_name}")
                for _, row in df.iterrows():
                    cursor.execute(f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})", tuple(row))

            conn.commit()
            messagebox.showinfo("Success", "All files uploaded successfully.")
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Error", str(e))

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVUploaderApp(root)
    root.mainloop()
