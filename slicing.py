def get_dense_patches(image, patch_size = 16, sample_rate = 8):
    """Gets patches of pixels from an array

    This uses the view_as_windows function from scikit-image.

    Parameters
    ----------
    image: ndarray
        Image to find dense patches within.
    patch_size: int (default: 8)
        Size of each patch. 8 x 8 patches are recommended.
    sample_rate: int (default: 4)
        How many pixels apart each patch should be chosen in both x and y
        directions.

    Returns
    -------
    out: ndarray
        An array of which the rows make up a ravel of each dense patch.
    """

    window_shape = (patch_size, patch_size)
    patches = view_as_windows(image, window_shape = window_shape,
                                    step = sample_rate)

    shp = patches.shape
    # Resize the array so that each row is one dense patch.
    out = np.reshape(patches, (shp[0]*shp[1], shp[2]*shp[3]))

    # Normalize the data
    m = out.mean(axis = 1)

    # Have to transpose as it won't take subtract along columns properly
    out = (np.transpose(out) - m).transpose()

    # Make unit length along the rows
    out = normalize(out, axis = 1)

    return out