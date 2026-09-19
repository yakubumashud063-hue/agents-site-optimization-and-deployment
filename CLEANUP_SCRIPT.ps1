# Cleanup and Organization Script
# This script will organize files and delete unsafe/unused files

$basePath = "C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"
$imagesPath = Join-Path $basePath "static\images"
$deletionLog = @()
$organizationLog = @()

Write-Host "=" * 80
Write-Host "FILE CLEANUP AND REORGANIZATION SCRIPT"
Write-Host "=" * 80
Write-Host ""

# Step 1: Delete unsafe/unused files from root
Write-Host "[STEP 1] Deleting unsafe/unused files from root..."
Write-Host "-" * 60

$filesToDelete = @(
    "cmd.exe",
    "python-3.13.1-amd64.exe",
    "_Getintopc.com_Sublime_Text_4_Build_4126.rar",
    "static\images\site.code-workspace"
)

foreach ($file in $filesToDelete) {
    $fullPath = Join-Path $basePath $file
    if (Test-Path $fullPath -ErrorAction SilentlyContinue) {
        try {
            Remove-Item $fullPath -Force -ErrorAction Stop
            $deletionLog += $file
            Write-Host "✓ Deleted: $file"
        } catch {
            Write-Host "✗ Failed to delete: $file - $_"
        }
    } else {
        Write-Host "→ Not found: $file"
    }
}

Write-Host "`n[STEP 2] Deleting audit report files..."
Write-Host "-" * 60

$auditFiles = @(
    "AUDIT_INDEX.md",
    "AUDIT_REPORT.md",
    "AUDIT_SUMMARY.txt",
    "FINAL_AUDIT_SUMMARY.txt",
    "README_AUDIT.md",
    "CONSOLE_OUTPUT.txt",
    "DELETION_CHECKLIST.sh",
    "QUICK_REFERENCE.txt"
)

foreach ($file in $auditFiles) {
    $fullPath = Join-Path $basePath $file
    if (Test-Path $fullPath -ErrorAction SilentlyContinue) {
        try {
            Remove-Item $fullPath -Force -ErrorAction Stop
            $deletionLog += $file
            Write-Host "✓ Deleted: $file"
        } catch {
            Write-Host "✗ Failed to delete: $file - $_"
        }
    } else {
        Write-Host "→ Not found: $file"
    }
}

# Step 2: Create organized category folders
Write-Host "`n[STEP 3] Creating organized category folders..."
Write-Host "-" * 60

$categories = @(
    "fruits",
    "vegetables",
    "livestock",
    "meats",
    "dairy",
    "seeds_tools",
    "services",
    "branding"
)

foreach ($category in $categories) {
    $folderPath = Join-Path $imagesPath $category
    if (-not (Test-Path $folderPath)) {
        try {
            New-Item -ItemType Directory -Path $folderPath -Force | Out-Null
            Write-Host "✓ Created folder: static/images/$category"
        } catch {
            Write-Host "✗ Failed to create folder: $category - $_"
        }
    } else {
        Write-Host "→ Already exists: static/images/$category"
    }
}

# Step 3: Organize and move files into categories
Write-Host "`n[STEP 4] Moving files into categories..."
Write-Host "-" * 60

# FRUITS: Keep representative files and delete numbered duplicates
$fruitFiles = @(
    @{src="apple.jpg"; dest="fruits"; label="Apple"},
    @{src="apples.jpg"; dest="fruits"; label="Apples"},
    @{src="Banana.jpg"; dest="fruits"; label="Banana"},
    @{src="Blueberries.jpg"; dest="fruits"; label="Blueberries"},
    @{src="cherries.jpg"; dest="fruits"; label="Cherries"},
    @{src="grapes.jpg"; dest="fruits"; label="Grapes"},
    @{src="lemon.jpg"; dest="fruits"; label="Lemon"},
    @{src="Mango.jpg"; dest="fruits"; label="Mango"},
    @{src="melon.jpg"; dest="fruits"; label="Melon"},
    @{src="oranges.jpg"; dest="fruits"; label="Oranges"},
    @{src="pawpaw.jpeg"; dest="fruits"; label="Pawpaw"},
    @{src="pear.png"; dest="fruits"; label="Pear"},
    @{src="pears.jpg"; dest="fruits"; label="Pears"},
    @{src="rasberries.jpg"; dest="fruits"; label="Raspberries"},
    @{src="durin.jpeg"; dest="fruits"; label="Durian"},
    @{src="Kiwi.jpg"; dest="fruits"; label="Kiwi"},
    @{src="avocado.jpg"; dest="fruits"; label="Avocado"},
    @{src="mangosteem.jpg"; dest="fruits"; label="Mangosteen"}
)

