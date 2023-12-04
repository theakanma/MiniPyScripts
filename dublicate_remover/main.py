import os
from PIL import Image
from skimage.metrics import structural_similarity as ssim

def compare_images(image1_path, image2_path):
    # Open images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Convert images to grayscale
    image1_gray = image1.convert("L")
    image2_gray = image2.convert("L")

    # Calculate structural similarity
    similarity_index, _ = ssim(image1_gray, image2_gray, full=True)

    return similarity_index

def find_and_remove_duplicates(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate through each pair of files
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            file1_path = os.path.join(folder_path, files[i])
            file2_path = os.path.join(folder_path, files[j])

            # Check if both files are images
            if file1_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and \
               file2_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                
                # Compare images
                similarity = compare_images(file1_path, file2_path)

                # If similarity is high, consider them duplicates and remove one
                if similarity > 0.95:  # You can adjust the threshold as needed
                    print(f"Removing duplicate: {files[i]} and {files[j]}")
                    os.remove(file2_path)

if __name__ == "__main__":
    folder_path = "path/to/your/folder"
    find_and_remove_duplicates(folder_path)
