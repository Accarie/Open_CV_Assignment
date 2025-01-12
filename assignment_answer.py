import cv2

image = cv2.imread('assignment-001-given.jpg')
bg_rec = image.copy()
cv2.rectangle(bg_rec, (800,80), (1260, 189), (0,0,0), -1)
image = cv2.addWeighted(bg_rec, 0.5, image, 0.5, 0)
cv2.rectangle(image, (260, 192), (992, 921), (0, 255, 0), 8)
cv2.putText(image, 'RAH972U', (803,165), cv2.FONT_HERSHEY_SIMPLEX, 3.2, (0, 255, 0), 7)
# Display the image in a new window named 'Image'
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite('assignment_result.jpg', image)
cv2.destroyAllWindows()