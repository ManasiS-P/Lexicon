import cv2
import numpy as np

# Load image and check if image loaded correctly
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not loaded. Check file path.")
    exit()

# Image shape
print("Image shape:", image.shape)

# 1)  What do the three values in the shape represent?
# --> The three values represent: (height, width, number of color channels)

# 2)  Which value corresponds to height? width? channels?
# --> shape[0] = height (rows), shape[1] = width (columns), shape[2] = channels (color channels)

print("Data type:", image.dtype)
# 3)  What is the data type of the image array?
# --> uint8 
# Access and Modify Pixels

pixel = image[100, 100]
print("Original pixel value:", pixel)

# 4)  In what order are color values stored in OpenCV?
# --> BGR order (Blue, Green, Red), NOT RGB

# Modifying pixel to new color (Blue)
image[100, 100] = [255, 0, 0]
print("Modified pixel value:", image[100, 100])

# 5)  What happens when you set all values to maximum?
# --> The pixel becomes white

# 6)  What happens when you set all values to zero?
# --> The pixel becomes black

# Show image
cv2.imshow("Modified Pixel Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Modify a Region of the Image
image[100:200, 100:300] = [0, 255, 0]  # Green region

# Results
cv2.imshow("Modified Region Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7)  How does slicing work in NumPy for images?
# --> Format is: image[row_start:row_end, col_start:col_end]
# It selects a rectangular region

# 8)  What do the row and column ranges represent?
# --> Rows = height (vertical position), Columns = width (horizontal position)