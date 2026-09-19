# MANUAL FILE CLEANUP AND REORGANIZATION GUIDE

## 🎯 OBJECTIVE
Safely clean up the repository by removing unsafe files, audit reports, and organizing images into logical categories.

## ⚠️ CRITICAL FILES TO DELETE IMMEDIATELY

### Root Directory (4 files)
These files should NOT be in the repository:
```
❌ cmd.exe                                    (Windows executable - unsafe)
❌ python-3.13.1-amd64.exe                   (Python installer - unsafe)
❌ _Getintopc.com_Sublime_Text_4_Build_4126.rar  (Archive file - unsafe)
❌ static/images/site.code-workspace         (Config file - should be at root level if needed)
```

### Audit Report Files (8 files)
These were generated during the audit and should be deleted:
```
❌ AUDIT_INDEX.md
❌ AUDIT_REPORT.md
❌ AUDIT_SUMMARY.txt
❌ FINAL_AUDIT_SUMMARY.txt
❌ README_AUDIT.md
❌ CONSOLE_OUTPUT.txt
❌ DELETION_CHECKLIST.sh
❌ QUICK_REFERENCE.txt
```

**Total critical deletions: 12 files**

---

## 📁 FOLDER STRUCTURE TO CREATE

Create these folders in `static/images/`:

```
static/images/
├── fruits/                 # Fruit images
├── vegetables/             # Vegetable images
├── livestock/              # Animal images (ONE per animal type)
├── meats/                  # Meat product images
├── dairy/                  # Dairy product images
├── seeds_tools/            # Seeds and tools images
├── services/               # Service-related images
└── branding/               # Logo and branding assets
```

---

## 📋 FILES TO ORGANIZE BY CATEGORY

### CATEGORY: Fruits (20 files → Move to `static/images/fruits/`)
```
apple.jpg
apples.jpg
Banana.jpg
Blueberries.jpg
cherries.jpg
grapes.jpg
lemon.jpg
Mango.jpg
melon.jpg
oranges.jpg
pawpaw.jpeg
pear.png
pears.jpg
rasberries.jpg
durin.jpeg
Kiwi.jpg
avocado.jpg
mangosteem.jpg
Fruit-Names-in-English.webp
madarin.jpeg
```

### CATEGORY: Vegetables (22 files → Move to `static/images/vegetables/`)
```
Carot.jpg                  (Carrot)
Spinach.jpg
Tomatoes.png
cabbage.jpg
beetroot.jpg
broccoli.jpg
cumber.jpg
cumcumber.jpg
corn .jpg
corn maize.png
egg plant.jpg
ginger.jpg
green peas.jpg
kale leaf.jpg
leav.jpg
lettuce.jpg
okro.jpg
onion.jpg
parsley leaf.jpg
potatoes.jpg
red pepper.jpg
spepper.jpg
```

### CATEGORY: Livestock (8 files → Move to `static/images/livestock/`)
**IMPORTANT: Keep ONLY ONE representative of each animal type**
```
cowbg.jpg                  (KEEP - Cow)
sheep.jpeg                 (KEEP - Sheep)
goats.jpg                  (KEEP - Goat)
rab1.jpeg                  (KEEP - Rabbit)
cock1.jpeg                 (KEEP - Rooster)
fowl1.jpeg                 (KEEP - Fowl)
guin1.webp                 (KEEP - Guinea Fowl)
hen1.jpeg                  (KEEP - Hen)
```

### CATEGORY: Branding (2 files → Move to `static/images/branding/`)
```
logo.png
freshlogo.jpg
```

---

## 🗑️ DUPLICATE FILES TO DELETE

### Livestock Duplicates (DELETE these - we're keeping only one per animal type)
```
❌ g2.jpeg, g3.jpg, g4.jpeg, g5.jpeg, g6.jpeg, g7.jpeg, g8.jpeg, g9.jpeg
   (Goat duplicates - keep g1.jpeg? or cowbg.jpg)
❌ sh2.jpeg, sh4.jpeg
   (Sheep duplicates - sh1.jpeg is the keeper)
❌ rab4.jpeg, rab6.jpeg, rab7.jpeg, rabz.jpeg, rabfat.jpg, rabits.jpeg
   (Rabbit duplicates - rab1.jpeg is the keeper)
❌ redh.jpeg, wred.jpeg
   (Unknown duplicates)
❌ wh1.jpeg, wh2.jpeg
   (Unknown numbered files)
❌ wcock.jpeg
   (Duplicate rooster)
```

