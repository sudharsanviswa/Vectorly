import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
    print(input_image.shape)
    for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            if (np.sum(input_image[i][j])>20):
                output[i][j][0]=255
                output[i][j][1]=255
                output[i][j][2]=255
    # Write your code here for output
    
    return output

#if __name__ == '__main__':
image = cv2.imread('simpsons_frame0.png')
output = getTextOverlay(image)
cv2.imwrite('simpons_text.png', output)

