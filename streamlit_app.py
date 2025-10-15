from src.loader import load_nifti, load_dicom
from src.preprocessing import preprocess_volume
from src.visualizer import show_sagittal_slice, plotly_3d_volume
import streamlit as st
import tempfile
import os
import zipfile

st.set_page_config(page_title="MedScan 3D", layout="wide")
st.title("🧠 MedScan 3D: MRI/CT Scan Visualizer")

file_type = st.radio("Choose scan type", ["NIfTI (.nii/.nii.gz)", "DICOM Folder"])
alpha = st.slider("3D Transparency", 0.0, 1.0, 0.6, step=0.05)
cmap = st.selectbox("Colormap", ["Gray", "Viridis", "Hot", "Jet", "Cividis",  "Magma", "Inferno"])
threshold = st.slider("3D Intensity Threshold", 0.0, 1.0, 0.1, step=0.01)

volume = None
if file_type == "NIfTI (.nii/.nii.gz)":
    nifti_file = st.file_uploader("Upload NIfTI file", type=["nii", "nii.gz"])
    if nifti_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".nii.gz") as tmp:
            tmp.write(nifti_file.read())
            volume = load_nifti(tmp.name)
else:
    dicom_zip = st.file_uploader("Upload DICOM folder (zipped)", type=["zip"])
    if dicom_zip:
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, "dicom.zip")
            with open(zip_path, "wb") as f:
                f.write(dicom_zip.read())
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)
            volume = load_dicom(tmpdir)

if volume is not None:
    st.success("Scan loaded successfully!")

    st.subheader("Gaussian smoothing filter")
    sigma = st.slider("Filter sigma", 0.1, 5.0, 1.0, step=0.1) 
    processed = preprocess_volume(volume, sigma=sigma)

    # Only sagittal view
    st.subheader("📖 Sagittal Slice Viewer")
    sagittal_index = st.slider("Select sagittal slice", 0, processed.shape[2] - 1, processed.shape[2] // 2)
    fig2d = show_sagittal_slice(processed, sagittal_index, cmap=cmap.lower())
    st.pyplot(fig2d)

    # 3D Viewer
    st.subheader("🧊 3D Volume Viewer")
    fig3d = plotly_3d_volume(processed, alpha=alpha, cmap=cmap.lower(), threshold=threshold)
    st.plotly_chart(fig3d, use_container_width=True)
