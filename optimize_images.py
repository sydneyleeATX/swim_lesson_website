import os
import requests
from pathlib import Path

def optimize_image(image_path):
    try:
        # TinyPNG API key
        api_key = "rjlJhWmDhK83n2ZGK7NNLM25mW0PGD9D"
        
        # Read the image file
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        
        # Send to TinyPNG API
        headers = {
            'Authorization': f'Basic {api_key}'
        }
        
        response = requests.post(
            'https://api.tinify.com/shrink',
            headers=headers,
            data=image_data
        )
        
        if response.status_code == 201:
            # Save optimized image
            optimized_path = image_path.with_suffix('.webp')
            with open(optimized_path, 'wb') as optimized_file:
                optimized_file.write(response.content)
            print(f"Optimized {image_path} successfully")
            return True
        else:
            print(f"Failed to optimize {image_path}")
            return False
    except Exception as e:
        print(f"Error optimizing {image_path}: {str(e)}")
        return False

def main():
    # Get all image files in the directory
    image_extensions = ['.jpg', '.jpeg', '.png']
    image_dir = Path(__file__).parent
    
    for file in image_dir.iterdir():
        if file.suffix.lower() in image_extensions:
            optimize_image(file)

if __name__ == "__main__":
    main()
