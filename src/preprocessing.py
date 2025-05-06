import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.exposure import rescale_intensity

def preprocess_volume(volume, sigma=1):
    # Normalize the volume to [0, 1] range
    volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))
    
    # Apply Gaussian filter
    volume = gaussian_filter(volume, sigma=sigma)
    
    # Rescale intensity to ensure values are within the range [0, 1]
    volume = rescale_intensity(volume, in_range='image', out_range=(0, 1))
    
    return volume
