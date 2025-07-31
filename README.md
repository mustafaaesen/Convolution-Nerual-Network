## 📦 Models & Dataset (Faces) - Drive Link

Due to GitHub’s 100 MB file size limitation, the following large files are **not included** in this repository:

- `lfw-deepfunneled.zip` (face dataset used in the Labeled Faces Project)
- `lfw_yuz-tanima_modeli.h5` (trained CNN model for face recognition)

You can download these files from Google Drive via the link below and manually place them in the appropriate project directories:

🔗 **[Download from Google Drive](https://drive.google.com/file/d/1uepc5jL5OY7yFsCGhE2cHzoVN_9wgw1D/view?usp=sharing)**

> ⚠️ After downloading, extract `lfw-deepfunneled.zip` and place the folder in the correct location as specified in the notebooks.  
> The `.h5` model file can be used directly to test predictions without retraining the model.




# 🧠 Convolutional Neural Network Projects

This repository contains four different Convolutional Neural Network (CNN) projects implemented with TensorFlow/Keras. Each project demonstrates a complete deep learning workflow: model training, saving, and testing with external data. These projects are suitable for beginner-to-intermediate level deep learning learners.

---

## 📁 Folder Structure
```
Convolution Neural Network/
│
├── MNIST Project/
│ ├── Model Training/
│ │ ├── Convolutional_Neural_Network_MNIST_Project.ipynb
│ │ └── convolutional_neural_network_mnist_project.py
│ ├── Model Control/
│ │ ├── Convolutional_Neural_Network_MNIST_Project_Model_Control.ipynb
│ │ └── convolutional_neural_network_mnist_project_model_control.py
│ └── el_yazisi_modeli.h5
│
├── Fashion MNIST Project/
│ ├── Model Training/
│ │ ├── Convolutional_Neural_Network_Fashion_MNIST_Project.ipynb
│ │ └── convolutional_neural_network_fashion_mnist_project.py
│ ├── Model Control/
│ │ ├── Convolutional_Neural_Network_Fashion_MNIST_Project_Model_Control.ipynb
│ │ └── convolutional_neural_network_fashion_mnist_project_model_control.py
│ └── fashion_mnist_modeli.h5
│
├── CIFAR-10 Project/
│ ├── Model Training/
│ │ ├── Convolutional_Neural_Network_CIFAR_10_Project.ipynb
│ │ └── convolutional_neural_network_cifar_10_project.py
│ ├── Model Control/
│ │ ├── Convolutional_Neural_Network_CIFAR_10_Project_Model_Control.ipynb
│ │ └── convolutional_neural_network_cifar_10_project_model_control.py
│ └── cifar-10_modeli.h5
│
├── Labeled Faces Project/
│ ├── Model Training/
│ │ ├── Convolutional_Neural_Network_Labeled_Faces_Project.ipynb
│ │ └── convolutional_neural_network_labeled_faces_project.py
│ ├── Model Control/
│ │ ├── Convolutional_Neural_Network_Labeled_Faces_Project_Model_Control.ipynb
│ │ └── convolutional_neural_network_labeled_faces_project_model_control.py
│ └── lfw_yuz-tanima_modeli.h5

---
```
## 🔬 Project Descriptions

### 1. **MNIST Digit Recognition**
- **Dataset:** MNIST handwritten digits
- **Goal:** Train a CNN to classify digits 0-9.
- **Accuracy Achieved:** >98%
- **Test Method:** Model tested with external uploaded digit images.

---

### 2. **Fashion MNIST Classification**
- **Dataset:** Zalando's Fashion-MNIST
- **Goal:** Classify images of shirts, shoes, bags, etc.
- **Model:** CNN with 3 convolutional layers
- **Test Method:** Manual testing with custom clothing images.

---

### 3. **CIFAR-10 Object Recognition**
- **Dataset:** CIFAR-10 (10-class image dataset)
- **Goal:** Classify objects like airplane, ship, truck, cat, etc.
- **Special Note:** Used RGB color images (32x32), higher complexity.

---

### 4. **Labeled Faces Recognition**
- **Dataset:** LFW (Labeled Faces in the Wild)
- **Goal:** Train a CNN model to recognize different real-world people.
- **Challenge:** Data filtered to include only people with ≥15 images.
- **Classes Used:** 96 persons, real face photos.
- **Result:** Face classification using CNN model trained from scratch.

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/mustafaaesen/Convolution-Nerual-Network.git

pip install tensorflow numpy matplotlib
Open the .ipynb notebooks to run model training or control.

If you want to test the pre-trained models, use the Model Control notebooks.


