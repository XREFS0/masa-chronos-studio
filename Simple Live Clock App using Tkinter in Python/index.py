"""
MASA Chronos: World Clock & Precision Chronometer
Developer: MASA
"""

import time
from datetime import datetime
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaChronos(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MASA Chronos Studio")
        self.geometry("480x420")
        self.resizable(False, False)
        self.configure(fg_color="#0A0D14")

        self.sw_running = False
        self.sw_start_time = 0.0
        self.sw_elapsed = 0.0

        self._build_ui()
        self._update_clock_loop()

    def _build_ui(self):
        header = ctk.CTkFrame(self, fg_color="#111625", corner_radius=14)
        header.pack(fill="x", padx=20, pady=(20, 10))

        title = ctk.CTkLabel(
            header,
            text="MASA CHRONOS ENGINE",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#38BDF8",
        )
        title.pack(pady=(12, 2))

        subtitle = ctk.CTkLabel(
            header,
            text="Atomic Chronometry & Digital Stopwatch",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 12))

        clock_card = ctk.CTkFrame(self, fg_color="#111625", corner_radius=16)
        clock_card.pack(fill="x", padx=20, pady=5)

        self.lbl_time = ctk.CTkLabel(
            clock_card,
            text="00:00:00",
            font=ctk.CTkFont(family="Consolas", size=48, weight="bold"),
            text_color="#F8FAFC",
        )
        self.lbl_time.pack(pady=(16, 2))

        self.lbl_date = ctk.CTkLabel(
            clock_card,
            text="Loading date...",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#38BDF8",
        )
        self.lbl_date.pack(pady=(0, 16))

        stopwatch_card = ctk.CTkFrame(self, fg_color="#111625", corner_radius=16)
        stopwatch_card.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        lbl_sw_title = ctk.CTkLabel(
            stopwatch_card,
            text="CHRONOMETER",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#64748B",
        )
        lbl_sw_title.pack(pady=(10, 2))

        self.lbl_sw_display = ctk.CTkLabel(
            stopwatch_card,
            text="00:00.00",
            font=ctk.CTkFont(family="Consolas", size=26, weight="bold"),
            text_color="#FBBF24",
        )
        self.lbl_sw_display.pack(pady=4)

        sw_controls = ctk.CTkFrame(stopwatch_card, fg_color="transparent")
        sw_controls.pack(fill="x", padx=20, pady=(5, 12))
        sw_controls.grid_columnconfigure((0, 1), weight=1)

        self.btn_sw_toggle = ctk.CTkButton(
            sw_controls,
            text="Start",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#0284C7",
            hover_color="#0369A1",
            corner_radius=8,
            height=36,
            command=self._toggle_stopwatch,
        )
        self.btn_sw_toggle.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.btn_sw_reset = ctk.CTkButton(
            sw_controls,
            text="Reset",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#334155",
            hover_color="#475569",
            corner_radius=8,
            height=36,
            command=self._reset_stopwatch,
        )
        self.btn_sw_reset.grid(row=0, column=1, padx=(5, 0), sticky="ew")

    def _update_clock_loop(self):
        now = datetime.now()
        self.lbl_time.configure(text=now.strftime("%H:%M:%S"))
        self.lbl_date.configure(text=now.strftime("%A, %B %d, %Y").upper())

        if self.sw_running:
            cur_elapsed = self.sw_elapsed + (time.time() - self.sw_start_time)
            mins = int(cur_elapsed // 60)
            secs = int(cur_elapsed % 60)
            csecs = int((cur_elapsed * 100) % 100)
            self.lbl_sw_display.configure(text=f"{mins:02d}:{secs:02d}.{csecs:02d}")

        self.after(50, self._update_clock_loop)

    def _toggle_stopwatch(self):
        if not self.sw_running:
            self.sw_running = True
            self.sw_start_time = time.time()
            self.btn_sw_toggle.configure(text="Pause", fg_color="#EF4444", hover_color="#DC2626")
        else:
            self.sw_running = False
            self.sw_elapsed += time.time() - self.sw_start_time
            self.btn_sw_toggle.configure(text="Resume", fg_color="#0284C7", hover_color="#0369A1")

    def _reset_stopwatch(self):
        self.sw_running = False
        self.sw_elapsed = 0.0
        self.btn_sw_toggle.configure(text="Start", fg_color="#0284C7", hover_color="#0369A1")
        self.lbl_sw_display.configure(text="00:00.00")


if __name__ == "__main__":
    app = MasaChronos()
    app.mainloop()
