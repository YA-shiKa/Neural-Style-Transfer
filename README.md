# 🎨 Neural Style Transfer (NST) Web App

This project implements **Neural Style Transfer** using both **TensorFlow** and **PyTorch**, and provides a **Flask-based web application** where users can upload images to generate stylized art.

---

## 📌 Table of Contents
- [🎥 Demo](#-demo)
- [🛠 Technologies Used](#-technologies-used)
- [📁 Project Structure](#-project-structure)
- [👩‍💻 Contributors](#-contributors)


---

## 🎥 Demo
> Upload a content image and a style image, and get a new image that blends both!

**[🖼 View Sample Output](#-results)**

---

## 🛠 Technologies Used
- Python
- TensorFlow & Keras
- PyTorch
- Flask
- HTML / CSS (Frontend)
- VGG19 Pre-trained Model

---

## 📁 Project Structure
```text
├── app.py                                 # Flask backend  
├── nst.py                                 # PyTorch implementation  
├── neuralstyle.ipynb                      # TensorFlow notebook  
├── index.html                             # Frontend HTML  
├── content.jpg                            # Sample content image  
├── style.jpg                              # Sample style image  
├── output.png                             # Output image  
├── README.md                              # Project README  
├── AIML REPORT(E23CSEU1153).docx          # Project Report  
├── Neural-Style-Transfer-with-TensorFlow.pptx  # Project Slides
```
---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YA-shiKa/Neural-Style-Transfer.git
cd Neural-Style-Transfer
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install the key packages:
```bash
pip install torch torchvision flask tensorflow
```

### 4. Run the Flask App
```bash
python app.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## 👩‍💻 Contributors

- **YA-shiKa**  
  GitHub: [YA-shiKa](https://github.com/YA-shiKa)  



