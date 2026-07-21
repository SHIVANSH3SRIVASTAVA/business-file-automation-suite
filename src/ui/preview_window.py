import tkinter as tk
from tkinter import ttk, messagebox

from src.automation.rename import rename_files


class PreviewWindow:
    def __init__(self, parent, preview_data):
        self.parent = parent
        self.preview_data = preview_data

        self.window = tk.Toplevel(parent)
        self.window.title("Rename Preview")
        self.window.geometry("900x550")
        self.window.resizable(False, False)

        self.create_widgets()
        self.load_preview()

    def create_widgets(self):

        title = ttk.Label(
            self.window,
            text="Rename Preview",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=15)

        table_frame = ttk.Frame(self.window)
        table_frame.pack(fill="both", expand=True, padx=20)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("old", "new"),
            show="headings",
            height=18
        )

        self.tree.heading("old", text="Current Name")
        self.tree.heading("new", text="New Name")

        self.tree.column("old", width=400)
        self.tree.column("new", width=400)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=20)

        rename_btn = ttk.Button(
            button_frame,
            text="Rename Files",
            command=self.rename_files
        )
        rename_btn.pack(side="left", padx=10)

        cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            command=self.window.destroy
        )
        cancel_btn.pack(side="left", padx=10)

    def load_preview(self):

        for item in self.preview_data:
            self.tree.insert(
                "",
                "end",
                values=(
                    item["old_name"],
                    item["new_name"]
                )
            )

    def rename_files(self):

        success, message = rename_files(self.preview_data)

        if success:
            messagebox.showinfo(
                "Success",
                message
            )

            self.window.destroy()

        else:
            messagebox.showerror(
                "Error",
                message
            )