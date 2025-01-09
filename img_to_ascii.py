from PIL import Image
from utils import resize_image, pixel_to_ascii

def adjust_contrast(image, factor=1.5):
    """Điều chỉnh độ tương phản của ảnh"""
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def image_to_ascii(image_path, output_path=None, width=100, keep_size=False, 
                  contrast=1.5, mode='simple'):
    """
    Chuyển đổi ảnh thành ASCII art
    """
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Lỗi khi mở file ảnh: {e}")
        return

    # Điều chỉnh độ tương phản
    image = adjust_contrast(image, contrast)
    
    # Chuyển sang ảnh xám
    image = image.convert('L')
    
    # Thay đổi kích thước
    if not keep_size:
        image = resize_image(image, width)  # Bỏ tham số scale
    else:
        width = image.size[0]
    
    # Chuyển đổi pixels thành ASCII
    pixels = image.getdata()
    ascii_str = ''
    for i, pixel in enumerate(pixels):
        ascii_str += pixel_to_ascii(pixel, mode)
        if (i + 1) % width == 0:
            ascii_str += '\n'
    
    # Lưu hoặc in kết quả
    if output_path:
        with open(output_path, 'w') as f:
            f.write(ascii_str)
    else:
        print(ascii_str)
    
    return ascii_str
