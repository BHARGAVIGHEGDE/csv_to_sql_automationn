This Python-based desktop application provides a simple GUI for uploading one or more CSV files into SQL Server tables. It helps automate data entry from CSV files into the database without needing to write SQL queries manually.

✅ Features
Select multiple CSV files at once

Input target SQL Server and database name

Assign a target table name for each file

Automatically map and insert CSV data into corresponding SQL tables

Handles column mismatch errors gracefully

Built-in error handling and logging for debugging

Built with Tkinter, pandas, and pyodbc

🛠️ Technologies Used
Python

Tkinter (for GUI)

Pandas (for CSV handling)

PyODBC (for SQL Server connection)

🚀 How to Use
Clone the repository:
git clone https://github.com/yourusername/csv-to-sql-uploader.git
cd csv-to-sql-uploader

Install dependencies:
pip install pandas pyodbc

Run the application:
python start.py
Enter your SQL Server and Database name.

Select one or more CSV files.

For each file, specify the destination table name.

Click OK to upload the data.

⚠️ Error Handling
Displays an error if server/database name is missing

Validates if CSV columns match SQL table columns

