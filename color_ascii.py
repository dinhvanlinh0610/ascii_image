from PIL import Image
from utils import resize_image, pixel_to_ascii
import numpy as np

class ColorAscii:
    def __init__(self):
        # Mã màu ANSI cơ bản
        self.colors = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m'
        }

    def rgb_to_ansi(self, r, g, b):
        """Chuyển đổi màu RGB sang mã ANSI 256 màu"""
        return f'\033[38;2;{r};{g};{b}m'

    def image_to_color_ascii(self, image_path, output_path=None, width=100, keep_size=False, 
                           contrast=1.5, mode='simple', colored=True):
        """
        Chuyển đổi ảnh thành ASCII art có màu
        """
        try:
            # Đọc ảnh
            image = Image.open(image_path)
            
            # Thay đổi kích thước nếu cần
            if not keep_size:
                image = resize_image(image, width)
            else:
                width = image.size[0]

            # Chuyển thành array để dễ xử lý
            img_array = np.array(image)
            height = img_array.shape[0]
            
            # Tạo ảnh xám để lấy ký tự ASCII
            gray_image = image.convert('L')
            gray_pixels = np.array(gray_image)

            # Tạo ASCII art có màu
            ascii_str = ''
            for i in range(height):
                for j in range(width):
                    # Lấy giá trị pixel xám để chọn ký tự ASCII
                    gray_val = gray_pixels[i, j]
                    ascii_char = pixel_to_ascii(gray_val, mode)
                    
                    if colored:
                        # Lấy màu RGB của pixel
                        r, g, b = img_array[i, j]
                        # Thêm mã màu ANSI
                        ascii_str += self.rgb_to_ansi(r, g, b) + ascii_char
                    else:
                        ascii_str += ascii_char
                
                ascii_str += '\n'
            
            # Thêm mã reset màu ở cuối
            if colored:
                ascii_str += self.colors['reset']

            # Xuất kết quả
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(ascii_str)
            else:
                print(ascii_str)

            return ascii_str

        except Exception as e:
            print(f"Lỗi khi xử lý ảnh: {e}")
            return None 