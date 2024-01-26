from PIL import Image
import requests as req
from dotenv import load_dotenv
import os
import json


load_dotenv()

def compress_image(input_path, output_path, quality = 85):
  with Image.open(input_path) as img:
    img.save(output_path, 'JPEG', quality=quality)    

def generate_image(prompt):
  url = os.environ["RUNPOD_ENDPOINT"]
  
  headers = {
    'Authorization' : os.environ["RUNPOD_TOKEN"],
    'Accept' : "application/json"
  }
  
  data = {
    "input": {
      "prompt": prompt,
      "height": 512,
      "width": 512,
      "num_outputs": 1,
      "num_inference_steps": 50,
      "guidance_scale": 7.5,
      "scheduler": "KLMS"
    }
  }
  
  res = req.post(url, headers=headers, data=json.dumps(data))
  
  imageData = res.json()['output'][0]['image']

  return imageData
