import cv2
import matplotlib.pyplot as plt

image_path='example.jpg'
image=cv2.imread(image_path)

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height,width,_=image_rgb.shape

rec1_width,rec1_height=100,100
top_left1=(20,20)
bottom_right1=(top_left1[0]+rec1_width,top_left1[1]+rec1_height)
cv2.rectangle(image_rgb,top_left1,bottom_right1,(0,255,255),3)

rec2_width,rec2_height=100,100
top_left2=(width -rec2_width-20,height-rec2_height-20)
bottom_right2=(top_left2[0]+rec1_width,top_left2[1]+rec1_height)
cv2.rectangle(image_rgb,top_left2,bottom_right2,(255,0,255),3)

center1_x=top_left1[0]+rec1_width//2
center1_y=top_left1[1]+rec1_height//2  
center2_x=top_left2[0]+rec2_width//2
center2_y=top_left2[1]+rec2_height//2
cv2.circle(image_rgb,(center1_x,center1_y),15,(0,0,255),-1)
cv2.circle(image_rgb,(center2_x,center2_y),15,(0,0,255),-1)
  
cv2.line(image_rgb,(center1_x,center1_y),(center2_x,center2_y),(255,0,0),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,'Region 1',(top_left1[0],top_left1[1]-10),font,0.5,(0,255,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Region 2',(top_left2[0],top_left2[1]-10),font,0.5,(255,0,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Center 1',(center1_x-30,center1_y-10),font,0.5,(0,0,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Center 2',(center2_x-30,center2_y-10),font,0.5,(0,0,255),2,cv2.LINE_AA)

arrow_start=(width-50,20)
arrow_end=(width-50,height-20)

cv2.arrowedLine(image_rgb,arrow_start,arrow_end,(0,255,0),3)
cv2.arrowedLine(image_rgb,arrow_end,arrow_start,(0,255,0),3)

height_label_position=(arrow_start[0]-150,(arrow_start[1]+arrow_end[1])//2)
cv2.putText(image_rgb,f'Height:{height}px',height_label_position,font,0.5,(0,255,0),2,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(image_rgb)
plt.title('Image with Annotations')
plt.axis('off')
plt.show()