import os
from PIL import Image

# Lấy đường dẫn thư mục project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Đường dẫn dataset
DATASET_PATH = os.path.join(BASE_DIR, "data", "raw", "chest_xray")

print("===== PHÂN TÍCH DATASET =====")
print("Dataset path:", DATASET_PATH)

total_images = 0

splits = ["train", "val", "test"]

for split in splits:
    split_path = os.path.join(DATASET_PATH, split)

    print("\n======================")
    print(f"[{split.upper()}]")

    if not os.path.exists(split_path):
        print("Folder không tồn tại:", split_path)
        continue

    split_count = 0

    for cls in os.listdir(split_path):
        class_path = os.path.join(split_path, cls)

        if not os.path.isdir(class_path):
            continue

        images = [
            f for f in os.listdir(class_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]

        num_images = len(images)

        split_count += num_images
        total_images += num_images

        print(f"{cls}: {num_images} images")

        # thử đọc 1 ảnh đầu
        if num_images > 0:
            sample_image = os.path.join(class_path, images[0])

            try:
                with Image.open(sample_image) as img:
                    print("  Sample size:", img.size, "| mode:", img.mode)
            except Exception as e:
                print("  Error reading image:", e)

    print(f"Tổng số ảnh trong {split}: {split_count}")

print("\n======================")
print("TỔNG TOÀN BỘ DATASET:", total_images, "images")