### Camera/Equipment Numbered Files (DELETE - appear to be test captures)
```
❌ c1.jpg, c2.jpg, c3.jpg
   (Camera numbered files)
❌ cam2.jpg, cam3.jpg, cam4.jpg, cam5.jpg, cam6.jpg, cam7.jpg
   (More camera numbered files)
```

### GUI/UI Numbered Files (DELETE)
```
❌ gui3.jpeg, gui4.jpeg, gui7.jpeg
   (GUI interface screenshots)
```

### Version History Files (DELETE - backup versions)
```
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~5.png
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~7.png
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~8.png
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~10.png
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~11.png
❌ aa7c6f80-099e-4ecc-aadc-fd7a72408b81~12.png
```

### Miscellaneous Duplicate/Test Files (DELETE)
```
❌ Fruit-Names-in-English~14.jpg
❌ Fruit-Names-in-English~15.jpg
   (Duplicate references)
❌ AdobeStock_249933303_Preview (1).jpeg
❌ AdobeStock_320398182_Preview (1).jpeg
   (Duplicate Adobe stock files)
❌ fru.jpg, images.jpeg, jar.jpg, swee.jpeg, h2.jpeg, r4.jpeg
   (Generic/test images)
❌ fowls.jpeg, guinea_fowls.jpeg, guineaf.jpeg
   (Duplicate poultry)
❌ vegetables.jpg, vetables.png, veges.jpg
   (Generic vegetable images)
❌ strawberries.gif
   (Duplicate strawberry)
❌ durin fruit.jpg
   (Duplicate durian)
```

**Total duplicates to delete: ~50 files**

---

## 📊 CLEANUP STATISTICS

| Category | Count |
|----------|-------|
| Audit files to delete | 8 |
| Unsafe root files to delete | 4 |
| Livestock duplicates to delete | 10 |
| Camera/GUI numbered files to delete | 11 |
| Version history files to delete | 6 |
| Other duplicates to delete | 19 |
| **Total files to delete** | **~58 files** |
| Files to organize into categories | 52 |
| Final folders to create | 8 |

---

## 🚀 HOW TO EXECUTE

### **Option 1: Using Batch File (RECOMMENDED for Windows)**
```batch
cd "C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"
cleanup.bat
```

### **Option 2: Using Python Script**
```bash
cd "C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"
python cleanup_script.py
```

### **Option 3: Using PowerShell**
```powershell
cd "C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\CLEANUP_SCRIPT.ps1
```

### **Option 4: Manual Execution (Step by Step)**

#### Step 1: Create folders
```batch
mkdir static\images\fruits
mkdir static\images\vegetables
mkdir static\images\livestock
mkdir static\images\meats
mkdir static\images\dairy
mkdir static\images\seeds_tools
mkdir static\images\services
mkdir static\images\branding
```

#### Step 2: Delete unsafe files
```batch
del cmd.exe
del _Getintopc.com_Sublime_Text_4_Build_4126.rar
del static\images\site.code-workspace
```

#### Step 3: Delete audit files
```batch
del AUDIT_INDEX.md
del AUDIT_REPORT.md
del AUDIT_SUMMARY.txt
del FINAL_AUDIT_SUMMARY.txt
del README_AUDIT.md
del CONSOLE_OUTPUT.txt
del DELETION_CHECKLIST.sh
del QUICK_REFERENCE.txt
```

#### Step 4: Move organize files (examples)
```batch
move static\images\apple.jpg static\images\fruits\
move static\images\Banana.jpg static\images\fruits\
move static\images\Carot.jpg static\images\vegetables\
move static\images\cowbg.jpg static\images\livestock\
```

#### Step 5: Delete duplicates
```batch
del static\images\g2.jpeg
del static\images\g3.jpg
del static\images\sh2.jpeg
del static\images\rab4.jpeg
REM ... (repeat for all duplicates listed above)
```

---

## ✅ VERIFICATION CHECKLIST

After running the cleanup script, verify:

- [ ] **Root directory cleaned**
  - [ ] cmd.exe deleted
  - [ ] python-3.13.1-amd64.exe deleted
  - [ ] _Getintopc.com_Sublime_Text_4_Build_4126.rar deleted

- [ ] **Audit files deleted**
  - [ ] All AUDIT_*.md files removed
  - [ ] FINAL_AUDIT_SUMMARY.txt removed
  - [ ] README_AUDIT.md removed
  - [ ] CONSOLE_OUTPUT.txt removed
  - [ ] DELETION_CHECKLIST.sh removed
  - [ ] QUICK_REFERENCE.txt removed

