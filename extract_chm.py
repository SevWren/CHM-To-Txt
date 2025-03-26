import chm
import tkinter as tk
from tkinter import filedialog, messagebox
import traceback
import os
import datetime

# Enable Debugging
DEBUG_MODE = True  

# Define paths for logs and output
LOG_DIR = "logs"
OUTPUT_DIR = "output"

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Setup logging
log_filename = os.path.join(LOG_DIR, f"chm_extraction_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

def log_message(message):
    """Logs messages to a file and prints if debugging is enabled."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)
    
    if DEBUG_MODE:
        print(log_entry.strip())

# Open file dialog to select the CHM file
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

try:
    log_message("Starting CHM extraction tool.")

    # Select CHM file
    chm_path = filedialog.askopenfilename(title="Select CHM File", filetypes=[("CHM Files", "*.chm")])
    if not chm_path:
        log_message("No CHM file selected. Exiting.")
        exit()

    log_message(f"Selected CHM file: {chm_path}")

    # Load the CHM file
    chm_file = chm.CHMFile(chm_path)

    # Suggest a default output filename in the /output/ folder
    default_output_path = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(chm_path))[0] + ".txt")

    # Select output text file location
    output_path = filedialog.asksaveasfilename(
        title="Save Extracted Text File",
        initialdir=OUTPUT_DIR,  # Default to output folder
        initialfile=os.path.basename(default_output_path),
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    
    if not output_path:
        log_message("No output file selected. Exiting.")
        exit()

    log_message(f"Saving extracted text to: {output_path}")

    # Extract text and save
    with open(output_path, "w", encoding="utf-8") as output_file:
        for topic in chm_file.topics():
            content = chm_file.topiccontent(topic)
            output_file.write(f"== {topic} ==\n{content}\n\n")

    log_message("Extraction completed successfully.")
    messagebox.showinfo("Success", f"Extraction completed!\nSaved to: {output_path}")

except Exception as e:
    error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
    log_message(error_msg)
    messagebox.showerror("Error", f"An error occurred.\nDetails saved in {log_filename}")

