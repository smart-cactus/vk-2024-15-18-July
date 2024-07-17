from PIL import Image, ImageDraw, ImageFont

def create_vk_logo():
    width, height = 200, 200

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    vk_blue = (74, 118, 168)

    rect_x0, rect_y0 = 20, 50
    rect_x1, rect_y1 = 180, 150

    draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill=vk_blue)

    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except IOError:
        font = ImageFont.load_default()

    text = "VK"

    # Используем textbbox для получения координат текста
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # ширина
    text_height = text_bbox[3] - text_bbox[1]  # высота

    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    draw.text((text_x, text_y), text, fill="white", font=font)

    image.save("vk_logo.png")

create_vk_logo()

