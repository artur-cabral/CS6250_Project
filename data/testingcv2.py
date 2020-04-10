import numpy as np
import cv2


# Load an color image in grayscale
img = cv2.imread('view1_frontal.jpg', 4)
print(img)

# display the image in a window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save the image processed
#cv2.imwrite('beachgray.jpg', img)
