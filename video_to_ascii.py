import cv2
from PIL import Image
import numpy as np
from img_to_ascii import image_to_ascii
import time
import os

def video_to_ascii(video_path, output_path=None, width=100):
    """
    Quy trình xử lý:
    1. Đọc video frame-by-frame bằng OpenCV
    2. Chuyển mỗi frame thành ảnh PIL
    3. Chuyển frame thành ASCII art
    4. Xóa màn hình và hiển thị frame mới
    5. Tạm dừng để tạo animation
    """
    try:
        cap = cv2.VideoCapture(video_path)
        os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Chuyển frame thành PIL Image
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame)
            
            # Chuyển thành ASCII và in
            ascii_frame = image_to_ascii(pil_image, width=width)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)
            
            # Tạm dừng để tạo hiệu ứng animation
            time.sleep(0.1)
            
        cap.release()
        
    except Exception as e:
        print(f"Lỗi khi xử lý video: {e}")
