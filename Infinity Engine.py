import pygame as Infinity2D
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import threading
import sys
import os
import subprocess

# Initialize Pygame
Infinity2D.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = Infinity2D.display.set_mode((WIDTH, HEIGHT))
Infinity2D.display.set_caption("Infinity2D")

# Define initial background color (white)
background_color = (255, 255, 255)

# Clock for controlling the frame rate
clock = Infinity2D.time.Clock()

# Global variable to hold the imported image
imported_image = None

# Function to run code from the code editor in the graphics window
def run_code():
    global running
    code = code_editor.get("1.0", tk.END)  # Get code from the editor window
    try:
        # Execute the code in the context of the graphics program
        exec(code)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to save code to a file
def save_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if file_path:
        code = code_editor.get("1.0", tk.END)
        try:
            with open(file_path, "w") as file:
                file.write(code)
            messagebox.showinfo("Save Successful", f"Code saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save file: {e}")

# Function to import an image asset
def import_asset():
    global imported_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        try:
            imported_image = Infinity2D.image.load(file_path)
            imported_image = Infinity2D.transform.scale(imported_image, (100, 100))  # Resize to fit in the window if needed
            messagebox.showinfo("Import Successful", f"Image imported from {file_path}")
        except Exception as e:
            messagebox.showerror("Import Error", f"Failed to import image: {e}")

# Function to open color settings for customizing the window background color
def open_color_settings():
    global background_color
    color_code = colorchooser.askcolor(title="Choose Background Color")[0]
    if color_code:
        # Convert the RGB color tuple to integers
        background_color = tuple(int(value) for value in color_code)
        messagebox.showinfo("Color Change", f"Background color set to {background_color}")

# Function to compile the code into an executable
def compile_to_exe():
    code = code_editor.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Warning", "Code editor is empty. Please write code before compiling.")
        return

    # Save the code to a temporary file
    temp_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "temp_code.py")
    try:
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(code)
        
        # Run PyInstaller to compile the code
        compile_command = f"pyinstaller --onefile --distpath {os.path.expanduser('~')}/Desktop --workpath {os.path.expanduser('~')}/Desktop --specpath {os.path.expanduser('~')}/Desktop {temp_file_path}"
        subprocess.run(compile_command, shell=True, check=True)

        messagebox.showinfo("Compilation Successful", "Your executable has been created on the Desktop.")
    except Exception as e:
        messagebox.showerror("Compilation Error", f"Failed to compile the code: {e}")

# Set up the code editor using Tkinter
def start_code_editor():
    global code_editor, root
    root = tk.Tk()
    root.title("InfinityEngine")  # Title for the IDE window
    root.geometry("1200x800")  # Adjust size as needed

    # Set up the editor window with buttons and text editor
    code_editor = tk.Text(root, wrap="none", width=100, height=30, bg="#1E1E1E", fg="#D4D4D4", insertbackground='white')
    code_editor.pack(padx=10, pady=10)

    run_button = tk.Button(root, text="Run Code", command=run_code, bg="#3A3A3A", fg="#FFFFFF")
    run_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Code", command=save_code, bg="#3A3A3A", fg="#FFFFFF")
    save_button.pack(pady=5)

    import_button = tk.Button(root, text="Import Asset", command=import_asset, bg="#3A3A3A", fg="#FFFFFF")
    import_button.pack(pady=5)

    settings_button = tk.Button(root, text="Settings", command=open_color_settings, bg="#3A3A3A", fg="#FFFFFF")
    settings_button.pack(pady=5)

    compile_button = tk.Button(root, text="Compile to EXE", command=compile_to_exe, bg="#3A3A3A", fg="#FFFFFF")
    compile_button.pack(pady=5)

    root.mainloop()

# Start the code editor in a separate thread
threading.Thread(target=start_code_editor, daemon=True).start()

# Main loop flag
running = True

# Main loop for the 2D graphics
while running:
    # Event handling
    for event in Infinity2D.event.get():
        if event.type == Infinity2D.QUIT:
            running = False

    # Clear the screen with the selected background color
    screen.fill(background_color)

    # Draw a black square (cube) at position (300, 250) with size 100x100 pixels
    Infinity2D.draw.rect(screen, (0, 0, 0), (300, 250, 100, 100))

    # If an image has been imported, display it on the screen at a specified position
    if imported_image:
        screen.blit(imported_image, (400, 300))  # Position image at (400, 300)

    # Update the display
    Infinity2D.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
Infinity2D.quit()
sys.exit()
