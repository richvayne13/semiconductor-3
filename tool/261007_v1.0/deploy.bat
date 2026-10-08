@echo off
chcp 65001 > nul
echo [1/3] HTML Sync Build...
python "%~dp0build_html.py"

echo.
echo [2/3] Git Staging and Commit...
pushd "%~dp0..\.."
git add .
git commit -m "update: Q01 헤일로 모서리 농도와 공핍층 정지 로직 추가"

echo.
echo [3/3] Git Push to GitHub...
git push origin main
popd

echo.
echo [SUCCESS] Deployed online: https://richvayne13.github.io/semiconductor-3/
