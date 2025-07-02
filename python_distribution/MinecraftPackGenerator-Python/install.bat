@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - Python版 インストーラー
echo ==================================================
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo Python 3.7以上をインストールしてください:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Pythonが確認されました
echo.

echo 📦 依存関係をインストール中...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ 依存関係のインストールに失敗しました
    pause
    exit /b 1
)
echo ✅ 依存関係のインストールが完了しました
echo.

echo 🧪 パック生成をテスト中...
python pack_generator.py --preview
if %errorlevel% neq 0 (
    echo ❌ パック生成のテストに失敗しました
    echo pack_generator.log を確認してください
    pause
    exit /b 1
)
echo ✅ パック生成のテストが成功しました！
echo.

echo 🎉 インストールが完了しました！
echo.
echo 📚 使用方法:
echo   - python pack_generator.py でパック生成
echo   - python pack_generator.py --help でヘルプ表示
echo.
echo 📁 生成されるファイル:
echo   - datapack.zip (データパック)
echo   - resourcepack.zip (リソースパック)
echo   - output/ (展開されたファイル)
echo.
echo 📖 詳細な使用方法は docs/ フォルダを参照してください
echo.
pause
