# Background Removal Project 🌆

## 📂 Overview
This project implements an automatic background removal technique using OpenCV's GrabCut algorithm. The program allows users to select an image and removes its background, leaving only the foreground object.

---

## ✂ Features

- Uses OpenCV's GrabCut algorithm for background removal
- Enhances the mask using morphological operations for better results
- Provides a user-friendly file selection dialog via Tkinter
- Displays the processed image with the background removed

---

## 💻 Requirements

Ensure you have the following dependencies installed before running the script:

```bash
pip install opencv-python numpy tkinter
```

---

## 🤖 How It Works 

1. The user selects an image file through a Tkinter file dialog.
2. The script applies the GrabCut algorithm to estimate the foreground object.
3. Morphological operations are used to refine the mask.
4. The background is removed, and the foreground is extracted.
5. The final image is displayed using OpenCV.

---

## 🖼 Usage

1. Run the script using:

    ```bash
    python script.py
    ```

2. Follow the on-screen prompt to select an image file. Once the processing is complete, the extracted foreground will be displayed.

---

## 🚥 Limitations

- The bounding box is automatically defined, which may not be optimal for all images.
- The method may not work well with complex backgrounds.
- Manual fine-tuning might be required for better accuracy.

---

## 🪴 Future Improvements

- Allow users to manually define the bounding box.
- Implement an interactive GUI for better user experience.
- Optimize performance for large images.

---

## 🩹 Contributions

This is a personal learning project, but submitting issues and suggestions are welcome!
<br> If you find any improvements, feel free to create a pull request. To contribute:

1. Fork the repository.

2. Create a new branch for your feature/bug fix.

3. Commit your changes and submit a pull request.

---

## 🫧 Authors
- Anushka Banerjee : < [@anushka369](https://github.com/anushka369) >
- Shashank Singh : < [@shashankexore](https://github.com/shashankexore) >

---
