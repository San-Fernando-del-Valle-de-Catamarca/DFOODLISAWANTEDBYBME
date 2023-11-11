import tkinter as tk
from datetime import datetime


class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.start_time = None
        self.end_time = None
        self.running = False
        self.lap_times = []

        self.time_display = tk.Label(master, font=('Helvetica', 40))
        self.time_display.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.lap_button = tk.Button(master, text="Lap", command=self.lap)
        self.lap_button.pack(side=tk.LEFT, padx=5)

        self.lap_list = tk.Listbox(master)
        self.lap_list.pack(side=tk.LEFT, padx=5)

        self.update_display()

    def update_display(self):
        if self.running:
            self.current_time = datetime.now() - self.start_time
            milliseconds = self.current_time.total_seconds() * 1000
            self.time_display.config(
                text=f"{int(milliseconds // 60000):02}:{int((milliseconds // 1000) % 60):02}.{int(milliseconds % 1000):03}")
            self.master.after(1, self.update_display)

    def start(self):
        if not self.running:
            if not self.start_time:
                self.start_time = datetime.now()
            else:
                self.start_time = datetime.now() - (self.end_time - self.start_time)
            self.running = True
            self.update_display()

    def stop(self):
        if self.running:
            self.end_time = datetime.now()
            self.running = False

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.running = False
        self.lap_times = []
        self.time_display.config(text="00:00.000")
        self.lap_list.delete(0, tk.END)

    def lap(self):
        if self.running:
            lap_time = datetime.now() - self.start_time
            self.lap_times.append(lap_time)
            self.lap_list.insert(tk.END,
                                 f"{int(lap_time.total_seconds() // 60):02}:{int(lap_time.total_seconds() % 60):02}.{int((lap_time.microseconds // 1000))}")


# Create the main window
root = tk.Tk()
root.title("Stopwatch")

# Create an instance of the Stopwatch class
stopwatch = Stopwatch(root)

# Start the Tkinter main loop
root.mainloop()