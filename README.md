🌍 Intel Image Classification (CNN + MobileNetV2)

This project classifies images into 6 natural scene categories:
- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

## 📂 Project Structure
INTEL_PROJECT/
│── intel_mobilenetv2.h5 # Pretrained CNN model
│── app.py # Streamlit app
│── analysis.ipynb # Notebook for metrics & visualization
│── requirements.txt # Dependencies
│── outputs/ # Saved graphs & results
│ ├── confusion_matrix.png
│ ├── sample_predictions.png
│ ├── accuracy_loss_curve.png
│ └── classification_report.txt


## 🚀 How to Run

### 1️⃣ Install Dependencies

## 🚀 How to Run

### 1️⃣ Install Dependencies

pip install -r requirements.txt

## requirements.txt

tensorflow
numpy
pandas
matplotlib
seaborn
scikit-learn
streamlit
Pillow

2️⃣ Run the Analysis Notebook

Open analysis.ipynb in Jupyter Notebook or VS Code and run all cells.
It will generate:

Confusion matrix

Classification report

Sample predictions

Accuracy/Loss curves (if training history available)

All images will be saved inside the outputs/ folder.


3️⃣ Run the Streamlit App

streamlit run app.py
Upload any image, and the model will classify it into one of the 6 categories.

📊 Example Outputs

✅ Confusion Matrix

✅ Sample Predictions

💡 Notes
Model used: MobileNetV2 (transfer learning)

Dataset: Intel Image Classification Dataset

Runs on CPU (no GPU needed).

## 📌 Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt```


SAMPLE OUTPUT 1 : <img width="1920" height="984" alt="Screenshot 2025-09-20 121458" src="https://github.com/user-attachments/assets/0f8efbf6-11d7-41a4-a3ed-3d4d0aaf0d4a" />


SAMPLE OUTPUT 2 : <img width="1920" height="1020" alt="Screenshot 2025-09-20 121554" src="https://github.com/user-attachments/assets/79805175-213d-4ad3-af79-71f80f4c69d8" />


SAMPLE OUTPUT 3 : <img width="1920" height="977" alt="Screenshot 2025-09-20 121522" src="https://github.com/user-attachments/assets/26bb6e7d-e805-403f-a57f-2bb9d265be8c" />




