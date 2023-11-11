import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import qrcode

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    display_qr_code()

def display_qr_code():
    qr_image = Image.open("qrcode.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_image = Image.open("qrcode.png")
        qr_image.save(file_path)

# Create the main window
root = tk.Tk()
root.title("QR Code Scanner")

# Entry for QR code data
entry = tk.Entry(root)
entry.pack(pady=10)

# Buttons
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(side=tk.LEFT, padx=5)
save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack(side=tk.LEFT, padx=5)

# Label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Variable to hold scanned QR code value
qr_value = tk.StringVar()
qr_value_label = tk.Label(root, textvariable=qr_value)
qr_value_label.pack()

# Start the Tkinter main loop
root.mainloop()