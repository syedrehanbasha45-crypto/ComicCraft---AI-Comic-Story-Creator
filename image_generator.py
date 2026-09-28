import os, re
from PIL import Image, ImageDraw, ImageFont

def generate_image(prompt, art_style):
    # Beginner-safe fallback image generator.
    # Replace this function later with Hugging Face Diffusers when your token/model setup is ready.
    os.makedirs("app/static/panels", exist_ok=True)
    safe = re.sub(r"[^a-zA-Z0-9]+", "_", prompt)[:50].strip("_") or "panel"
    path = f"app/static/panels/{safe}.png"

    img = Image.new("RGB", (900, 550), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((20,20,880,530), outline="black", width=4)
    draw.text((45,60), "ComicCraft Panel", fill="black")
    draw.text((45,130), f"Style: {art_style}", fill="black")
    draw.text((45,190), prompt[:100], fill="black")
    draw.text((45,450), "AI image placeholder - enable Stable Diffusion later", fill="black")
    img.save(path)
    return "/static/panels/" + os.path.basename(path)
