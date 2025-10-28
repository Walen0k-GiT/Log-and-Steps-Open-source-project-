import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
from datetime import datetime


class LogViewer:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg='black')
        self.window.title("Log and Steps (Open source project)")
        self.window.iconbitmap("log_and_steps.ico")
        self.window.geometry("600x400")

        # Цвета для темной темы
        self.bg_color = 'black'
        self.fg_color = 'white'
        self.entry_bg = '#333333'
        self.button_bg = '#444444'

        # Interface
        label = tk.Label(window,
                        text="Log and Steps - System Logs Viewer \n By: Walen0k \n Github - ",
                        font=("Regular, italic", 16, "bold"),
                        bg=self.bg_color,
                        fg=self.fg_color)
        label.pack(pady=10)

        # Log selection
        frame_top = tk.Frame(window, bg=self.bg_color)
        frame_top.pack(pady=15)

        self.log_type = tk.StringVar(value="Castllar")

        # Radiobuttons с темной темой
        tk.Radiobutton(frame_top, text="System", variable=self.log_type, value="system",
                    bg=self.bg_color, fg=self.fg_color, selectcolor='black').pack(side=tk.LEFT)
        tk.Radiobutton(frame_top, text="Application", variable=self.log_type, value="application",
                    bg=self.bg_color, fg=self.fg_color, selectcolor='black',).pack(side=tk.LEFT),
        tk.Radiobutton(frame_top, text="Security", variable=self.log_type, value="security",
                    bg=self.bg_color, fg=self.fg_color, selectcolor='black').pack(side=tk.LEFT)

        # Controls
        frame_controls = tk.Frame(window, bg=self.bg_color)
        frame_controls.pack(pady=5)

        # Кнопки с темной темой
        tk.Button(frame_controls, text="Load Logs", command=self.load_logs,
                bg=self.button_bg, fg=self.fg_color).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_controls, text="Clear", command=self.clear_logs,
                bg=self.button_bg, fg=self.fg_color).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_controls, text="Export", command=self.export_logs,
                bg=self.button_bg, fg=self.fg_color).pack(side=tk.LEFT, padx=5)

        # Logs area с темной темой
        self.log_text = scrolledtext.ScrolledText(window,
                                                width=90,
                                                height=25,
                                                wrap=tk.WORD,
                                                bg=self.entry_bg,
                                                fg=self.fg_color,
                                                insertbackground=self.fg_color)  # Цвет курсора
        self.log_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def load_logs(self):
        try:
            command = f"Get-EventLog -LogName {self.log_type.get()} -Newest 50 | Format-Table TimeGenerated, EntryType, Source, Message -Wrap -AutoSize"
            result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True,
                                    encoding='cp866')

            self.log_text.delete(1.0, tk.END)
            if result.returncode == 0:
                self.log_text.insert(1.0, result.stdout)
            else:
                self.log_text.insert(1.0, f"Error: {result.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logs: {str(e)}")

    def clear_logs(self):
        self.log_text.delete(1.0, tk.END)

    def export_logs(self):
        logs = self.log_text.get(1.0, tk.END)
        if logs.strip():
            filename = f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(logs)
            messagebox.showinfo("Success", f"Logs saved to {filename}")
        else:
            messagebox.showwarning("Warning", "No data to export")


if __name__ == "__main__":
    root = tk.Tk()
    app = LogViewer(root)
    root.mainloop()