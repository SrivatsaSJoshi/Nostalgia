import os
import argparse
import hashlib
import csv

def get_file_hash(file_path):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_images(root_dir, index_file, output_csv):
    """Recursively search for duplicate images in a directory."""
    image_hashes = {}
    duplicates = []

    with open(index_file, 'w') as index:
        index_writer = csv.writer(index)
        index_writer.writerow(["Hash", "Path"])

        for root, _, files in os.walk(root_dir):
            print(f"Processing directory: {root}")  # Debug statement
            for filename in files:
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    file_path = os.path.join(root, filename)
                    file_hash = get_file_hash(file_path)
                    index_writer.writerow([file_hash, file_path])

                    if file_hash in image_hashes:
                        duplicates.append((file_path, image_hashes[file_hash]))
                    else:
                        image_hashes[file_hash] = file_path

    with open(output_csv, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Original", "Duplicate"])

        for original, duplicate in duplicates:
            csv_writer.writerow([original, duplicate])

def main():
    parser = argparse.ArgumentParser(description="Find and report duplicate images.")
    parser.add_argument("-d", "--directory", required=True, help="Path to the directory containing images")
    args = parser.parse_args()

    big_directory = args.directory
    index_file = "image_index.csv"
    output_csv = "duplicate_images.csv"
    
    find_duplicate_images(big_directory, index_file, output_csv)

if __name__ == "__main__":
    main()

