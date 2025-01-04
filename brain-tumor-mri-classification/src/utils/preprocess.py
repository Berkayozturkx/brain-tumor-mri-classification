def preprocess_image(image, target_size=(200, 200)):
    """
    Preprocess the uploaded image for model prediction.

    Parameters:
        image (numpy.ndarray): The input image to preprocess.
        target_size (tuple): The target size for resizing the image.

    Returns:
        numpy.ndarray: The preprocessed image ready for prediction.
    """
    # Resize the image to the target size
    image = cv.resize(image, target_size)
    
    # Normalize the image
    image = image / 255.0
    
    # Expand dimensions to match the input shape of the model
    image = np.expand_dims(image, axis=0)
    
    return image

def load_and_preprocess_image(image_path):
    """
    Load an image from the specified path and preprocess it.

    Parameters:
        image_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The preprocessed image ready for prediction.
    """
    # Load the image using OpenCV
    image = cv.imread(image_path)
    
    # Preprocess the image
    return preprocess_image(image)