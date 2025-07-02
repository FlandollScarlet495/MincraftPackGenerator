@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - 配布パッケージ作成ツール
echo ====================================================
echo.

echo 📦 配布用パッケージを作成します...
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo 配布パッケージの作成にはPythonが必要です
    pause
    exit /b 1
)

echo ✅ Pythonが確認されました
echo.

echo 🚀 配布パッケージ作成スクリプトを実行中...
REM 通常版
python create_distribution.py
REM GUI同梱版
python create_distribution.py --with-gui
if %errorlevel% neq 0 (
    echo ❌ 配布パッケージの作成に失敗しました
    pause
    exit /b 1
)

echo.
echo 🎉 配布パッケージの作成が完了しました！
echo.
echo 📦 作成されたファイル:
echo   - MinecraftPackGenerator_v1.0.0_YYYYMMDD.zip (配布用ZIP)
echo   - distribution/ (展開されたファイル)
echo.
echo 📤 配布準備完了！
echo.
echo 📋 配布時のチェックリスト:
echo   □ ZIPファイルのサイズ確認
echo   □ ウイルススキャンの実行
echo   □ 動作確認の実施
echo   □ ドキュメントの確認
echo.
echo 📖 配布方法:
echo   1. ZIPファイルを配布サイトにアップロード
echo   2. ユーザーはZIPをダウンロード・展開
echo   3. install.bat をダブルクリックでインストール
echo.
pause 