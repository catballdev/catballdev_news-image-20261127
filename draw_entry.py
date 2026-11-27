#!/usr/bin/env python3
"""Generate entry.png for the catballdev news-image entry."""

from PIL import Image, ImageDraw

# Create a simple news-style image
width, height = 800, 600
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Draw masthead "THE DAILY GLOBE"
draw.rectangle([0, 0, width, 85], fill='#2c3e50')
draw.text((40, 20), "THE DAILY GLOBE", fill='white', font=None, size=36)

# Draw date "FRIDAY 27 NOVEMBER 2026"
draw.text((40, 60), "FRIDAY 27 NOVEMBER 2026", fill='white', font=None, size=16)

# Draw news content area
draw.rectangle([0, 85, width, 500], fill='#ecf0f1')

# Draw eight headlines
headlines = [
    "Cairo tanker fire lead story",
    "Kim Jong Un",
    "Thanksgiving storm",
    "SpaceX satellites",
    "Zelenskyy",
    "Indonesia gold mine",
    "Pope Leo XIV",
    "Hong Kong fire anniversary"
]

y_pos = 115
for headline in headlines:
    draw.text((40, y_pos), headline, fill='#2c3e50', font=None, size=16)
    y_pos += 36

# Draw footer
draw.rectangle([0, 500, width, 600], fill='#34495e')
# Thin rule above footer content
draw.line([(40, 508), (760, 508)], fill='#555555', width=1)
# Footer text in smaller font
draw.text((40, 518), "FRIDAY 27 NOVEMBER 2026", fill='white', font=None, size=12)
draw.text((40, 535), "catballdev News Image Entry", fill='white', font=None, size=12)

# Save the image
img.save('entry.png')
print("Created entry.png")