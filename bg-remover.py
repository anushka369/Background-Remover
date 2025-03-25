import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas
from rembg import remove
from PIL import Image, ImageTk
import io

# Perform background removal using GrabCut algorithm
def enhanced_grabcut(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found or unable to load: {image_path}")
    
    height, width = image.shape[:2]
    mask = np.zeros(image.shape[:2], np.uint8)
    rect = (10, 10, width - 20, height - 20)
    
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    
    kernel = np.ones((5, 5), np.uint8)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
    
    foreground = image * mask2[:, :, np.newaxis]
    return foreground

# Open file dialog to select an image and process it
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp")])
    if not file_path:
        return
    
    image = Image.open(file_path)
    img_display = image.resize((300, 300))
    img_display = ImageTk.PhotoImage(img_display)
    image_canvas.create_image(0, 0, anchor=tk.NW, image=img_display)
    image_canvas.image = img_display
    
    process_image(image, file_path)

# Process image with both Rembg and GrabCut and display results
def process_image(image, input_path):
    # Automatic background removal with rembg
    output_rembg = remove(image)
    img_io = io.BytesIO()
    output_rembg.save(img_io, format='PNG')
    img_io.seek(0)
    processed_img = Image.open(img_io)
    
    # Background removal with GrabCut
    grabcut_output = enhanced_grabcut(input_path)
    grabcut_output = cv2.cvtColor(grabcut_output, cv2.COLOR_BGR2RGB)
    grabcut_output = Image.fromarray(grabcut_output)
    
    # Display rembg result
    processed_img_display = processed_img.resize((300, 300))
    processed_img_display = ImageTk.PhotoImage(processed_img_display)
    output_canvas_rembg.create_image(0, 0, anchor=tk.NW, image=processed_img_display)
    output_canvas_rembg.image = processed_img_display
    
    # Display GrabCut result
    grabcut_display = grabcut_output.resize((300, 300))
    grabcut_display = ImageTk.PhotoImage(grabcut_display)
    output_canvas_grabcut.create_image(0, 0, anchor=tk.NW, image=grabcut_display)
    output_canvas_grabcut.image = grabcut_display
    
    save_output(processed_img, grabcut_output)

# Save processed images
def save_output(output_rembg, output_grabcut):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        output_rembg.save(f"{save_path}_rembg.png", format='PNG')
        output_grabcut.save(f"{save_path}_grabcut.png", format='PNG')
        status_label.config(text=f"Saved: {save_path}_rembg.png & {save_path}_grabcut.png")

def on_enter(e):
    e.widget.config(bg="#ff5722", fg="white")

def on_leave(e):
    e.widget.config(bg="#007bff", fg="white")

# GUI Setup
root = tk.Tk()
root.title("Background Remover - Rembg & GrabCut")
root.geometry("1000x600")
root.configure(bg="#ffeb3b")

header = Label(root, text="🖼️ Background Remover", font=("Arial", 18, "bold"), bg="#ffeb3b", fg="#333")
header.pack(pady=10)

btn_select = Button(root, text="📂 Select Image", command=select_image, font=("Arial", 12, "bold"), bg="#007bff", fg="white", padx=10, pady=5, borderwidth=2, relief="raised")
btn_select.pack(pady=10)
btn_select.bind("<Enter>", on_enter)
btn_select.bind("<Leave>", on_leave)

frame = tk.Frame(root, bg="#ffeb3b")
frame.pack(pady=10)

image_canvas = Canvas(frame, width=300, height=300, bg="#ff9800", highlightthickness=2, relief="ridge")
image_canvas.grid(row=0, column=0, padx=20, pady=10)

output_canvas_rembg = Canvas(frame, width=300, height=300, bg="#4caf50", highlightthickness=2, relief="ridge")
output_canvas_rembg.grid(row=0, column=1, padx=20, pady=10)

output_canvas_grabcut = Canvas(frame, width=300, height=300, bg="#3f51b5", highlightthickness=2, relief="ridge")
output_canvas_grabcut.grid(row=0, column=2, padx=20, pady=10)

status_label = Label(root, text="", font=("Arial", 12, "bold"), fg="#d32f2f", bg="#ffeb3b")
status_label.pack(pady=10)

root.mainloop()