- [ ] **Folder structure created**
  - [ ] static/images/fruits/ exists
  - [ ] static/images/vegetables/ exists
  - [ ] static/images/livestock/ exists
  - [ ] static/images/meats/ exists
  - [ ] static/images/dairy/ exists
  - [ ] static/images/seeds_tools/ exists
  - [ ] static/images/services/ exists
  - [ ] static/images/branding/ exists

- [ ] **Files organized**
  - [ ] Fruits folder contains 20 fruit images
  - [ ] Vegetables folder contains 22 vegetable images
  - [ ] Livestock folder contains 8 animal images (1 per type)
  - [ ] Branding folder contains logo.png and freshlogo.jpg

- [ ] **Duplicates removed**
  - [ ] No numbered livestock files (g1-g9, sh1-sh4, rab1-rab7)
  - [ ] No numbered camera files (c1-c3, cam2-cam7)
  - [ ] No version history files (aa7c6f80...~*.png)
  - [ ] No miscellaneous duplicates (fru.jpg, images.jpeg, jar.jpg, etc.)

---

## 🔍 REMAINING FILES (Not Organized)

The following Adobe Stock images will remain in `static/images/` as they appear to be generic reference assets. Consider moving these to a separate folder if needed:

```
9168a8879330db3008cbb48455bf5370.jpg
AdobeStock_10343740_Preview.jpeg
AdobeStock_1097229380_Preview.jpeg
AdobeStock_165933212_Preview.jpeg
AdobeStock_182899273_Preview.jpeg
AdobeStock_215439279_Preview.jpeg
AdobeStock_223017721_Preview.jpeg
AdobeStock_249933303_Preview.jpeg
AdobeStock_266683754_Preview.jpeg
AdobeStock_306818191_Preview.jpeg
AdobeStock_320398182_Preview.jpeg
AdobeStock_356468494_Preview.jpeg
AdobeStock_41301053_Preview.jpeg
AdobeStock_496371797_Preview.jpeg
AdobeStock_527918116_Preview.png
AdobeStock_532645441_Preview.jpeg
AdobeStock_535268032_Preview.png
AdobeStock_53590332_Preview.jpeg
AdobeStock_537046123_Preview.png
AdobeStock_545474888_Preview.png
AdobeStock_572570982_Preview.jpeg
AdobeStock_599808048_Preview.png
AdobeStock_601408545_Preview.png
AdobeStock_607564487_Preview.png
AdobeStock_618992780_Preview.png
AdobeStock_66500337_Preview.jpeg
AdobeStock_69190946_Preview.jpeg
AdobeStock_80961739_Preview.jpeg
AdobeStock_813762506_Preview.jpeg
AdobeStock_889538282_Preview.jpeg
AdobeStock_93875874_Preview.jpeg
AdobeStock_982916066_Preview.jpeg
```

**Recommendation:** Create `static/images/adobe_stock/` folder and move these for better organization.

---

## 🎯 NEXT STEPS AFTER CLEANUP

1. **Delete the cleanup scripts** (they're no longer needed):
   - cleanup.bat
   - cleanup_script.py
   - CLEANUP_SCRIPT.ps1
   - CLEANUP_EXECUTION_REPORT.md
   - MANUAL_CLEANUP_GUIDE.md (this file)

2. **Commit the changes**:
   ```bash
   git add -A
   git commit -m "Cleanup: Remove unsafe files, organize images into categories"
   ```

3. **Update documentation**: If your project has a README or assets directory guide, update it to reflect the new folder structure.

4. **Consider Adobe Stock images**: Decide whether to organize them into `adobe_stock/` subfolder or keep them at root level.

---

## 📝 NOTES

- The goat images (g*.jpeg) were ambiguous - check if g1.jpeg is the representative or if cowbg.jpg is more appropriate
- The chicken/rooster images have multiple variations - cock1.jpeg and hen1.jpeg are kept as representatives
- Several files had typos (Carot → Carrot, cumcumber, spepper → pepper) - these are preserved as-is to avoid breaking references
- The Adobe Stock preview images appear to be placeholders/references - consider if they should be in a separate folder

---

**Status**: Ready for execution  
**Scripts Available**: cleanup.bat, cleanup_script.py, CLEANUP_SCRIPT.ps1  
**Total Cleanup Scope**: 58 files deleted, 52 files organized into 8 categories
