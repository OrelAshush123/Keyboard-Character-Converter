import base64

with open("icon.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

with open("encoded_string.txt", "w") as f:
    f.write(encoded_string)