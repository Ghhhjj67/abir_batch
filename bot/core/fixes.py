# (c) @AbirHasan2005
from PIL import Image, ImageDraw, ImageFont
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import requests
from io import BytesIO

async def fix_thumbnail(thumb_path: str, height: int = 0):
    if not height:
        metadata = extractMetadata(createParser(thumb_path))
        if metadata.has("height"):
            height = metadata.get("height")
        else:
            height = 0
    Image.open(thumb_path).convert("RGB").save(thumb_path)
    img = Image.open(thumb_path)
    img1=img.resize((320, 180))
    img1.save(thumb_path, "JPEG")
    return thumb_path



async def fix_thumbnail1(thumb_path: str, height1: int = 0):
    if not height1:
        metadata = extractMetadata(createParser(thumb_path))
        if metadata.has("height"):
            height1 = metadata.get("height")
        else:
            height1 = 0
    Image.open(thumb_path).convert("RGB").save(thumb_path)
    img = Image.open(thumb_path)
    width, height = img.size
    left = 6
    top = height / 10
    right = 1
    bottom = 3 * height / 4
    img1=img.crop((0, 0, width, height-28))
    img1.save(thumb_path, "JPEG")
    img_resi = Image.open(thumb_path)
    img_resi1=img_resi.resize((320,180),Image.ANTIALIAS)
    img_resi1.save(thumb_path,"JPEG")
    # img_edit=Image.open(thumb_path)
    # draw = ImageDraw.Draw(img_edit)
    # req = requests.get("https://github.com/yogeshmirro/font/blob/main/ShortBaby-Mg2w.ttf?raw=true")
    # myFont = ImageFont.truetype(BytesIO(req.content), 20)
    # draw.text((width/2, height-60), "@seaofallmovies",fill =(255, 0, 0),font=myFont)
    # img_edit.save(thumb_path,"JPEG")
    return thumb_path
