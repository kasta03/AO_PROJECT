import cv2

image = cv2.imread("shapes.png")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, bin_image = cv2.threshold(grey_image, 225, 255, cv2.THRESH_BINARY)

contours, relation = cv2.findContours(bin_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    if i == 0:
        continue
    approx_factor = 0.02
    approx = cv2.approxPolyDP(contour, approx_factor * cv2.arcLength(contour, True), True)
    
    x, y, w, h = cv2.boundingRect(approx)
    x = int(x + w//3)
    y = int(y + h//1.5)
    boundaries = (x, y)

    cv2.drawContours(image, contour, 0, (0, 0, 0), 1)
    if len(approx) == 3:
        cv2.putText(image, "Triangle", boundaries, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)
    elif len(approx) == 4:
        cv2.putText(image,  "Rectangle", boundaries, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", boundaries, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)
    elif len(approx) == 6:
        cv2.putText(image, "Hexagon", boundaries, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)
    elif len(approx) == 7:
        cv2.putText(image, "Heptagon", boundaries, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)
        
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()