@echo off
chcp 65001 >nul
echo 🔍 Minecraft Pack Generator - 配布パッケージ品質チェックツール
echo ============================================================
echo.

echo 📦 配布パッケージの品質をチェックします...
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo 品質チェックにはPythonが必要です
    pause
    exit /b 1
)

echo ✅ Pythonが確認されました
echo.

echo 🚀 品質チェックスクリプトを実行中...
python distribution_checker.py
if %errorlevel% neq 0 (
    echo ❌ 品質チェックに失敗しました
    pause
    exit /b 1
)

echo.
echo 🎉 品質チェックが完了しました！
echo.
echo 📋 チェック結果:
echo   - ファイル構造の確認
echo   - ファイルサイズの確認
echo   - Python構文の確認
echo   - JSON構文の確認
echo   - バッチファイルの確認
echo   - ZIPファイルの整合性確認
echo   - チェックサムファイルの生成
echo.
echo 📤 配布準備完了！
echo.
echo 📖 配布時の注意事項:
echo   - ウイルススキャンを実行
echo   - 複数の環境で動作確認
echo   - ドキュメントの最終確認
echo   - チェックサムファイルも一緒に配布
echo.
pause 