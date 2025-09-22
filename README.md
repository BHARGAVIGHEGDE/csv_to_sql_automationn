# CSV to SQL Server Uploader

This Python-based desktop application provides a simple **GUI** for uploading one or more CSV files into SQL Server tables.  
It helps automate data entry from CSV files into the database without needing to write SQL queries manually.

---

## Features
- Select multiple CSV files at once  
- Input target SQL Server and database name  
- Assign a target table name for each file  
- Automatically map and insert CSV data into corresponding SQL tables  
- Handles column mismatch errors gracefully  
- Built-in error handling and logging for debugging  
- Built with **Tkinter**, **pandas**, and **pyodbc**  

---

##  Technologies Used
- **Python**  
- **Tkinter** (for GUI)  
- **Pandas** (for CSV handling)  
- **PyODBC** (for SQL Server connection)  

---

##  How to Use

### 1. Clone the repository
```bash
git clone https://github.com/BHARGAVIGHEGDE/csv_to_sql_automationn.git
cd csv_to_sql_automationn
```

### 2. Install dependencies
```bash
pip install pandas pyodbc
```

### 3. Run the application
```bash
python start.py
```

### 4. Steps inside the application
1. Enter your **SQL Server** and **Database name**.  
2. Select one or more **CSV files**.  
3. For each file, specify the **destination table name**.  
4. Click **OK** to upload the data.  

---

##  Error Handling
1. Displays an error if server/database name is missing.  
2. Validates if CSV columns match SQL table columns.  

---
  
