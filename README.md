# 🎵 MP4 to MP3 Extractor (CustomTkinter GUI)

A simple yet powerful desktop application built with **Python**, **CustomTkinter**, and **MoviePy** that allows you to extract audio (MP3) from MP4 video files in bulk with a beautiful, responsive dark/light theme toggle.

---

## 🚀 Features

- 🎬 **Batch Conversion** – Convert all `.mp4` files in a folder to `.mp3` automatically.  
- 🌙 **Dark / Light Mode** – Toggle appearance modes on the fly.  
- 📁 **Simple Folder Selection** – Choose any folder containing MP4 files.  
- 🔊 **Progress Bar** – Real-time visual feedback of conversion progress.  
- ⚡ **Threaded Conversion** – Keeps GUI responsive while processing files.  
- ✅ **Error Handling** – Displays messages if conversion fails or no videos are found.  

---

## 🖼️ GUI Preview

The interface features:
- A clean CustomTkinter design
- Folder selection and conversion buttons
- Real-time progress display and current file name
- Dark/light mode icons (`Sun.png`, `Moon.png`)

---

## 🧩 Requirements

- Python 3.8 or higher  
- The following Python packages:
  ```bash
  pip install customtkinter moviepy Pillow
  ```

---

## 📦 Setup & Usage

1. **Clone or download** this repository.  
2. Make sure you have the required dependencies installed (see above).  
3. Place `Sun.png` and `Moon.png` icons in the same directory as the script.  
4. Run the application:
   ```bash
   python main.py
   ```
5. Click **"📁 Select Folder"** to choose your folder containing `.mp4` files.  
6. Click **"🎬 Convert to MP3"** to start extraction.  
7. Converted `.mp3` files will be saved in the same folder as the videos.  

---

## 🧠 How It Works

The program:
- Scans the selected folder for all `.mp4` files.  
- Uses **MoviePy** to extract and save audio as `.mp3`.  
- Updates the progress bar and current file being processed in real-time.  
- Uses threading to prevent GUI freezing during conversion.  

---

## 📁 Project Structure

```
📂 MP4_to_MP3_Extractor/
├── main.py                # Main Python script (the GUI)
├── Sun.png                # Light mode icon
├── Moon.png               # Dark mode icon
├── README.md              # Project documentation
└── LICENSE                # Open-source license
```

---

## 🪪 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 💡 Author

**Developed by:**  AKY Tricks

**Year:** 2025  

Feel free to modify, enhance, and use it for personal or commercial purposes under the MIT License.

---
