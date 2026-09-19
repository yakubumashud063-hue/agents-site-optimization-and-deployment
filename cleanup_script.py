#!/usr/bin/env python3
"""
File Cleanup and Reorganization Script
Deletes unsafe files, removes audit reports, and organizes images into categories
"""

import os
import shutil
from pathlib import Path

# Base paths
BASE_PATH = r"C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"
IMAGES_PATH = os.path.join(BASE_PATH, "static", "images")

# Tracking
deleted_files = []
organized_files = []
failed_operations = []

print("=" * 80)
print("FILE CLEANUP AND REORGANIZATION SCRIPT")
print("=" * 80)
print()

# Step 1: Delete unsafe/unused files from root
print("[STEP 1] Deleting unsafe/unused files from root...")
print("-" * 60)

files_to_delete = [
    os.path.join(BASE_PATH, "cmd.exe"),
    os.path.join(BASE_PATH, "python-3.13.1-amd64.exe"),
    os.path.join(BASE_PATH, "_Getintopc.com_Sublime_Text_4_Build_4126.rar"),
    os.path.join(IMAGES_PATH, "site.code-workspace"),
]

for file_path in files_to_delete:
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            deleted_files.append(os.path.relpath(file_path, BASE_PATH))
            print(f"✓ Deleted: {os.path.relpath(file_path, BASE_PATH)}")
        except Exception as e:
            failed_operations.append(f"Failed to delete {file_path}: {e}")
            print(f"✗ Failed to delete: {os.path.basename(file_path)} - {e}")
    else:
        print(f"→ Not found: {os.path.relpath(file_path, BASE_PATH)}")

# Step 2: Delete audit report files
print("\n[STEP 2] Deleting audit report files...")
print("-" * 60)

audit_files = [
    "AUDIT_INDEX.md",
    "AUDIT_REPORT.md",
    "AUDIT_SUMMARY.txt",
    "FINAL_AUDIT_SUMMARY.txt",
    "README_AUDIT.md",
    "CONSOLE_OUTPUT.txt",
    "DELETION_CHECKLIST.sh",
    "QUICK_REFERENCE.txt"
]

for file_name in audit_files:
    file_path = os.path.join(BASE_PATH, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            deleted_files.append(file_name)
            print(f"✓ Deleted: {file_name}")
        except Exception as e:
            failed_operations.append(f"Failed to delete {file_name}: {e}")
            print(f"✗ Failed to delete: {file_name} - {e}")
    else:
        print(f"→ Not found: {file_name}")

# Step 3: Create organized category folders
print("\n[STEP 3] Creating organized category folders...")
print("-" * 60)

categories = [
    "fruits",
    "vegetables",
    "livestock",
    "meats",
    "dairy",
    "seeds_tools",
    "services",
    "branding"
]

for category in categories:
    folder_path = os.path.join(IMAGES_PATH, category)
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"✓ Created folder: static/images/{category}")
        except Exception as e:
            failed_operations.append(f"Failed to create folder {category}: {e}")
            print(f"✗ Failed to create folder: {category} - {e}")
    else:
        print(f"→ Already exists: static/images/{category}")

# Step 4: Organize and move files into categories
print("\n[STEP 4] Moving files into categories...")
print("-" * 60)

# Define file movements
file_mappings = {
    "fruits": [
        ("apple.jpg", "Apple"),
        ("apples.jpg", "Apples"),
        ("Banana.jpg", "Banana"),
        ("Blueberries.jpg", "Blueberries"),
        ("cherries.jpg", "Cherries"),
        ("grapes.jpg", "Grapes"),
        ("lemon.jpg", "Lemon"),
        ("Mango.jpg", "Mango"),
        ("melon.jpg", "Melon"),
        ("oranges.jpg", "Oranges"),
        ("pawpaw.jpeg", "Pawpaw"),
        ("pear.png", "Pear"),
        ("pears.jpg", "Pears"),
        ("rasberries.jpg", "Raspberries"),
        ("durin.jpeg", "Durian"),
        ("Kiwi.jpg", "Kiwi"),
        ("avocado.jpg", "Avocado"),
        ("mangosteem.jpg", "Mangosteen"),
        ("Fruit-Names-in-English.webp", "Fruit Names"),
        ("madarin.jpeg", "Mandarin"),
    ],
    "vegetables": [
        ("Carot.jpg", "Carrot"),
        ("Spinach.jpg", "Spinach"),
        ("Tomatoes.png", "Tomatoes"),
        ("cabbage.jpg", "Cabbage"),
        ("beetroot.jpg", "Beetroot"),
        ("broccoli.jpg", "Broccoli"),
        ("cumber.jpg", "Cucumber"),
        ("cumcumber.jpg", "Cucumber"),
        ("corn .jpg", "Corn"),
        ("corn maize.png", "Corn Maize"),
        ("egg plant.jpg", "Eggplant"),
        ("ginger.jpg", "Ginger"),
        ("green peas.jpg", "Green Peas"),
        ("kale leaf.jpg", "Kale"),
        ("leav.jpg", "Leaves"),
        ("lettuce.jpg", "Lettuce"),
        ("okro.jpg", "Okra"),
        ("onion.jpg", "Onion"),
        ("parsley leaf.jpg", "Parsley"),
        ("potatoes.jpg", "Potatoes"),
        ("red pepper.jpg", "Red Pepper"),
        ("spepper.jpg", "Pepper"),
    ],
    "livestock": [
        ("cowbg.jpg", "Cow"),
        ("sheep.jpeg", "Sheep"),
        ("goats.jpg", "Goat"),
        ("rab1.jpeg", "Rabbit"),
        ("cock1.jpeg", "Rooster"),
        ("fowl1.jpeg", "Fowl"),
        ("guin1.webp", "Guinea Fowl"),
        ("hen1.jpeg", "Hen"),
    ],
    "branding": [
        ("logo.png", "Logo"),
        ("freshlogo.jpg", "Fresh Logo"),
    ],
}

