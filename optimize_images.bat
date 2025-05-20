@echo off
setlocal enabledelayedexpansion

:: Create optimized directory if it doesn't exist
if not exist "optimized" mkdir optimized

:: Convert all images to WebP format
echo Optimizing images...
for %%f in (*.jpg *.jpeg *.png) do (
    echo Optimizing %%f
    magick convert "%%f" -quality 80 "optimized/%%~nf.webp"
)

echo Image optimization complete!
pause
