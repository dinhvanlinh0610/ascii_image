from PIL import Image
import numpy as np

def pixel_to_enhanced_ascii(pixel_value):
    """
    Sử dụng Unicode block elements để tạo độ chi tiết cao hơn
    Mỗi "ký tự" thực tế là 4 sub-pixels (2x2)
    """
    # Unicode block elements cho các mẫu khác nhau
    blocks = [' ', '▀', '▒', '▓', '█']  # Từ trống đến đầy
    
    # Chuyển đổi giá trị pixel (0-255) thành mức độ đậm (0-4)
    # Đảm bảo level không vượt quá chỉ số của blocks
    level = min(int(pixel_value / 51), len(blocks) - 1)
    return blocks[level]

def image_to_enhanced_ascii(image_path, output_path=None, width=100, contrast=1.5):
    """
    Chuyển đổi ảnh thành Enhanced ASCII art sử dụng Unicode blocks
    """
    try:
        # Đọc ảnh
        image = Image.open(image_path)
        
        # Điều chỉnh độ tương phản
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
        
        # Chuyển sang ảnh xám
        image = image.convert('L')
        
        # Thay đổi kích thước
        # Nhân đôi width vì mỗi block chiếm ít không gian hơn ký tự ASCII thông thường
        width = width * 2
        ratio = image.size[1] / image.size[0]
        height = int(width * ratio * 0.5)  # Điều chỉnh tỷ lệ cho phù hợp với terminal
        image = image.resize((width, height))
        
        # Chuyển đổi pixels thành enhanced ASCII
        pixels = image.getdata()
        ascii_str = ''
        for i, pixel in enumerate(pixels):
            ascii_str += pixel_to_enhanced_ascii(pixel)
            if (i + 1) % width == 0:
                ascii_str += '\n'
        
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