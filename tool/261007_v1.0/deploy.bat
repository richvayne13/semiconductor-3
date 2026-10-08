@echo off
echo ========================================================
echo [1/3] Building HTML...
echo ========================================================
python "%~dp0build_html.py"

echo.
echo ========================================================
echo [2/3] Git Add and Commit...
echo ========================================================
pushd "%~dp0..\.."
git add .
git commit -m "update: Q01 semiconductor dashboard"

echo.
echo ========================================================
echo [3/3] Git Push to GitHub Pages...
echo ========================================================
git push origin main
popd

echo.
echo ========================================================
echo [SUCCESS] Deployed online to https://richvayne13.github.io/semiconductor-3/
echo ========================================================
