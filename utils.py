import numpy as np
from PIL import Image

def resize_image(image, new_width=100):
    """Thay đổi kích thước ảnh giữ nguyên tỷ lệ"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.43)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def pixel_to_ascii(pixel_value, mode='simple'):
    """
    Chuyển đổi giá trị pixel (0-255) thành ký tự ASCII
    mode: 
        - 'simple': Sử dụng bộ ký tự đơn giản
        - 'complex': Sử dụng bộ ký tự phức tạp
    """
    if mode == 'simple':
        ascii_chars = '@%#*+=-:. '
    else:
        ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    step = 256 / len(ascii_chars)
    return ascii_chars[int(pixel_value / step)]
