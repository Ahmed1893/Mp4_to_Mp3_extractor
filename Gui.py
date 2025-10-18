import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip
from PIL import Image

# Initial GUI appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AudioExtractorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🎵 MP4 to MP3 Extractor")
        self.geometry("500x340")
        self.resizable(False, False)
        self.folder_path = None
        self.dark_mode = True

        # Load icons
        self.sun_icon = ctk.CTkImage(light_image=Image.open("Sun.png"), size=(24, 24))
        self.moon_icon = ctk.CTkImage(light_image=Image.open("Moon.png"), size=(24, 24))

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Extract Audio from MP4 to MP3", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=15)

        self.theme_button = ctk.CTkButton(self, text="", image=self.moon_icon, width=36, height=36, command=self.toggle_theme)
        self.theme_button.place(x=450, y=10)

        self.select_button = ctk.CTkButton(self, text="📁 Select Folder", command=self.select_folder, width=240)
        self.select_button.pack(pady=5)

        self.convert_button = ctk.CTkButton(self, text="🎬 Convert to MP3", command=self.start_conversion_thread, width=240)
        self.convert_button.pack(pady=5)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar_is_visible = False  # track display state

        self.file_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.file_label.pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=15))
        self.status_label.pack(pady=5)

    def toggle_theme(self):
        if self.dark_mode:
            ctk.set_appearance_mode("Light")
            self.theme_button.configure(image=self.sun_icon)
        else:
            ctk.set_appearance_mode("Dark")
            self.theme_button.configure(image=self.moon_icon)
        self.dark_mode = not self.dark_mode

    def select_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder with MP4 Files")
        if self.folder_path:
            self.status_label.configure(text="📂 Folder selected.")

    def start_conversion_thread(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return
        threading.Thread(target=self.extract_audio, daemon=True).start()

    def show_progress_bar(self):
        if not self.progress_bar_is_visible:
            self.progress_bar.pack(pady=10)
            self.progress_bar_is_visible = True

    def hide_progress_bar(self):
        if self.progress_bar_is_visible:
            self.progress_bar.pack_forget()
            self.progress_bar_is_visible = False

    def extract_audio(self):
        mp4_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith('.mp4')]
        total = len(mp4_files)

        if total == 0:
            self.status_label.configure(text="")
            messagebox.showinfo("No Videos", "No .mp4 files found in the selected folder.")
            return

        self.status_label.configure(text="Processing...")
        self.show_progress_bar()
        self.progress_bar.set(0)

        for index, file in enumerate(mp4_files, start=1):
            mp4_path = os.path.join(self.folder_path, file)
            mp3_path = os.path.join(self.folder_path, os.path.splitext(file)[0] + '.mp3')

            percent = int((index / total) * 100)
            self.file_label.configure(text=f"🎧 Converting: {file} ({percent}%)")
            self.update_idletasks()

            try:
                video = VideoFileClip(mp4_path)
                video.audio.write_audiofile(mp3_path, logger=None)
                video.close()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {file}:\n{e}")
                continue

            self.progress_bar.set(index / total)

        # Final display
        self.file_label.configure(text=f"✅ Done (100%)")
        self.status_label.configure(text="All files have been converted.")
        messagebox.showinfo("Done", "✅ Done: All MP4 files have been converted to MP3.")
        self.progress_bar.set(1)

if __name__ == "__main__":
    app = AudioExtractorApp()
    app.mainloop()