# VEGETABLES: Keep representative files
$vegetableFiles = @(
    @{src="Carot.jpg"; dest="vegetables"; label="Carrot"},
    @{src="Spinach.jpg"; dest="vegetables"; label="Spinach"},
    @{src="Tomatoes.png"; dest="vegetables"; label="Tomatoes"},
    @{src="cabbage.jpg"; dest="vegetables"; label="Cabbage"},
    @{src="beetroot.jpg"; dest="vegetables"; label="Beetroot"},
    @{src="broccoli.jpg"; dest="vegetables"; label="Broccoli"},
    @{src="cumber.jpg"; dest="vegetables"; label="Cucumber"},
    @{src="cumcumber.jpg"; dest="vegetables"; label="Cucumber"},
    @{src="corn .jpg"; dest="vegetables"; label="Corn"},
    @{src="corn maize.png"; dest="vegetables"; label="Corn Maize"},
    @{src="egg plant.jpg"; dest="vegetables"; label="Eggplant"},
    @{src="ginger.jpg"; dest="vegetables"; label="Ginger"},
    @{src="green peas.jpg"; dest="vegetables"; label="Green Peas"},
    @{src="kale leaf.jpg"; dest="vegetables"; label="Kale"},
    @{src="leav.jpg"; dest="vegetables"; label="Leaves"},
    @{src="lettuce.jpg"; dest="vegetables"; label="Lettuce"},
    @{src="okro.jpg"; dest="vegetables"; label="Okra"},
    @{src="onion.jpg"; dest="vegetables"; label="Onion"},
    @{src="parsley leaf.jpg"; dest="vegetables"; label="Parsley"},
    @{src="potatoes.jpg"; dest="vegetables"; label="Potatoes"},
    @{src="red pepper.jpg"; dest="vegetables"; label="Red Pepper"},
    @{src="spepper.jpg"; dest="vegetables"; label="Pepper"}
)

# LIVESTOCK: Keep ONE representative of each animal type (delete numbered duplicates)
$livestockFiles = @(
    @{src="cowbg.jpg"; dest="livestock"; label="Cow"},
    @{src="sheep.jpeg"; dest="livestock"; label="Sheep"},
    @{src="goats.jpg"; dest="livestock"; label="Goat"},
    @{src="rab1.jpeg"; dest="livestock"; label="Rabbit"},
    @{src="cock1.jpeg"; dest="livestock"; label="Rooster"},
    @{src="fowl1.jpeg"; dest="livestock"; label="Fowl"},
    @{src="guin1.webp"; dest="livestock"; label="Guinea Fowl"},
    @{src="hen1.jpeg"; dest="livestock"; label="Hen"}
)

# BRANDING: Logo and site assets
$brandingFiles = @(
    @{src="logo.png"; dest="branding"; label="Logo"},
    @{src="freshlogo.jpg"; dest="branding"; label="Fresh Logo"}
)

Write-Host ""
Write-Host "Moving fruit files..."
foreach ($file in $fruitFiles) {
    $srcPath = Join-Path $imagesPath $file.src
    $destDir = Join-Path $imagesPath $file.dest
    $destPath = Join-Path $destDir $file.src
    
    if (Test-Path $srcPath -ErrorAction SilentlyContinue) {
        try {
            Move-Item $srcPath $destPath -Force -ErrorAction Stop
            $organizationLog += "Moved: $($file.src) → $($file.dest)/"
            Write-Host "✓ Moved: $($file.label) ($($file.src)) → $($file.dest)/"
        } catch {
            Write-Host "✗ Failed: $($file.src) - $_"
        }
    }
}

Write-Host ""
Write-Host "Moving vegetable files..."
foreach ($file in $vegetableFiles) {
    $srcPath = Join-Path $imagesPath $file.src
    $destDir = Join-Path $imagesPath $file.dest
    $destPath = Join-Path $destDir $file.src
    
    if (Test-Path $srcPath -ErrorAction SilentlyContinue) {
        try {
            Move-Item $srcPath $destPath -Force -ErrorAction Stop
            $organizationLog += "Moved: $($file.src) → $($file.dest)/"
            Write-Host "✓ Moved: $($file.label) ($($file.src)) → $($file.dest)/"
        } catch {
            Write-Host "✗ Failed: $($file.src) - $_"
        }
    }
}

