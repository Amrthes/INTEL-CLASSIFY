<img width="1920" height="1020" alt="Screenshot 2025-09-20 121458" src="https://github.com/user-attachments/assets/041b7e59-d97c-46e3-b475-00a95d320d6d" /># 🌍 Intel Image Classification (CNN + MobileNetV2)

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

yaml
Copy code

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
requirements.txt

nginx
Copy code
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
bash
Copy code
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
   pip install -r requirements.txt

SAMPLE OUTPUT 1 : <img width="1920" height="1020" alt="Screenshot 2025-09-20 121554" src="https://github.com/user-attachments/assets/2e1e3ab9-5588-4cdd-805f-c05a81451569" />

SAMPLE OUTPUT 2 : <img width="1920" height="1020" alt="Screenshot 2025-09-20 121458" src="https://github.com/user-attachments/assets/ac280e12-35a9-44e1-a635-7698a09d748d" />

SAMPLE OUTPUT 3 : <img width="1920" height="1020" alt="Screenshot 2025-09-20 121522" src="https://github.com/user-attachments/assets/e67f2ff1-1cd3-4bf5-b26a-7be851fe3c91" />



