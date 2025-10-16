from PIL import Image, ImageColor

def recolor_png(src_path, dst_path, hex_color="#FF3B30", alpha_threshold=1):
    """
    Recolors all non-transparent pixels to `hex_color`, preserving original alpha.
    alpha_threshold: treat pixels with alpha <= threshold as transparent.
    """
    img = Image.open(src_path).convert("RGBA")
    r, g, b, a = img.split()

    # Binary mask of where we consider pixels "painted"
    mask = a.point(lambda x: 255 if x > alpha_threshold else 0, mode="L")

    # A solid image in the new color
    new_rgb = ImageColor.getrgb(hex_color)
    solid = Image.new("RGBA", img.size, new_rgb + (255,))

    # Composite: put solid color wherever mask is set
    colored = Image.new("RGBA", img.size, (0, 0, 0, 0))
    colored.paste(solid, mask=mask)

    # Keep the *original* alpha (soft edges, antialiasing)
    colored.putalpha(a)
    colored.save(dst_path)

# Example
recolor_png("/Users/benedikthoward/Documents/Portfolio 2.0/media/other/ubcrocket_logo_white_long.png", "/Users/benedikthoward/Documents/Portfolio 2.0/media/other/rocket_logo.png", hex_color="#012460")
print("done")