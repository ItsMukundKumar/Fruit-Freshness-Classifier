import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import gdown
import os

# ---- CONFIG ----
IMG_SIZE = 244
MODEL_PATH = "fruit_model.h5"

# ---- DOWNLOAD MODEL ----
if not os.path.exists(MODEL_PATH):
    st.write("Downloading model... ⏳")
    url = "https://drive.google.com/file/d/1mbYFUQxcr8zr1xqPslmGqveAHofgD69K/view"
    gdown.download(url, MODEL_PATH, quiet=False, fuzzy=True)

# ---- LOAD MODEL ----
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH, compile=False)

model = load_model()

# ---- UI CSS ----
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00C6FF;
}
.sub-text {
    text-align: center;
    color: #aaa;
    font-size: 18px;
    margin-bottom: 20px;
}
.result-box {
    text-align: center;
    padding: 15px;
    border-radius: 10px;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---- UI ----
st.markdown('<div class="main-title">🍎 Fruit Freshness Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Upload an image and click Predict</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Preview", use_container_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing..."):

            img = image.resize((IMG_SIZE, IMG_SIZE))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)[0][0]

            if prediction > 0.5:
                confidence = prediction
                st.markdown(
                    f'<div class="result-box" style="background-color:#ff4b4b;color:white;">🥀 Rotten ({confidence:.2f})</div>',
                    unsafe_allow_html=True
                )
            else:
                confidence = 1 - prediction
                st.markdown(
                    f'<div class="result-box" style="background-color:#6eefa3;color:black;">✅ Fresh ({confidence:.2f})</div>',
                    unsafe_allow_html=True
                )

            st.progress(float(confidence))