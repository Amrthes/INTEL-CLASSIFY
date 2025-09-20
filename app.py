import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# ----------------- Load model -----------------
MODEL_PATH = "intel_mobilenetv2.h5"  # change to your model path
model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

# ----------------- Prediction function -----------------
def predict_image(img: Image.Image):
    img = img.resize((128, 128))
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    preds = model.predict(arr)[0]
    top_idx = np.argmax(preds)
    label = CLASS_NAMES[top_idx]
    confidence = float(preds[top_idx])
    # return label, confidence, full probability array
    return label, confidence, {cls: float(p) for cls, p in zip(CLASS_NAMES, preds)}

# ----------------- Gradio Interface -----------------
title = "🌍 Intel Image Classification (MobileNetV2)"
description = "Upload an image (buildings, forest, glacier, mountain, sea, street) and the model will classify it."

iface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Textbox(label="Predicted Class"),
        gr.Number(label="Confidence"),
        gr.Label(num_top_classes=6, label="Class Probabilities")
    ],
    title=title,
    description=description,
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()
