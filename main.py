import time
import datetime as dt
import tkinter as tk
import winsound

WORK = 25*60
BREAK = 5*60

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.phase = "Work"
        self.remaining = WORK
        self.running = False
        self.start_time=dt.datetime.now().strftime("%H:%M")

        self.root.title("Pomodoro Timer")

        self.start_label = tk.Label(root, text=f"Start Time: {self.start_time}", font=("Arial", 14))
        self.start_label.pack(pady=10)

        self.label = tk.Label(root, text=self.format_time(self.remaining), font=("Arial", 36))
        self.label.pack(pady=20)


        self.start_btn = tk.Button(root, text="Start", command=self.start)
        self.start_btn.pack(side="left", expand=True)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop)
        self.stop_btn.pack(side="left", expand=True)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.pack(side="left", expand=True)

    def format_time(self, sec):
        m, s = divmod(sec, 60)
        return f"{m:02d}:{s:02d}"

    def update(self):
        if self.running:
            self.remaining -= 1
            self.label.config(text=self.format_time(self.remaining))

            self.root.title(f"{self.format_time(self.remaining)} - {self.phase}")

            if self.remaining <= 0:
                winsound.Beep(880 if self.phase=="Work" else 440, 400)
                if self.phase == "Work":
                    self.phase = "Break"
                    self.remaining = BREAK
                else:
                    self.phase = "Work"
                    self.remaining = WORK

            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.start_time=time.strftime("%H:%M:%S")
            self.start_label.config(text=self.start_time)
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.phase = "Work"
        self.remaining = WORK
        self.label.config(text=self.format_time(self.remaining))
        self.root.title("Pomodoro Timer")

if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro(root)
    root.mainloop()
