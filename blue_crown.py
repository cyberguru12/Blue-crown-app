import tkinter as tk
from tkinter import messagebox

# History content
history_sections = [
    ("Pre-Colonial Botswana", 
     "Botswana's early history is marked by the migration of the Tswana people..."
    ),
    ("Colonial Era", 
     "During the late 19th century, Botswana became a British Protectorate..."
    ),
    ("Independence", 
     "Botswana gained independence on 30 September 1966..."
    ),
    ("Modern Botswana", 
     "Today, Botswana is known for its stable democracy and rich wildlife..."
    )
]

class BlueCrownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blue Crown - History of Botswana")
        self.root.geometry("700x500")
        self.root.configure(bg="#1E90FF")  # Blue theme
        self.current = 0

        # Title
        self.title_label = tk.Label(root, text="", font=("Helvetica", 20, "bold"), bg="#1E90FF", fg="white")
        self.title_label.pack(pady=20)

        # Content
        self.content_text = tk.Text(root, wrap="word", font=("Helvetica", 14), bg="#87CEFA", fg="#000080")
        self.content_text.pack(expand=True, fill="both", padx=20, pady=10)

        # Navigation buttons
        btn_frame = tk.Frame(root, bg="#1E90FF")
        btn_frame.pack(pady=10)
        self.prev_btn = tk.Button(btn_frame, text="⏮ Previous", command=self.prev_section, bg="white", fg="#1E90FF")
        self.prev_btn.pack(side="left", padx=10)
        self.next_btn = tk.Button(btn_frame, text="Next ⏭", command=self.next_section, bg="white", fg="#1E90FF")
        self.next_btn.pack(side="left", padx=10)

        self.update_section()

    def update_section(self):
        title, content = history_sections[self.current]
        self.title_label.config(text=title)
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, content)

    def next_section(self):
        if self.current < len(history_sections) - 1:
            self.current += 1
            self.update_section()
        else:
            messagebox.showinfo("Blue Crown", "You have reached the end of the history!")

    def prev_section(self):
        if self.current > 0:
            self.current -= 1
            self.update_section()
        else:
            messagebox.showinfo("Blue Crown", "You are at the beginning.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlueCrownApp(root)
    root.mainloop()
