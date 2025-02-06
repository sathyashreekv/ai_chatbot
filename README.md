# Image to Sketch - Streamlit App

This is a simple **Streamlit** application that converts an image into a pencil sketch using OpenCV.

## 🚀 Features
- Upload an image (`.jpg`, `.jpeg`, `.png`)
- Convert it to a grayscale pencil sketch
- Adjust blur intensity for different sketch styles
- Download the sketch

## 🖥️ Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/image-to-sketch.git
cd image-to-sketch
```
### **2️⃣ Install Dependencies**
Ensure you have **Python 3.7+** installed, then run:
```bash
pip install streamlit opencv-python numpy pillow
```

### **3️⃣ Run the Streamlit App**
```bash
streamlit run app.py
```

## 📦 Dependencies
This project requires the following libraries:
- **Streamlit** - For building the web app
- **OpenCV (cv2)** - For image processing
- **NumPy** - For numerical operations
- **Pillow (PIL)** - For image handling

## 📸 How It Works Internally
1. **Upload an Image** → Convert it into a NumPy array.
2. **Convert to Grayscale** → Removes color information.
3. **Invert Colors** → Highlights sketchable areas.
4. **Apply Gaussian Blur** → Softens details.
5. **Invert Blur and Divide** → Creates a hand-drawn effect.
6. **Display & Download** → Shows and allows downloading the sketch.

## 📂 Project Structure
```
image-to-sketch/
├── app.py  # Main Streamlit app
├── README.md  # Project documentation
```

## 🛠️ Contributing
Feel free to open issues and contribute to the project!

## 📜 License
This project is licensed under the **MIT License**.

