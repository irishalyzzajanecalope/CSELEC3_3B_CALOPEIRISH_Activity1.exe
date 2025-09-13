from PIL import Image, ImageDraw, ImageFont

canvas_w, canvas_h = 600, 800
img = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))  # white background
draw = ImageDraw.Draw(img)

main_color = (235, 235, 180)   
base_color = (245, 230, 120)   
text_color = (0, 0, 0)

parallelogram_points = [(180, 150), (380, 100), (340, 600), (200, 600)]

min_x = min(p[0] for p in parallelogram_points)
max_x = max(p[0] for p in parallelogram_points)
min_y = min(p[1] for p in parallelogram_points)
max_y = max(p[1] for p in parallelogram_points)

shape_w = max_x - min_x
shape_h = max_y - min_y

offset_x = (canvas_w - shape_w) // 2 - min_x
offset_y = (canvas_h - shape_h) // 2 - min_y

parallelogram_points = [(x + offset_x, y + offset_y) for x, y in parallelogram_points]
draw.polygon(parallelogram_points, fill=main_color)

draw.rectangle((150+offset_x, 570+offset_y, 415+offset_x, 650+offset_y), fill=base_color)

title_font = ImageFont.truetype("timesbd.ttf", 40)
year_font = ImageFont.truetype("timesbd.ttf", 28)
subtitle_font = ImageFont.truetype("arial.ttf", 19)

text = "INTRAMURALS"
bbox = draw.textbbox((0,0), text, font=subtitle_font)
w = bbox[2] - bbox[0]
draw.text(((canvas_w-w)//2, (canvas_h//2)+150), text, font=subtitle_font, fill=text_color)

text = "2025"
bbox = draw.textbbox((0,0), text, font=year_font)
w = bbox[2] - bbox[0]
draw.text(((canvas_w-w)//2, (canvas_h//2)+175), text, font=year_font, fill=text_color)

text2 = "CHAMPION"
bbox2 = draw.textbbox((0,0), text2, font=title_font)
w2 = bbox2[2] - bbox2[0]
draw.text(((canvas_w-w2)//2, (canvas_h//2)+240), text2, font=title_font, fill=text_color)

logo = Image.open("logo.png")    
logo = logo.resize((200, 200))   
img.paste(logo, (205, 250), logo) 

img.save("award_graphic.png")
img.show()