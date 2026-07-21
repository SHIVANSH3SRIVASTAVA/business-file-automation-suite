import tkinter as tk
from tkinter import ttk, filedialog
from src.automation.rename import rename_files

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Business File Automation Suite")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.selected_folder = tk.StringVar()
        self.base_name = tk.StringVar(value="File")
        self.operation = tk.StringVar(value="rename")

        self.create_widgets()

    def create_widgets(self):

        title = ttk.Label(
            self.root,
            text="Business File Automation Suite",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=20)

        folder_frame = ttk.Frame(self.root)
        folder_frame.pack(fill="x", padx=20)

        ttk.Label(folder_frame, text="Selected Folder:").pack(anchor="w")

        folder_entry = ttk.Entry(
            folder_frame,
            textvariable=self.selected_folder,
            width=70
        )
        folder_entry.pack(side="left", padx=(0, 10), pady=5)

        browse_btn = ttk.Button(
            folder_frame,
            text="Browse",
            command=self.browse_folder
        )
        browse_btn.pack(side="left")


        # Base Name Section
        base_frame = ttk.Frame(self.root)
        base_frame.pack(fill="x", padx=20, pady=(10, 0))

        ttk.Label(base_frame, text="Base Name:").pack(anchor="w")

        ttk.Entry(
            base_frame,
            textvariable=self.base_name,
            width=30
        ).pack(anchor="w", pady=5)

        operation_frame = ttk.LabelFrame(
            self.root,
            text="Operation"
        )
        operation_frame.pack(fill="x", padx=20, pady=20)

        operations = [
            ("Rename Files", "rename"),
            ("Organize Files", "organize"),
            ("Add Prefix", "prefix"),
            ("Add Suffix", "suffix"),
            ("Replace Text", "replace"),
            ("Remove Text", "remove"),
            ("Change Case", "case")
        ]

        for text, value in operations:
            ttk.Radiobutton(
                operation_frame,
                text=text,
                value=value,
                variable=self.operation
            ).pack(anchor="w", padx=10, pady=2)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        self.preview_btn = ttk.Button(
            button_frame,
            text="Preview",
            state="disabled"
        )
        self.preview_btn.pack(side="left", padx=10)

        self.run_btn = ttk.Button(
            button_frame,
            text="Run",
            state="disabled",
            command=self.run_operation
        )
        self.run_btn.pack(side="left", padx=10)

        self.status = ttk.Label(
            self.root,
            text="Status: Ready"
        )
        self.status.pack(side="bottom", pady=20)

    def browse_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.selected_folder.set(folder)

            self.preview_btn.config(state="normal")
            self.run_btn.config(state="normal")

            self.status.config(text="Status: Folder Selected")

    def run_operation(self):

        folder = self.selected_folder.get()

        if not folder:
            self.status.config(text="Status: Please select a folder.")
            return

        operation = self.operation.get()

        if operation == "rename":

            success, message = rename_files(
                folder,
                self.base_name.get().strip()
            )

            self.status.config(text=f"Status: {message}")

        else:
            self.status.config(
                text="Status: Feature coming in next sprint."
        )


    def run(self):
        self.root.mainloop()