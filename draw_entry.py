#!/usr/bin/env python3
"""Generate entry.png for the catballdev news-image entry."""

from PIL import Image, ImageDraw

# Create a simple news-style image
width, height = 800, 600
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Draw masthead "THE DAILY GLOBE"
draw.rectangle([0, 0, width, 80], fill='#2c3e50')
draw.text((40, 20), "THE DAILY GLOBE", fill='white', font=None, size=36)

# Draw date "FRIDAY 27 NOVEMBER 2026"
draw.text((40, 55), "FRIDAY 27 NOVEMBER 2026", fill='white', font=None, size=16)

# Draw news content area
draw.rectangle([0, 80, width, 500], fill='#ecf0f1')

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

y_pos = 120
for headline in headlines:
    draw.text((40, y_pos), headline, fill='#2c3e50', font=None, size=16)
    y_pos += 30

# Draw footer
draw.rectangle([0, 500, width, 600], fill='#34495e')
draw.text((40, 530), "catballdev News Image Entry", fill='white', font=None, size=14)

# Save the image
img.save('entry.png')
print("Created entry.png")