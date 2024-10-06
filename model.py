import cv2
from PIL import Image

def overlay_images(user_image_path, garment_image_path, output_path):
    # Load images
    user_image = cv2.imread(user_image_path)
    garment_image = cv2.imread(garment_image_path)

    if user_image is None:
        print("Error loading user image.")
        return
    if garment_image is None:
        print("Error loading garment image.")
        return

    # Resize garment image to fit (you can adjust the dimensions as needed)
    garment_resized = cv2.resize(garment_image, (user_image.shape[1] // 2, user_image.shape[0] // 2))

    # Define position to overlay garment (you can adjust this)
    x_offset = 50
    y_offset = 50

    # Overlay the garment on the user image
    user_image[y_offset:y_offset + garment_resized.shape[0], x_offset:x_offset + garment_resized.shape[1]] = garment_resized

    # Save the result
    cv2.imwrite(output_path, user_image)

if __name__ == "__main__":
    overlay_images('./images/user_image.jpg', './images/garment_image.jpg', './outputs/output_image.jpg')