for category, files in file_mappings.items():
    if files:
        print(f"\nMoving {category} files...")
    for src_file, label in files:
        src_path = os.path.join(IMAGES_PATH, src_file)
        dest_dir = os.path.join(IMAGES_PATH, category)
        dest_path = os.path.join(dest_dir, src_file)
        
        if os.path.exists(src_path):
            try:
                shutil.move(src_path, dest_path)
                organized_files.append(f"{src_file} → {category}/")
                print(f"✓ Moved: {label} ({src_file}) → {category}/")
            except Exception as e:
                failed_operations.append(f"Failed to move {src_file}: {e}")
                print(f"✗ Failed: {src_file} - {e}")

# Step 5: Delete duplicate and numbered files
print("\n[STEP 5] Deleting duplicate and numbered files...")
print("-" * 60)

files_to_remove = [
    # Numbered livestock duplicates
    "g2.jpeg", "g3.jpg", "g4.jpeg", "g5.jpeg", "g6.jpeg", "g7.jpeg", "g8.jpeg", "g9.jpeg",
    "sh2.jpeg", "sh4.jpeg",
    "rab4.jpeg", "rab6.jpeg", "rab7.jpeg", "rabz.jpeg", "rabfat.jpg", "rabits.jpeg",
    "redh.jpeg", "wred.jpeg", "wh1.jpeg", "wh2.jpeg", "wcock.jpeg",
    # Numbered camera images
    "c1.jpg", "c2.jpg", "c3.jpg",
    "cam2.jpg", "cam3.jpg", "cam4.jpg", "cam5.jpg", "cam6.jpg", "cam7.jpg",
    # Numbered UI/GUI files
    "gui3.jpeg", "gui4.jpeg", "gui7.jpeg",
    # Numbered history files
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~5.png",
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~7.png",
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~8.png",
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~10.png",
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~11.png",
    "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~12.png",
    # Duplicate fruit/veg files
    "Fruit-Names-in-English~14.jpg",
    "Fruit-Names-in-English~15.jpg",
    "AdobeStock_249933303_Preview (1).jpeg",
    "AdobeStock_320398182_Preview (1).jpeg",
    # Miscellaneous extras
    "fru.jpg", "images.jpeg", "jar.jpg", "swee.jpeg", "h2.jpeg", "r4.jpeg",
    "fowls.jpeg", "guinea_fowls.jpeg", "guineaf.jpeg", "wcock.jpeg",
    # Duplicates and generic files
    "vegetables.jpg", "vetables.png", "veges.jpg",
    "strawberries.gif",
    # Python installer and archive
    "python-3.13.1-amd64.exe",
    "_Getintopc.com_Sublime_Text_4_Build_4126.rar",
]

for file_name in files_to_remove:
    file_path = os.path.join(IMAGES_PATH, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            deleted_files.append(file_name)
            print(f"✓ Deleted: {file_name}")
        except Exception as e:
            failed_operations.append(f"Failed to delete {file_name}: {e}")
            print(f"✗ Failed to delete: {file_name} - {e}")

# Summary Report
print("\n" + "=" * 80)
print("CLEANUP SUMMARY")
print("=" * 80)

print(f"\nTotal files deleted: {len(deleted_files)}")
print(f"Total files organized: {len(organized_files)}")
if failed_operations:
    print(f"Failed operations: {len(failed_operations)}")

print("\n[DELETED FILES]")
print("-" * 60)
for file in deleted_files:
    print(f"  - {file}")

print("\n[FOLDER STRUCTURE]")
print("-" * 60)

for category in sorted(categories):
    folder_path = os.path.join(IMAGES_PATH, category)
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        print(f"  {category}/ - {len(files)} files")
        for file in sorted(files):
            print(f"    └─ {file}")

# List remaining unorganized files
print("\nRemaining unorganized files in static/images:")
print("-" * 60)
all_files = [f for f in os.listdir(IMAGES_PATH) if os.path.isfile(os.path.join(IMAGES_PATH, f))]
if all_files:
    for file in sorted(all_files):
        print(f"  - {file}")
else:
    print("  (None - all files organized!)")

print("\n" + "=" * 80)
print("CLEANUP COMPLETE")
print("=" * 80)

if failed_operations:
    print("\n[FAILED OPERATIONS]")
    print("-" * 60)
    for op in failed_operations:
        print(f"  ⚠ {op}")
