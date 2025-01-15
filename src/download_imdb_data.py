import os
import requests

DATASET_URL = "https://datasets.imdbws.com/title.basics.tsv.gz"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../data")
OUTPUT_FILE = "title.basics.tsv.gz"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_dataset():
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    response = requests.get(DATASET_URL, stream=True)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Dataset downloaded successfully: {output_path}")
    else:
        print(f"Failed to download dataset. Status code: {response.status_code}")

if __name__ == "__main__":
    download_dataset()
