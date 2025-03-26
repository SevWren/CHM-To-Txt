---

### 📜 **README.md - CHM-To-Txt**  

```md
# CHM-To-Txt 📖➡️📄  

A Python tool to extract text from `.chm` (Compiled HTML Help) files and save them as plain text or PDF.  
Includes logging for debugging and error tracking.

Decided to write this as AI context windows grow, using native documentation for scripting languages will become more and more useful for forcing 
LLM models to restrict their suggestions to those compatible with the source language versus making assumptions.

## 🚀 Features  
- **Select CHM File via File Explorer**  
- **Extract Text from CHM**  
- **Save Output as `.txt`** (User-selectable location)  
- **Error Logging & Debugging** (Logs saved in `/logs/` folder)  
- **Optional PDF Conversion**  

---

## 🛠 Installation  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/yourusername/CHM-To-Txt.git
cd CHM-To-Txt
```

### 2️⃣ **Create a Virtual Environment**  
```sh
python -m venv chm_env
```
Activate the virtual environment:  
- **Windows (CMD)**:  
  ```sh
  chm_env\Scripts\activate
  ```
- **PowerShell**:  
  ```sh
  chm_env\Scripts\Activate.ps1
  ```

### 3️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

---

## 📂 Folder Structure  
```
CHM-To-Txt/
│── chm_env/                # Virtual environment (not included in Git)
│── logs/                   # Stores error logs
│── src/                    # Source code
│   ├── extract_chm.py      # Extracts text from CHM
│   ├── convert_to_pdf.py   # Converts text to PDF (optional)
│── docs/                   # Documentation (if needed)
│── requirements.txt        # Dependencies list
│── README.md               # This file
│── .gitignore              # Git ignore settings
```

---

## 🏃‍♂️ Usage  

1️⃣ **Run the script**  
```sh
python src/extract_chm.py
```

2️⃣ **Select the CHM file** via the file explorer.  
3️⃣ **Choose an output `.txt` file** location.  
4️⃣ ✅ Done! The extracted text is saved to the selected file.  

### **Optional: Convert to PDF**  
```sh
python src/convert_to_pdf.py
```

---

## 🛠 Troubleshooting  

### ❌ `error: Microsoft Visual C++ 14.0 or greater is required`  
➡ **Solution**: Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and select:  
   - ✅ **MSVC v142 - VS 2019 C++ Build Tools**  
   - ✅ **Windows 10 SDK**  

### ❌ `No file selected. Exiting.`  
➡ **Solution**: Ensure you select a CHM file when prompted.  

### ❌ `PermissionError: [Errno 13] Permission denied`  
➡ **Solution**: Ensure you have **write permissions** in the output folder. Try running as **Administrator**.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 🌟 Acknowledgments  
- `pychm` library for CHM parsing  
- `Tkinter` for file selection  
- `reportlab` for optional PDF generation  

---

🎯 **Enjoy hassle-free CHM extraction! 🚀**  
```