# Duplicate Image Remover
This Python script is designed to find and remove duplicate images
 within a specified folder. It uses the structural similarity index (SSI)
 to compare images and removes one of the duplicates if the similarity is above a certain threshold.

## Requirements
Python (3.x)
Pillow
scikit-image
You can install the required packages using the following command:

```bash
pip install Pillow 
pip install scikit-image
```

## Usage
Clone the repository or download the script (remove_duplicates.py).
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script with the following command:
```bash
python main.py
```
Make sure to replace "path/to/your/folder" in the script with the path to the folder where you want to remove duplicate images.

## Important Note
The script uses a default structural similarity threshold of 0.95. You can adjust this threshold in the script based on your needs.
