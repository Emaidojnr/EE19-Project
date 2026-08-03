# GET 324 Mini Project - Group EE19

## Project Overview
This repository contains the source code and documentation for the GET 324 mini-project, collaboratively developed by Group EE19. The primary objective of this project is to implement core computational and engineering principles to solve the assigned problem sets.

## Code Description
* **Algorithm Implementation:** Contains the necessary logic and structural code required by the GET 324 curriculum.
* **Execution:** Designed to process the required computational tasks accurately and efficiently.
* **Version Control:** Managed via Git to track group contributions and code integration.

---
**Contributor:** 22/eg/ee/2109
=======
# EE19 Project

## Overview

EE19 Project is a software application developed to provide an efficient and user-friendly solution for its intended purpose. The project is built with modern development practices, focusing on performance, scalability, and maintainability.

## Features

- Clean and intuitive user interface
- Responsive design
- Secure and reliable functionality
- Well-structured project architecture
- Easy deployment and maintenance

## Technologies Used

- Frontend: *(Add framework, e.g., React, HTML/CSS, JavaScript)*
- Backend: *(Add framework, e.g., Node.js, Express, Laravel, Django)*
- Database: *(e.g., MongoDB, MySQL, PostgreSQL)*
- Other Tools: *(Git, Docker, etc.)*

## Project Structure

```
EE19-Project/
├── src/
├── public/
├── assets/
├── components/
├── package.json
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/shugabright565/EE19-Project.git
```

2. Navigate to the project directory:

```bash
cd EE19-Project
```

3. Install dependencies:

```bash
npm install
```

4. Start the development server:

```bash
npm run dev
```

or

```bash
npm start
```

## Usage

Open your browser and navigate to:

```
http://localhost:3000
```

or the port specified by your development server.

## Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Author
22/EG/EE/2019 - Robson, Israel Bassey
=======
# Concrete Crack Detection System

> A lightweight vision pipeline that tells you, from a single photo, whether a concrete surface is cracked — and how confident it is about that call.

## Why This Project Exists

Cracks in concrete are one of the earliest visible signs of structural fatigue, and catching them early is far cheaper than repairing what they eventually lead to. Manual inspection is slow, subjective, and doesn't scale — two inspectors can look at the same wall and disagree. This project explores a small, practical question: **can a lightweight model do a first-pass triage of crack images reliably enough to be useful in the field?**

The result is a two-stage pipeline rather than a single classifier — a design choice explained below.

## How It Actually Works

Most crack-detection demos stop at "load a CNN, predict, done." This one adds a check *before* that step:

1. **Anomaly gate.** Before trusting the crack classifier's verdict, the image is passed through an autoencoder-style anomaly detector. It reconstructs the input and measures how far off the reconstruction is (`reconError`). If an image looks nothing like the surfaces the model was trained on — a random object, a blurry photo, the wrong kind of material entirely — the reconstruction error spikes and the app can flag it as out-of-distribution instead of confidently guessing wrong.
2. **Crack classification.** Only after that sanity check does the image go to the dedicated CNN that decides **Cracked** vs **Non-Cracked**, returning a confidence score alongside the label.

This two-stage approach — gatekeeper model, then specialist model — is the core design decision that separates this from a plain single-model classifier, and it's the part worth highlighting if you're comparing it against similar projects.

## Project Structure

```
EE19/
├── app.py                     # Streamlit application (UI + inference pipeline)
├── crackDetectionModel.keras  # CNN trained to classify Cracked / Non-Cracked
├── anomalyDetector.keras      # Autoencoder used as the out-of-distribution gate
└── anomalyThreshold.txt       # Reconstruction-error cutoff for the anomaly gate
```

## Running It

```bash
pip install streamlit tensorflow numpy pillow
streamlit run app.py
```

Upload an image of a concrete surface at the prompt. The app resizes it to 120×120, normalizes it, runs it through the anomaly gate, then the crack classifier, and returns a labeled prediction with a confidence percentage.

## Design Notes & Honest Limitations

- The model works on still images only — no video stream or live camera support yet.
- Confidence scores reflect the classifier's certainty, not a physical measurement of crack severity (width, depth, length aren't estimated).
- The anomaly threshold is a fixed value read from `anomalyThreshold.txt` rather than dynamically calibrated per deployment — worth tuning if you retrain on a different dataset.

## Possible Extensions

Ideas for anyone building on this: heatmap visualization of *where* the crack was detected (Grad-CAM), batch image processing with a results table, or a rough severity score derived from pixel-level crack geometry.

## Author

Epharim  
**Reg No:** 22/EG/EE/1989
=======
EE19-Project/
├── EE19/
│   ├── app.py                      # Streamlit application
│   ├── model.ipynb                 # Training & evaluation notebook
│   ├── crackDetectionModel.keras   # Trained crack classifier
│   ├── anomalyDetector.keras       # Trained autoencoder
│   ├── anomalyThreshold.txt        # Reconstruction error threshold
│   ├── requirements.txt            # Python dependencies
│   └── dataset_small/
│       ├── Positive/               # Cracked concrete images
│       └── Negative/               # Non-cracked concrete images
└── README.md
22/EG/EE/2049
