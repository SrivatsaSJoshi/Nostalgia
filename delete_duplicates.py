import os
import csv

def delete_image(image_path):
    try:
        os.remove(image_path)
        print(f"Deleted: {image_path}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"Error deleting {image_path}: {e}")

def main():
    csv_file = 'duplicate_images.csv'
    
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header

        for row in reader:
            if len(row) >= 2:
                image_path = row[1].strip()
                delete_image(image_path)

if __name__ == "__main__":
    main()
