import tkinter as tk
from tkinter import filedialog, Text, Frame, Button, Label, Scrollbar


class SimpleNotepad(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Notepad")

        self.current_file = None  # To track the current file path

        # Create a text area with a scrollbar
        self.text_area = Text(self, wrap=tk.WORD)
        self.scrollbar = Scrollbar(self, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Frame for buttons
        self.button_frame: Frame = Frame(self)
        self.button_frame.pack()

        self.save_button: Button = Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        self.load_button: Button = Button(self.button_frame, text="Load", command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

        # Label for status messages
        self.status_label: Label = Label(self, text="No file loaded", anchor="w")
        self.status_label.pack(fill=tk.X)

    def save_file(self) -> None:
        if self.current_file:  # Save to the current file if it exists
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            self.status_label.config(text=f"Saved to {self.current_file}")
        else:
            self.save_as_file()

    def save_as_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text files", "*.txt")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            self.title(f"Notepad - {file_path}")
            self.status_label.config(text=f"Saved to {file_path}")

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content: str = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.title(f"Notepad - {file_path}")
            self.status_label.config(text=f"Loaded file from {file_path}")

    def run(self):
        self.mainloop()


def main() -> None:
    app = SimpleNotepad()
    app.run()


if __name__ == '__main__':
    main()
