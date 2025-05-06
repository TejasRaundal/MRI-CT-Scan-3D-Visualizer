# 🧠 MRI/CT Scan 3D Visualizer

This project is a Streamlit-based web application that processes DICOM images from CT or MRI scans, performs preprocessing and segmentation using SciPy, and visualizes them in both 2D and interactive 3D using Matplotlib and Plotly. Designed to aid medical imaging research and analysis, this tool is ideal for quick visualization of scan data.

## 🚀 Features

- ✅ Upload and preview DICOM files  
- 🧼 Image preprocessing: normalization, noise reduction, etc.  
- ✂️ Threshold-based segmentation for tissue isolation  
- 📊 2D visualization with custom colormaps  
- 🌐 3D volume rendering using Plotly  
- 🎚 Adjustable parameters for transparency (alpha), threshold, and color maps  

## 📁 Project Structure

```

MRI-CT-Scan-3D-Visualizer/
├── streamlit_app.py            # Main Streamlit interface
├── src/
│   ├── loader.py               # DICOM loading logic
│   ├── preprocessing.py         # Image preprocessing functions
│   ├── utils.py                # Utilities
│   └── visualizer.py           # 2D and 3D rendering functions
├── requirements.txt            # Python dependencies
└── README.md

````

## 🧠 Technologies Used

- **Python 3.8+**  
- **Streamlit** – Web interface
- **Matplotlib** – 2D and 3D visualizations  
- **Plotly** – 3D visualizations  
- **Pydicom** – DICOM image parsing  
- **NumPy / SciPy** – Image processing  

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/mri-ct-scan-3d-visualizer.git
cd mri-ct-scan-3d-visualizer
````

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app:**

```bash
streamlit run streamlit_app.py
```

## 🖼 Preview

*Coming soon*

## 🧪 Example Use Cases

* Medical students studying anatomy via CT/MRI scans
* Radiologists for preliminary scan previews
* Research projects that require rapid visual analysis

## 📄 License

This project is open-source and available under the **MIT License**.

## 🤝 Contributors

* Tejas Yadav Raundal
* Nikhil Dattatraya Kale
* Shubham Devidas Kadam
* Vivek Dnyaneshwar Shinde
