import customtkinter as ctk
from PIL import Image, ImageTk

def alternate_case(text):
    result = ''
    toggle = True
    for char in text:
        if char.isalpha():
            result += char.lower() if toggle else char.upper()
            toggle = not toggle
        else:
            result += char
    return result

def convert_text():
    input_text = entry.get()
    output_text = alternate_case(input_text)
    result_label.configure(text=output_text)
    
    # Automatically copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(output_text)
    root.update()

def copy_to_clipboard():
    output_text = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(output_text)
    root.update()

# Initialize the CustomTkinter root window
ctk.set_appearance_mode("dark")  # Modes: "dark", "light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("El Mockko")  # App name

# Set the window icon (replace 'icon.ico' with your .ico file path)
root.iconbitmap('icon.ico')

root.geometry("600x600")

# Input label and entry
input_label = ctk.CTkLabel(root, text="Enter text:", font=('Arial', 16))
input_label.pack(pady=10)

entry = ctk.CTkEntry(root, width=400, height=40, font=('Arial', 14))
entry.pack(pady=10)

# Convert button
convert_button = ctk.CTkButton(root, text="Convert", command=convert_text, width=120, height=40)
convert_button.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(root, text="", font=('Arial', 16))
result_label.pack(pady=10)

# Copy to clipboard button
copy_button = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard, width=120, height=40)
copy_button.pack(pady=10)

# Load and display the image (JPEG or PNG)
image_path = 'retard.png'  # Replace with your correct image path
img = Image.open(image_path)
img = img.resize((300, 150))  # Resize the image
img_tk = ImageTk.PhotoImage(img)

# Correct image display for CTkLabel
image_label = ctk.CTkLabel(root, image=img_tk, text="")  # Remove default 'ctklabel' text
image_label.image = img_tk  # Keep a reference to avoid garbage collection
image_label.pack(pady=10)

# Start the application
root.mainloop()
