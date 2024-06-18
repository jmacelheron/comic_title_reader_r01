import base64
import requests
import os
import csv

# OpenAI API Key
# Load variables from .env file

with open('.env', 'r') as f:
    for line in f:
        if line.strip():
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

# OpenAI API Key
api_key = os.getenv("API_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
image_directory = 'imageTest/'
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(image_directory, filename)
        base64_image = encode_image(image_path)

        headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {api_key}"
        }

        payload = {
          "model": "gpt-4o",
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Identify the comic in this image by title and the issue number. I need this in a csv format strictly with no other commentary from you.```"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                  }
                }
              ]
            }
          ],
          "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        print(response.json())
        # csv = response.json()['choices'][0]['message']['content']
        # print(csv)

        content = response.json()
        content = content['choices'][0]['message']['content']

        # Clean data
        content = content.replace('```csv\n', '').replace('\n```', '')
        content = f'original Titile,{content},{filename}'
        lines = content.split('\n')
        title = ''
        edition = ''

        if len(lines) > 1:
            title_parts = lines[1].split(',')
            if len(title_parts) > 0:
                title = title_parts[0]
            else:
                title = None

            if len(title_parts) > 1:
                edition = title_parts[1]
            else:
                edition = None

        # open a CSV file to write to
        with open(f'processed/csvs/{title}_{edition}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                # split each line into fields and write it to the CSV file
                writer.writerow(line.split(','))

        # Rename the file
        name, extension = os.path.splitext(f'imageTest/{filename}')
        os.rename(f'imageTest/{filename}', f'processed/images/{title}_{edition}{extension}')
