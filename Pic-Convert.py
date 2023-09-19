import pyimgur

CLIENT_ID = "30e0a5d81af9c08"

def upload_image_to_imgur(image_path):
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(image_path, title="Uploaded with PyImgur")
    return uploaded_image.link

# Replace 'your_image_path_here.jpg' with the path to the image you want to upload.
image_path = "/Users/admin/Downloads/MicrosoftTeams-image.png"
image_link = upload_image_to_imgur(image_path)
print(f"Your image link: {image_link}")
