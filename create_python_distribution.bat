@echo off
chcp 65001 >nul
echo 🐍 Minecraft Pack Generator - Python版配布パッケージ作成ツール
echo ============================================================
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo Python 3.7以上をインストールしてください
    pause
    exit /b 1
)
echo ✅ Pythonが確認されました
echo.

echo 🚀 Python版配布パッケージ作成スクリプトを実行中...

REM 通常版（GUIなし）
echo.
echo 📦 通常版（GUIなし）を作成中...
python create_python_distribution.py
if %errorlevel% neq 0 (
    echo ❌ 通常版の作成に失敗しました
    pause
    exit /b 1
)

REM GUI同梱版
echo.
echo 📦 GUI同梱版を作成中...
python create_python_distribution.py --with-gui
if %errorlevel% neq 0 (
    echo ❌ GUI同梱版の作成に失敗しました
    pause
    exit /b 1
)

echo.
echo 🎉 Python版配布パッケージの作成が完了しました！
echo.
echo 📦 作成されたファイル:
echo   - MinecraftPackGenerator-Python_v1.1.0_YYYYMMDD_nogui.zip (通常版)
echo   - MinecraftPackGenerator-Python_v1.1.0_YYYYMMDD_with_gui.zip (GUI同梱版)
echo.
echo 📤 配布方法:
echo   1. ZIPファイルをGitHub Releasesにアップロード
echo   2. ユーザーはZIPを展開
echo   3. install.sh (Linux/Mac) または install.bat (Windows) を実行
echo.
echo 🌍 対応プラットフォーム:
echo   - Windows (Python 3.7+)
echo   - macOS (Python 3.7+)
echo   - Linux (Python 3.7+)
echo.
echo 📋 配布時のチェックリスト:
echo   □ ZIPファイルのサイズ確認
echo   □ ウイルススキャンの実行
echo   □ 動作確認の実施
echo   □ ドキュメントの確認
echo.
pause 