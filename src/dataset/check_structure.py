import os

# lấy đường dẫn project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "data", "raw", "chest_xray")

print("Checking dataset structure...")

for split in ["train", "val", "test"]:
    split_path = os.path.join(DATASET_PATH, split)

    print(f"\n[{split.upper()}]")

    if not os.path.exists(split_path):
        print("Folder not found:", split_path)
        continue

    for cls in os.listdir(split_path):
        class_path = os.path.join(split_path, cls)

        if os.path.isdir(class_path):
            num_images = len(os.listdir(class_path))
            print(f"{cls}: {num_images} images")