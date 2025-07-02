@echo off
chcp 65001 >nul
echo 🐍 Minecraft Pack Generator - Python版配布パッケージ作成ツール
echo ============================================================
echo.

echo 📦 Python版配布パッケージを作成します...
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo Python版配布パッケージの作成にはPythonが必要です
    pause
    exit /b 1
)

echo ✅ Pythonが確認されました
echo.

echo 🚀 Python版配布パッケージ作成スクリプトを実行中...
python create_python_distribution.py
if %errorlevel% neq 0 (
    echo ❌ Python版配布パッケージの作成に失敗しました
    pause
    exit /b 1
)

echo.
echo 🎉 Python版配布パッケージの作成が完了しました！
echo.
echo 📦 作成されたファイル:
echo   - MinecraftPackGenerator-Python_v1.0.0_YYYYMMDD.zip (Python版配布用ZIP)
echo   - python_distribution/ (展開されたファイル)
echo.
echo 📤 配布準備完了！
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
echo 📖 配布方法:
echo   1. ZIPファイルをGitHub Releasesにアップロード
echo   2. ユーザーはZIPをダウンロード・展開
echo   3. install.sh (Linux/Mac) または install.bat (Windows) を実行
echo.
pause 