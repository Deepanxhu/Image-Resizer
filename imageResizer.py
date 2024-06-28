import cv2

# Configurable Parameters
source = "thankyou.png"
destination = "newImage.png"
scale_percentage = 50

src = cv2.imread(source , cv2.IMREAD_UNCHANGED)

# Calculate the 50 percentage of original dimension
new_width = int(src.shape[1]*scale_percentage/100)
new_height = int(src.shape[0]*scale_percentage/100)
                 
# Resize image
output = cv2.resize(src , (new_width , new_height))

cv2.imwrite(destination , output)
cv2.waitKey(0)