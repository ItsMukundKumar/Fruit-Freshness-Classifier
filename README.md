<h1 align="center">🍎 Fruit Freshness Classifier</h1>

<p align="center">
A Deep Learning project that classifies fruit images as <b>Fresh</b> or <b>Rotten</b> using Convolutional Neural Networks (CNN) and a Streamlit web app.
</p>

<p align="center">
🚀 Built with TensorFlow • 🎯 Binary Classification • 🎨 Streamlit UI
</p>

---

<h2>🚀 Project Overview</h2>

This project uses a <b>Convolutional Neural Network (CNN)</b> to classify fruit images into two categories:
<ul>
<li>✅ Fresh</li>
<li>🥀 Rotten</li>
</ul>

The model is trained on a dataset containing multiple fruit types and then simplified into a <b>binary classification problem</b>.

---

<h2>🧠 Model Architecture</h2>

<ul>
<li>Conv2D (32 filters) + ReLU</li>
<li>MaxPooling</li>
<li>Conv2D (64 filters) + ReLU</li>
<li>MaxPooling</li>
<li>Conv2D (128 filters) + ReLU</li>
<li>MaxPooling</li>
<li>Flatten</li>
<li>Dense (128 units) + ReLU</li>
<li>Output Layer (Sigmoid)</li>
</ul>

<p><b>Loss Function:</b> Binary Crossentropy</p>
<p><b>Optimizer:</b> Adam</p>
<p><b>Input Size:</b> 244 × 244</p>

---

<h2>📂 Dataset</h2>

<ul>
<li>Fruit Freshness Dataset</li>
<li>Multiple classes: apples, bananas, oranges</li>
<li>Each class divided into <b>fresh</b> and <b>rotten</b></li>
</ul>

<h3>📁 Folder Structure</h3>

<pre>
train/
 ├── freshapples/
 ├── freshbanana/
 ├── freshoranges/
 ├── rottenapples/
 ├── rottenbanana/
 └── rottenoranges/
</pre>

---

<h2>⚙️ Features</h2>

<ul>
<li>📷 Upload fruit image</li>
<li>🔍 Predict using trained CNN model</li>
<li>📊 Confidence score display</li>
<li>🎨 Clean UI with custom CSS</li>
<li>⚡ Fast inference</li>
</ul>

---

<h2>🖥️ Streamlit App</h2>

<ul>
<li>Interactive UI for predictions</li>
<li>Real-time image classification</li>
<li>User-friendly design</li>
</ul>

<p align="center">
<img src="https://via.placeholder.com/800x400.png?text=App+Preview" width="80%">
</p>

---

<h2>🛠️ Tech Stack</h2>

<ul>
<li><b>Frontend:</b> Streamlit</li>
<li><b>Backend:</b> TensorFlow / Keras</li>
<li><b>Language:</b> Python</li>
<li><b>Libraries:</b> NumPy, PIL</li>
</ul>

---

<h2>📦 Installation & Setup</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/your-username/fruit-freshness-classifier.git
cd fruit-freshness-classifier
</pre>

<h3>2️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>3️⃣ Run Application</h3>

<pre>
streamlit run app.py
</pre>

---

<h2>📊 Model Performance</h2>

<ul>
<li>Achieves high accuracy on validation data</li>
<li>Generalizes well on unseen test images</li>
<li>Uses data augmentation to reduce overfitting</li>
</ul>

---

<h2>📌 Future Improvements</h2>

<ul>
<li>🧠 Add Grad-CAM for model explainability</li>
<li>📱 Improve UI with advanced components</li>
<li>🌐 Deploy on cloud (AWS / Streamlit Cloud)</li>
<li>🍌 Extend to multi-class classification</li>
</ul>

---

<h2>🙌 Author</h2>

<p>
<b>Mukund Shah</b><br>
Aspiring Machine Learning Engineer 🚀
</p>

---

<h2>⭐ Support</h2>

<p>If you like this project, consider giving it a ⭐ on GitHub!</p>