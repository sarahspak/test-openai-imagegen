from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
from PIL import Image
import requests
from datetime import datetime

load_dotenv(find_dotenv())

openai_api_key = os.environ.get("OPENAI_API_KEY")

# set environment variable OPENAI_API_KEY to your key
os.environ["OPENAI_API_KEY"] = openai_api_key
client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="Image of organic bacterial growth texture, that tiles horizontally and fades into a small dot pattern at the top and bottom",
    size="1024x1024",
    quality="hd",  # one of hd or standard
    style="vivid",
    n=1,
)

image_url = response.data[0].url
print(image_url)
# open and download the image_url
data = requests.get(image_url).content

# Opening a new file named img with extension .jpg
# This file would store the data of the image file
current_dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
f = open(f"{current_dt}_image.jpg", "wb")

# Storing the image data inside the data variable to the file
f.write(data)
f.close()

# Opening the saved image and displaying it
img = Image.open(f"{current_dt}_image.jpg")
img.show()
