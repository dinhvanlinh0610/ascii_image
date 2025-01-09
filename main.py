import argparse
from img_to_ascii import image_to_ascii
from video_to_ascii import video_to_ascii
from color_ascii import ColorAscii
from enhanced_ascii import image_to_enhanced_ascii

def main():
    parser = argparse.ArgumentParser(description='Chuyển đổi ảnh/video thành ASCII art')
    parser.add_argument('--input', required=True, help='Đường dẫn file đầu vào (ảnh/video)')
    parser.add_argument('--type', choices=['image', 'video'], required=True, help='Loại file đầu vào')
    parser.add_argument('--output', help='Đường dẫn file đầu ra (tùy chọn)')
    parser.add_argument('--width', type=int, default=100, help='Chiều rộng của ASCII art')
    parser.add_argument('--keep-size', action='store_true', help='Giữ nguyên kích thước ảnh gốc')
    parser.add_argument('--contrast', type=float, default=1.5, help='Điều chỉnh độ tương phản (mặc định: 1.5)')
    parser.add_argument('--mode', choices=['simple', 'complex', 'enhanced'], default='simple', 
                       help='Chế độ ASCII (simple/complex/enhanced)')
    parser.add_argument('--color', action='store_true', help='Tạo ASCII art có màu')
    
    args = parser.parse_args()
    
    if args.type == 'image':
        if args.mode == 'enhanced':
            image_to_enhanced_ascii(args.input, args.output, args.width, args.contrast)
        elif args.color:
            color_ascii = ColorAscii()
            color_ascii.image_to_color_ascii(args.input, args.output, args.width, 
                                          args.keep_size, args.contrast, args.mode)
        else:
            image_to_ascii(args.input, args.output, args.width, 
                         args.keep_size, args.contrast, args.mode)
    else:
        video_to_ascii(args.input, args.output, args.width, args.mode)

if __name__ == "__main__":
    main() 