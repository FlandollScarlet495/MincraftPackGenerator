@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - 全プラットフォーム配布パッケージ作成ツール
echo ====================================================================
echo.

echo 📦 全プラットフォーム用の配布パッケージを作成します...
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
echo 1. Windows版配布パッケージの作成
echo 2. Python版配布パッケージの作成
echo 3. 最終確認
echo.

echo 🚀 ステップ1: Windows版配布パッケージの作成
echo ----------------------------------------
python create_distribution.py
if %errorlevel% neq 0 (
    echo ❌ Windows版配布パッケージの作成に失敗しました
    pause
    exit /b 1
)
echo ✅ Windows版配布パッケージの作成が完了しました
echo.

echo 🐍 ステップ2: Python版配布パッケージの作成
echo ----------------------------------------
python create_python_distribution.py
if %errorlevel% neq 0 (
    echo ❌ Python版配布パッケージの作成に失敗しました
    pause
    exit /b 1
)
echo ✅ Python版配布パッケージの作成が完了しました
echo.

echo 📊 ステップ3: 最終確認
echo ----------------------------------------
echo 📁 作成されたファイル:
for %%f in (MinecraftPackGenerator_v1.0.0_*.zip) do (
    echo   - %%f (Windows版配布用ZIPパッケージ)
)

for %%f in (MinecraftPackGenerator-Python_v1.0.0_*.zip) do (
    echo   - %%f (Python版配布用ZIPパッケージ)
)

for %%f in (*_checksums.txt) do (
    echo   - %%f (チェックサムファイル)
)

if exist distribution_manifest.json (
    echo   - distribution_manifest.json (ファイルマニフェスト)
)

if exist RELEASE_NOTES.md (
    echo   - RELEASE_NOTES.md (リリースノート)
)

echo.
echo 📂 配布ディレクトリ:
if exist distribution (
    echo   - distribution/ (Windows版展開ファイル)
)

if exist python_distribution (
    echo   - python_distribution/ (Python版展開ファイル)
)

echo.
echo 🎉 全プラットフォーム配布パッケージの作成が完了しました！
echo.
echo 📤 配布準備完了！
echo.
echo 🌍 対応プラットフォーム:
echo   - Windows (exe版 + Python版)
echo   - macOS (Python版)
echo   - Linux (Python版)
echo.
echo 📋 配布時のチェックリスト:
echo   □ ZIPファイルのサイズ確認
echo   □ ウイルススキャンの実行
echo   □ 動作確認の実施
echo   □ ドキュメントの確認
echo   □ チェックサムファイルの配布
echo.
echo 📖 GitHub配布方法:
echo   1. GitHub Releasesページにアクセス
echo   2. 新しいリリースを作成 (v1.0.0)
echo   3. 両方のZIPファイルをアップロード
echo   4. チェックサムファイルもアップロード
echo   5. リリースノートを設定
echo.
echo 🎯 推奨配布サイト:
echo   - GitHub Releases (推奨)
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