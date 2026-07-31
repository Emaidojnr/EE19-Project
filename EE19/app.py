import os
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

imgSize = 120
classNames = ["Non-Cracked", "Cracked"]

st.set_page_config(page_title="Concrete Crack Detection")

root = os.path.dirname(os.path.abspath(__file__))


@st.cache_resource
def loadModels():
    crack_path = os.path.join(root, "crackDetectionModel.keras")
    anomaly_path = os.path.join(root, "anomalyDetector.keras")
    threshold_path = os.path.join(root, "anomalyThreshold.txt")

    crackModel = tf.keras.models.load_model(crack_path)
    anomalyModel = tf.keras.models.load_model(anomaly_path)
    with open(threshold_path, "r") as f:
        threshold = float(f.read())
    return crackModel, anomalyModel, threshold


crackModel, anomalyModel, threshold = loadModels()

st.title("Concrete Bridge Deck Crack Detection")
st.write("Upload an image of a concrete surface to check if it's cracked or non-cracked.")

uploadedFile = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploadedFile is not None:
    image = Image.open(uploadedFile).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    resized = image.resize((imgSize, imgSize))
    arr = np.array(resized, dtype="float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    reconstructed = anomalyModel.predict(arr)
    reconError = np.mean(np.square(arr - reconstructed))

    if reconError > threshold:
        st.error(f"This doesn't look like a concrete surface. Please upload a photo of a concrete surface")
    else:
        prediction = crackModel.predict(arr)[0][0]

        if 0.4 <= prediction <= 0.6:
            st.warning(f"Uncertain prediction (confidence: {prediction:.2f}). Try a clearer image.")
        else:
            label = classNames[1] if prediction > 0.5 else classNames[0]
            confidence = prediction if prediction > 0.5 else 1 - prediction
            st.success(f"Prediction: **{label}** (confidence: {confidence:.2%})")
