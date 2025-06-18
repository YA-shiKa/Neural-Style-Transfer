# 🎨 Neural Style Transfer (NST) Web App

This project is a web-based tool that applies neural style transfer to combine the content of one image with the artistic style of another. Built using Flask, PyTorch, and Tailwind CSS, it provides a clean and responsive interface for uploading images and viewing stylized results.

---

## 🖼️ Features

- Upload your own **content** and **style** images
- View real-time result comparisons (Content | Style | Stylized Output)
- Responsive layout with **Dark Mode toggle**
- Image processing using PyTorch-based **Neural Style Transfer**

---

## 🎥 Preview
> Upload a content image and a style image, and get a new image that blends both!
![image](https://github.com/user-attachments/assets/5594b671-95da-4e31-915a-945361dfa2af)
![image](https://github.com/user-attachments/assets/cdf37a09-7e30-4df9-a907-e0a31be310b7)

---

## 🛠️ Technologies Used
- Python, PyTorch

- Flask (Backend & Routing)

- Tailwind CSS, HTML, Jinja2 (Frontend)

---

## 💡 How It Works
- User uploads a content image and a style image.

- Backend loads both images, extracts features via VGG-19, and computes losses.

- The output is optimized via gradient descent to generate a stylized version.

- The final image is saved and displayed in the browser.

---

## 👩‍💻 Contributors

- **Yashika Maligi**  
  GitHub: [YA-shiKa](https://github.com/YA-shiKa)  



