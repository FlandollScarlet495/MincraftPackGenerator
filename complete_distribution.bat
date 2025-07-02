@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - 完全配布パッケージ作成ツール
echo =========================================================
echo.

echo 📦 配布パッケージの完全作成を開始します...
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

echo 📋 作成手順:
echo 1. 配布パッケージの作成
echo 2. 品質チェックの実行
echo 3. 最終確認
echo.

echo 🚀 ステップ1: 配布パッケージの作成
echo ----------------------------------------
python create_distribution.py
if %errorlevel% neq 0 (
    echo ❌ 配布パッケージの作成に失敗しました
    pause
    exit /b 1
)
echo ✅ 配布パッケージの作成が完了しました
echo.

echo 🔍 ステップ2: 品質チェックの実行
echo ----------------------------------------
python distribution_checker.py
if %errorlevel% neq 0 (
    echo ❌ 品質チェックに失敗しました
    echo 配布前に問題を修正してください
    pause
    exit /b 1
)
echo ✅ 品質チェックが完了しました
echo.

echo 📊 ステップ3: 最終確認
echo ----------------------------------------
echo 📁 作成されたファイル:
for %%f in (MinecraftPackGenerator_v1.0.0_*.zip) do (
    echo   - %%f (配布用ZIPパッケージ)
)

for %%f in (*_checksums.txt) do (
    echo   - %%f (チェックサムファイル)
)

if exist distribution_manifest.json (
    echo   - distribution_manifest.json (ファイルマニフェスト)
)

echo.
echo 📂 配布ディレクトリ:
if exist distribution (
    echo   - distribution/ (展開されたファイル)
)

echo.
echo 🎉 完全配布パッケージの作成が完了しました！
echo.
echo 📤 配布準備完了！
echo.
echo 📋 配布時のチェックリスト:
echo   □ ZIPファイルのサイズ確認
echo   □ ウイルススキャンの実行
echo   □ 動作確認の実施
echo   □ ドキュメントの確認
echo   □ チェックサムファイルの配布
echo.
echo 📖 配布方法:
echo   1. ZIPファイルを配布サイトにアップロード
echo   2. チェックサムファイルも一緒に配布
echo   3. ユーザーはZIPをダウンロード・展開
echo   4. install.bat をダブルクリックでインストール
echo.
echo 🎯 推奨配布サイト:
echo   - GitHub Releases
echo   - itch.io
echo   - CurseForge
echo   - Planet Minecraft
echo.
echo 📞 サポート情報:
echo   - ログファイル: pack_generator.log
echo   - ドキュメント: docs/
echo   - サンプル: examples/
echo.
pause 