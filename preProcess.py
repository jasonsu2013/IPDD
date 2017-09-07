#coding=utf-8
import cv2
import os




def imGray(filePath):
      
      im = cv2.imread(filePath)  #读取图片
      im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
      #cv2.axis("off")
      #cv2.title("Input Image")
      
      cv2.imshow('gray',im_gray)  #显示图片
      cv2.waitKey(0) 
      cv2.destroyAllWindows()
      return im_gray
def imBinary(im_gray):
    
     retval, im_at_fixed = cv2.threshold(im_gray,199, 255, cv2.THRESH_BINARY) 
         #将阈值设置为123，阈值类型为cv2.THRESH_BINARY，则灰度在大于123的像素其值将设置为255，其它像素设置为0
     #cv2.axis("off") 
     #cv2.title("Fixed Thresholding")
     cv2.imshow('binary',im_at_fixed) 
     cv2.waitKey(0) 
     cv2.destroyAllWindows()
     return im_at_fixed
def main():
    base_dir = "C:\Users\i073072\Downloads\OCR"
             #path_test_image = os.path.join(base_dir, "test_data.png")  
    path_test_image = os.path.join(base_dir, "fapiao1.jpg")
    
    im_gray = imGray(path_test_image)
    
    im_bin = imBinary(im_gray)
     
if __name__ == '__main__':
    main()