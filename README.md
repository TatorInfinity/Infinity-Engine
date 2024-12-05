# Infinity-Engine
Infinity Engine is a simple yet powerful Python-based game engine for building 2D games.
Infinity Engine
Overview
Infinity Engine is an innovative game engine and integrated development environment (IDE) designed for seamless 2D game creation. Built using pygame and tkinter, this tool enables developers to write, test, and compile Python code with real-time feedback and a powerful graphics display. Infinity Engine allows rapid development, live code execution, and easy compilation into Windows executables, making it a perfect choice for game developers looking for an efficient and user-friendly development environment.

Key Features
Real-Time Game Creation: Create and modify 2D games interactively, with changes reflected instantly.
Integrated Code Editor: A built-in Python editor for writing and managing game code within the same window.
Immediate Code Execution: Run your code directly from the editor and view updates in real-time.
Asset Importing: Easily import images to use as sprites, backgrounds, or other game assets.
Customizable Background: Change the background color of the IDE window to suit your preferences.
Code Compilation: Convert your Python scripts into standalone Windows executable files using PyInstaller.
Extendable Architecture: Integrate your own Python scripts and external libraries for enhanced functionality.
Requirements
Ensure you have Python 3.6 or higher installed, along with the following libraries:

pygame: For 2D game development and graphical rendering.
tkinter: For building the code editor and user interface.
PyInstaller: For compiling Python code into a Windows executable.
Installing Dependencies
To install the required Python packages, use:

bash
Copy code
pip install pygame tk pyinstaller
Installation Instructions
Download or Clone the Repository: Get the project files onto your system.
Install Dependencies: Ensure that Python and all required libraries are installed.
Run the Engine: Launch the IDE by executing main.py.
bash
Copy code
python main.py
How to Use Infinity Engine
Launch the IDE: Start main.py to open the Infinity Engine IDE.
Write and Edit Code: Use the built-in code editor to write Python code for your game logic.
Run Code: Click the "Run Code" button to see real-time updates in the graphics window.
Import Assets: Use the "Import Asset" button to load images into your project.
Customize Appearance: Access "Settings" to change the background color of the IDE.
Compile to EXE: Click "Compile to EXE" to create a standalone executable, making your game easy to distribute.
Example Code
Here's a simple example to get started with drawing shapes and displaying an image:

python
Copy code
# Draw a red rectangle at (150, 150) with size 50x50 pixels
Infinity2D.draw.rect(screen, (255, 0, 0), (150, 150, 50, 50))

# Display the imported image at (200, 200)
if imported_image:
    screen.blit(imported_image, (200, 200))
Project Structure
graphql
Copy code
InfinityEngine/
│
├── main.py               # Main script to launch the IDE and game engine
├── requirements.txt      # Lists Python dependencies
└── README.md             # This README file
Troubleshooting
Import Errors: Make sure all required libraries (pygame, tkinter, pyinstaller) are installed.
Compilation Issues: If the compilation fails, ensure that PyInstaller is installed and that there are no errors in your code.
Code Execution: Debug any Python syntax errors by using the "Run Code" button and checking the console output.
Future Improvements
Syntax Highlighting: Implement a more advanced text editor with syntax highlighting and code auto-completion.
Advanced Asset Management: Support more asset formats like audio files and 3D models.
Custom Game Templates: Add templates for common game types (e.g., platformers, puzzles).
Performance Enhancements: Optimize rendering and code execution for smoother performance.
Contributing
We welcome contributions! To contribute, please email tatoralexander2000@gmail.com
