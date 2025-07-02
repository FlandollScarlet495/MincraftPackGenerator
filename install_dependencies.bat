@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - 依存関係インストーラー
echo ===================================================
echo.

echo 🔍 Pythonのバージョンを確認中...
python --version
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo.
    echo Pythonをインストールしてください:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)
echo ✅ Pythonがインストールされています
echo.

echo 🔧 pipをアップグレード中...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ⚠️ pipのアップグレードに失敗しましたが、続行します
)
echo.

echo 📦 基本ライブラリをインストール中...
echo.
echo 1. PyInstaller (exeファイル作成用)
python -m pip install pyinstaller>=5.0.0
if %errorlevel% neq 0 (
    echo ❌ PyInstallerのインストールに失敗しました
    pause
    exit /b 1
)
echo ✅ PyInstallerをインストールしました
echo.

echo 2. Colorama (ログの色付け用)
python -m pip install colorama>=0.4.0
if %errorlevel% neq 0 (
    echo ⚠️ Coloramaのインストールに失敗しましたが、続行します
) else (
    echo ✅ Coloramaをインストールしました
)
echo.

echo 3. tqdm (プログレスバー用)
python -m pip install tqdm>=4.64.0
if %errorlevel% neq 0 (
    echo ⚠️ tqdmのインストールに失敗しましたが、続行します
) else (
    echo ✅ tqdmをインストールしました
)
echo.

echo 4. jsonschema (設定ファイル検証用)
python -m pip install jsonschema>=4.0.0
if %errorlevel% neq 0 (
    echo ⚠️ jsonschemaのインストールに失敗しましたが、続行します
) else (
    echo ✅ jsonschemaをインストールしました
)
echo.

echo 5. Pillow (画像処理用)
python -m pip install Pillow>=9.0.0
if %errorlevel% neq 0 (
    echo ⚠️ Pillowのインストールに失敗しましたが、続行します
) else (
    echo ✅ Pillowをインストールしました
)
echo.

echo 🔍 インストール状況を確認中...
python -c "import pyinstaller; print('✅ PyInstaller:', pyinstaller.__version__)"
python -c "import colorama; print('✅ Colorama:', colorama.__version__)"
python -c "import tqdm; print('✅ tqdm:', tqdm.__version__)"
python -c "import jsonschema; print('✅ jsonschema:', jsonschema.__version__)"
python -c "import PIL; print('✅ Pillow:', PIL.__version__)"
echo.

echo 🎉 依存関係のインストールが完了しました！
echo.
echo 次のステップ:
echo   1. python pack_generator.py でパック生成をテスト
echo   2. build_exe.bat でexeファイルを作成
echo.
echo 何か問題がある場合は、pack_generator.log を確認してください。
echo.
pause 