from converter import convert_image

import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: conv-cli <image> <format>")
    print("Eg: conv-cli mbdtf.png jpg")
    print("Please try again.")

    sys.exit(1)

image = Path(sys.argv[1])
format = sys.argv[2]

output = image.with_suffix("." + format)

convert_image(image, output)

print("Done!")