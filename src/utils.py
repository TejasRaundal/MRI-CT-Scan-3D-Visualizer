def normalize(volume):
    return (volume - volume.min()) / (volume.max() - volume.min())