Write-Host ""
Write-Host "Moving livestock files..."
foreach ($file in $livestockFiles) {
    $srcPath = Join-Path $imagesPath $file.src
    $destDir = Join-Path $imagesPath $file.dest
    $destPath = Join-Path $destDir $file.src
    
    if (Test-Path $srcPath -ErrorAction SilentlyContinue) {
        try {
            Move-Item $srcPath $destPath -Force -ErrorAction Stop
            $organizationLog += "Moved: $($file.src) → $($file.dest)/"
            Write-Host "✓ Moved: $($file.label) ($($file.src)) → $($file.dest)/"
        } catch {
            Write-Host "✗ Failed: $($file.src) - $_"
        }
    }
}

Write-Host ""
Write-Host "Moving branding files..."
foreach ($file in $brandingFiles) {
    $srcPath = Join-Path $imagesPath $file.src
    $destDir = Join-Path $imagesPath $file.dest
    $destPath = Join-Path $destDir $file.src
    
    if (Test-Path $srcPath -ErrorAction SilentlyContinue) {
        try {
            Move-Item $srcPath $destPath -Force -ErrorAction Stop
            $organizationLog += "Moved: $($file.src) → $($file.dest)/"
            Write-Host "✓ Moved: $($file.label) ($($file.src)) → $($file.dest)/"
        } catch {
            Write-Host "✗ Failed: $($file.src) - $_"
        }
    }
}

# Step 4: Delete duplicate and numbered files
Write-Host "`n[STEP 5] Deleting duplicate and numbered files..."
Write-Host "-" * 60

# Files to delete (duplicates and numbered versions)
$filesToRemove = @(
    # Numbered livestock duplicates (keep only g1/sh1/rab1/cock1)
    "g2.jpeg", "g3.jpg", "g4.jpeg", "g5.jpeg", "g6.jpeg", "g7.jpeg", "g8.jpeg", "g9.jpeg",
    "sh2.jpeg", "sh4.jpeg",
    "rab4.jpeg", "rab6.jpeg", "rab7.jpeg", "rabz.jpeg", "rabfat.jpg", "rabits.jpeg",
    "redh.jpeg", "wred.jpeg", "wh1.jpeg", "wh2.jpeg", "wock.jpeg",
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
    "strawberries.gif"
)

foreach ($file in $filesToRemove) {
    $fullPath = Join-Path $imagesPath $file
    if (Test-Path $fullPath -ErrorAction SilentlyContinue) {
        try {
            Remove-Item $fullPath -Force -ErrorAction Stop
            $deletionLog += $file
            Write-Host "✓ Deleted: $file"
        } catch {
            Write-Host "✗ Failed to delete: $file - $_"
        }
    }
}

# Summary Report
Write-Host "`n" + "=" * 80
Write-Host "CLEANUP SUMMARY"
Write-Host "=" * 80

Write-Host "`nTotal files deleted: $($deletionLog.Count)"
Write-Host "Total files organized: $($organizationLog.Count)"

Write-Host "`n[DELETED FILES]"
Write-Host "-" * 60
$deletionLog | ForEach-Object { Write-Host "  - $_" }

Write-Host "`n[FOLDER STRUCTURE]"
Write-Host "-" * 60
Get-ChildItem $imagesPath -Directory | ForEach-Object {
    $count = (Get-ChildItem $_.FullPath -Force | Measure-Object).Count
    Write-Host "  $($_.Name)/ - $count files"
    Get-ChildItem $_.FullPath -File | ForEach-Object {
        Write-Host "    └─ $($_.Name)"
    }
}

Write-Host "`nRemaining unorganized files in static/images:"
$unorganized = Get-ChildItem $imagesPath -File -Force
if ($unorganized) {
    $unorganized | ForEach-Object { Write-Host "  - $($_.Name)" }
} else {
    Write-Host "  (None - all files organized!)"
}

Write-Host "`n" + "=" * 80
Write-Host "CLEANUP COMPLETE"
Write-Host "=" * 80
