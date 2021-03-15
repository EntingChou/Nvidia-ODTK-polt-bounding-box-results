import json 
import cv2
 
# Opening JSON file 
print("Your inferred JSON path")
f = open(input())

print('Your inferred images path')
image_path = input()
# returns JSON object as  
# a dictionary 
data = json.load(f) 
   
# Iterating through the json 
# list 
x = int(0)
for i in data['annotations']: 
    image_id = i['image_id']
    score = i['score']
    category_id = i['category_id']
    x, y, w, h  = i['bbox']       
    
    fname = image_path+'/'+str(image_id)+'.png'
    img = cv2.imread(fname)
    
    cv2.rectangle(img, (int(x),int(y)), (int(x)+int(w),int(y)+int(h)), (0,255,0), 4)
    # 标注文本
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(score)+'|'+str(category_id)
    cv2.putText(img, text, (212, 310), font, 1, (0,255,255), 1, cv2.LINE_AA)

    cv2.imwrite('pic_'+str(x)+'.jpg', img)
    x = x + 1
f.close() 
