import cv2

source = "mohit.jpg"
destination = "newImages.png"
src = cv2.imread(source,cv2.IMREAD_UNCHANGED)

# Percent by which the image is resized
scale_percent = 50

# Calculate the 50 percent of original dimensions
# existing width ki jo bhi percent hai yeh usko naya with bana do.
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
# wait till any key is pressed on keyboard.
# cv2.waitKey(0)
