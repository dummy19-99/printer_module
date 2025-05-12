import os
import win32print
import win32api
import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # GUIウィンドウは表示しない
    file_path = filedialog.askopenfilename(
        title="PDFファイルを選択",
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path

def print_pdf(filepath):
    if not filepath:
        print("ファイルが選択されませんでした。")
        return

    default_printer = win32print.GetDefaultPrinter()
    print(f"既定のプリンター: {default_printer}")
    win32print.StartDocPrinter(
        default_printer,
        1,
        ("PDF印刷", None, "RAW")
    )
    print(f"印刷中: {filepath}")
    win32api.ShellExecute(
        0,
        "print",
        filepath,
        None,
        ".",
        0
    )

if __name__ == "__main__":
    pdf_path = select_pdf_file()
    print_pdf(pdf_path)