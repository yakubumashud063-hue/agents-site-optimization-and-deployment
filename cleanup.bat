@echo off
REM File Cleanup and Reorganization Script
setlocal enabledelayedexpansion

cd /d "C:\Users\HP\Desktop\site.worktrees\agents-site-optimization-and-deployment"

echo.
echo ================================================================================
echo FILE CLEANUP AND REORGANIZATION SCRIPT
echo ================================================================================
echo.

REM Step 1: Delete unsafe/unused files
echo [STEP 1] Deleting unsafe/unused files from root...
echo ---------------------------------------------------------------

if exist cmd.exe (
    del /F /Q cmd.exe
    echo OK - Deleted: cmd.exe
) else (
    echo -- Not found: cmd.exe
)

if exist _Getintopc.com_Sublime_Text_4_Build_4126.rar (
    del /F /Q _Getintopc.com_Sublime_Text_4_Build_4126.rar
    echo OK - Deleted: _Getintopc.com_Sublime_Text_4_Build_4126.rar
) else (
    echo -- Not found: _Getintopc.com_Sublime_Text_4_Build_4126.rar
)

if exist static\images\site.code-workspace (
    del /F /Q static\images\site.code-workspace
    echo OK - Deleted: static\images\site.code-workspace
) else (
    echo -- Not found: static\images\site.code-workspace
)

REM Step 2: Delete audit report files
echo.
echo [STEP 2] Deleting audit report files...
echo ---------------------------------------------------------------

for %%F in (AUDIT_INDEX.md AUDIT_REPORT.md AUDIT_SUMMARY.txt FINAL_AUDIT_SUMMARY.txt README_AUDIT.md CONSOLE_OUTPUT.txt DELETION_CHECKLIST.sh QUICK_REFERENCE.txt) do (
    if exist %%F (
        del /F /Q %%F
        echo OK - Deleted: %%F
    )
)

REM Step 3: Create organized category folders
echo.
echo [STEP 3] Creating organized category folders...
echo ---------------------------------------------------------------

for %%D in (fruits vegetables livestock meats dairy seeds_tools services branding) do (
    if not exist static\images\%%D (
        mkdir static\images\%%D
        echo OK - Created folder: static\images\%%D
    ) else (
        echo -- Already exists: static\images\%%D
    )
)

REM Step 4: Move files into categories
echo.
echo [STEP 4] Moving files into categories...
echo ---------------------------------------------------------------
echo.
echo Moving fruit files...

REM Fruits
for %%F in (apple.jpg apples.jpg Banana.jpg Blueberries.jpg cherries.jpg grapes.jpg lemon.jpg Mango.jpg melon.jpg oranges.jpg pawpaw.jpeg pear.png pears.jpg rasberries.jpg durin.jpeg Kiwi.jpg avocado.jpg mangosteem.jpg "Fruit-Names-in-English.webp" madarin.jpeg) do (
    if exist static\images\%%F (
        move /Y static\images\%%F static\images\fruits\%%F >nul
        echo OK - Moved: %%F ^-^> fruits\
    )
)

echo.
echo Moving vegetable files...

REM Vegetables
for %%F in (Carot.jpg Spinach.jpg Tomatoes.png cabbage.jpg beetroot.jpg broccoli.jpg cumber.jpg cumcumber.jpg "corn .jpg" "corn maize.png" "egg plant.jpg" ginger.jpg "green peas.jpg" "kale leaf.jpg" leav.jpg lettuce.jpg okro.jpg onion.jpg "parsley leaf.jpg" potatoes.jpg "red pepper.jpg" spepper.jpg) do (
    if exist static\images\%%F (
        move /Y static\images\%%F static\images\vegetables\%%F >nul
        echo OK - Moved: %%F ^-^> vegetables\
    )
)

echo.
echo Moving livestock files...

REM Livestock
for %%F in (cowbg.jpg sheep.jpeg goats.jpg rab1.jpeg cock1.jpeg fowl1.jpeg guin1.webp hen1.jpeg) do (
    if exist static\images\%%F (
        move /Y static\images\%%F static\images\livestock\%%F >nul
        echo OK - Moved: %%F ^-^> livestock\
    )
)

echo.
echo Moving branding files...

REM Branding
for %%F in (logo.png freshlogo.jpg) do (
    if exist static\images\%%F (
        move /Y static\images\%%F static\images\branding\%%F >nul
        echo OK - Moved: %%F ^-^> branding\
    )
)

REM Step 5: Delete duplicate and numbered files
echo.
echo [STEP 5] Deleting duplicate and numbered files...
echo ---------------------------------------------------------------

REM Numbered livestock duplicates
for %%F in (g2.jpeg g3.jpg g4.jpeg g5.jpeg g6.jpeg g7.jpeg g8.jpeg g9.jpeg sh2.jpeg sh4.jpeg rab4.jpeg rab6.jpeg rab7.jpeg rabz.jpeg rabfat.jpg rabits.jpeg redh.jpeg wred.jpeg wh1.jpeg wh2.jpeg wcock.jpeg) do (
    if exist static\images\%%F del /F /Q static\images\%%F & echo OK - Deleted: %%F
)

REM Numbered camera images
for %%F in (c1.jpg c2.jpg c3.jpg cam2.jpg cam3.jpg cam4.jpg cam5.jpg cam6.jpg cam7.jpg) do (
    if exist static\images\%%F del /F /Q static\images\%%F & echo OK - Deleted: %%F
)

REM Numbered UI/GUI files
for %%F in (gui3.jpeg gui4.jpeg gui7.jpeg) do (
    if exist static\images\%%F del /F /Q static\images\%%F & echo OK - Deleted: %%F
)

REM History files
for %%F in ("aa7c6f80-099e-4ecc-aadc-fd7a72408b81~5.png" "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~7.png" "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~8.png" "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~10.png" "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~11.png" "aa7c6f80-099e-4ecc-aadc-fd7a72408b81~12.png") do (
    if exist static\images\%%F del /F /Q static\images\%%F & echo OK - Deleted: %%F
)

REM Duplicate files
for %%F in ("Fruit-Names-in-English~14.jpg" "Fruit-Names-in-English~15.jpg" "AdobeStock_249933303_Preview (1).jpeg" "AdobeStock_320398182_Preview (1).jpeg" fru.jpg images.jpeg jar.jpg swee.jpeg h2.jpeg r4.jpeg fowls.jpeg guinea_fowls.jpeg guineaf.jpeg vegetables.jpg vetables.png veges.jpg strawberries.gif) do (
    if exist static\images\%%F del /F /Q static\images\%%F & echo OK - Deleted: %%F
)

REM Summary
echo.
echo ================================================================================
echo CLEANUP COMPLETE - FOLDER STRUCTURE
echo ================================================================================
echo.

for /d %%D in (static\images\*) do (
    echo %%~nxD\ - Files:
    for %%F in (%%D\*) do (
        echo   - %%~nxF
    )
    echo.
)

echo ================================================================================
echo REMAINING UNORGANIZED FILES
echo ================================================================================
echo.

for %%F in (static\images\*) do (
    if not "%%~nxF"=="fruits" if not "%%~nxF"=="vegetables" if not "%%~nxF"=="livestock" if not "%%~nxF"=="meats" if not "%%~nxF"=="dairy" if not "%%~nxF"=="seeds_tools" if not "%%~nxF"=="services" if not "%%~nxF"=="branding" (
        if exist "%%F" echo   - %%~nxF
    )
)

echo.
echo ================================================================================
echo Done!
echo ================================================================================
