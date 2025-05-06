import nibabel as nib
import pydicom
import os
import numpy as np

def load_nifti(file_path):
    img = nib.load(file_path)
    return img.get_fdata()

def load_dicom(directory):
    slices = [pydicom.dcmread(os.path.join(directory, f)) for f in os.listdir(directory) if f.endswith('.dcm')]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    volume = np.stack([s.pixel_array for s in slices], axis=-1)
    return volume.astype(np.float32)
