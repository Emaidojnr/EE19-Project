# EE19-Project — Concrete Bridge Deck Crack Detection

GET 324 mini project for group EE19.

A Streamlit web app that classifies uploaded images of concrete surfaces as **Cracked** or **Non-Cracked**. Before classification, an anomaly-detection autoencoder first checks whether the uploaded image actually looks like a concrete surface, to reduce false predictions on irrelevant images.

## How it works

1. **Anomaly check** — An autoencoder (`anomalyDetector.keras`) reconstructs the uploaded image. If the reconstruction error exceeds a stored threshold (`anomalyThreshold.txt`), the app rejects the image as "not a concrete surface."
2. **Crack classification** — If the image passes the anomaly check, a CNN classifier (`crackDetectionModel.keras`) predicts whether the surface is cracked or non-cracked.
3. **Confidence handling** — Predictions with confidence between 0.4 and 0.6 are flagged as uncertain, prompting the user to try a clearer image.

## Tech stack

- [Streamlit](https://streamlit.io/) — web app interface
- [TensorFlow / Keras](https://www.tensorflow.org/) — model loading and inference
- [Pillow (PIL)](https://python-pillow.org/) — image handling
- [NumPy](https://numpy.org/) — array/image preprocessing

## Project structure

```
EE19-Project/
├── EE19/
│   ├── app.py                     # Streamlit app (main entry point)
│   ├── crackDetectionModel.keras  # CNN model for crack classification
│   ├── anomalyDetector.keras      # Autoencoder for anomaly detection
│   └── anomalyThreshold.txt       # Reconstruction error threshold
└── README.md
```

> Note: update the file/folder names above if they differ from your actual repo layout.

## Getting started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/shugabright565/EE19-Project.git
cd EE19-Project/EE19
pip install streamlit numpy pillow tensorflow
```

### Run the app

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (typically `http://localhost:8501`) in your browser.

## Usage

1. Launch the app.
2. Upload an image of a concrete surface (`.jpg`, `.jpeg`, or `.png`).
3. The app will:
   - Reject the image if it doesn't resemble a concrete surface.
   - Otherwise, display a prediction of **Cracked** or **Non-Cracked** with a confidence score.

## Model details

| Parameter | Value |
|---|---|
| Input image size | 120 × 120 |
| Classes | `Non-Cracked`, `Cracked` |
| Pixel normalization | 0–1 (divided by 255.0) |
| Uncertain prediction range | 0.4 – 0.6 confidence |

## Team

GET 324 — Group EE19

## Author
22/EG/EE/2039
