from PIL import Image
import base64
# Open the image file
with open("./Barack-Obama-2012.webp", "rb") as f:
    encoded_image = base64.b64encode(f.read())
# Save the encoded image to a file
with open("image.txt", "w") as f:
    f.write(encoded_image.decode("utf-8"))