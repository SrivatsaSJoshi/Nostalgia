import os

def get_file_type(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower()

def calculate_directory_size(directory):
    total_size = 0
    file_type_sizes = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size

            file_type = get_file_type(file)
            if file_type in file_type_sizes:
                file_type_sizes[file_type] += file_size
            else:
                file_type_sizes[file_type] = file_size

    return total_size, file_type_sizes

def main():
    directory = input("Enter the directory path: ")
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    total_size, file_type_sizes = calculate_directory_size(directory)

    print(f"Total directory size: {total_size / (1024 ** 3):.2f} GB")

    print("\nFile type sizes:")
    for file_type, size in file_type_sizes.items():
        print(f"{file_type}: {size / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    main()
