import cv2
image = cv2.imread('solar-system.jpg')
cv2.putText(image,'Sol',(100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
cv2.putText(image,'Mercurio',(110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Venus',(190,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Terra',(300,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Marte',(400,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Jupiter',(500,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Saturno',(720,110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Urano',(950,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(image,'Netuno',(1080,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))









cv2.imshow('resultado', image)
cv2.waitKey(0)