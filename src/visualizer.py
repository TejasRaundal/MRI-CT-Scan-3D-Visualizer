import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from skimage.transform import resize

def show_sagittal_slice(volume, index, cmap='gray'):
    """Show only sagittal slice."""
    slice_ = volume[:, :, index]
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(slice_.T, cmap=cmap, origin='lower')
    ax.axis('off')
    ax.set_title(f"Sagittal Slice {index}")
    return fig

def plotly_3d_volume(volume, alpha=0.6, cmap='gray', threshold=0.1, max_dim=64):
    """3D volume rendering with Plotly"""
    vol = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))

    if max(vol.shape) > max_dim:
        scale = max_dim / max(vol.shape)
        vol = resize(vol, output_shape=tuple(int(s * scale) for s in vol.shape), anti_aliasing=True)

    z, y, x = np.where(vol > threshold)
    values = vol[z, y, x]

    if len(values) == 0:
        return go.Figure()

    fig = go.Figure(data=go.Volume(
        x=x, y=y, z=z,
        value=values,
        opacity=alpha,
        surface_count=15,
        colorscale=cmap,
    ))

    fig.update_layout(
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(t=10, l=10, b=10, r=10),
        width=800,
        height=800
    )
    return fig