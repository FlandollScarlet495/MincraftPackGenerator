@echo off
chcp 65001 >nul
echo 🚀 Minecraft Pack Generator - GitHub配布セットアップツール
echo =========================================================
echo.

echo 📦 GitHub配布の準備を開始します...
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo GitHub配布のセットアップにはPythonが必要です
    pause
    exit /b 1
)

echo ✅ Pythonが確認されました
echo.

echo 📋 セットアップ手順:
echo 1. GitHub配布用ファイルの作成
echo 2. 配布パッケージの作成
echo 3. 品質チェックの実行
echo 4. 最終確認
echo.

echo 🚀 ステップ1: GitHub配布用ファイルの作成
echo ----------------------------------------
python github_release_creator.py
if %errorlevel% neq 0 (
    echo ❌ GitHub配布用ファイルの作成に失敗しました
    pause
    exit /b 1
)
echo ✅ GitHub配布用ファイルの作成が完了しました
echo.

echo 📦 ステップ2: 配布パッケージの作成
echo ----------------------------------------
python create_distribution.py
if %errorlevel% neq 0 (
    echo ❌ 配布パッケージの作成に失敗しました
    pause
    exit /b 1
)
echo ✅ 配布パッケージの作成が完了しました
echo.

echo 🔍 ステップ3: 品質チェックの実行
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

echo 📊 ステップ4: 最終確認
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

if exist RELEASE_NOTES.md (
    echo   - RELEASE_NOTES.md (リリースノート)
)

echo.
echo 📂 GitHub用ファイル:
if exist .github (
    echo   - .github/ (GitHub設定ファイル)
)

if exist README.md (
    echo   - README.md (GitHub用README)
)

if exist LICENSE (
    echo   - LICENSE (ライセンスファイル)
)

echo.
echo 🎉 GitHub配布セットアップが完了しました！
echo.
echo 📤 GitHub配布準備完了！
echo.
echo 📋 GitHub配布手順:
echo   1. GitHubでリポジトリを作成
echo   2. ローカルリポジトリを初期化
echo   3. ファイルをコミット・プッシュ
echo   4. タグを作成 (v1.0.0)
echo   5. GitHub Actionsが自動実行
echo   6. Releasesページで確認
echo.
echo 🔧 詳細な手順:
echo.
echo 1. GitHubでリポジトリ作成:
echo    - GitHub.com にアクセス
echo    - "New repository" をクリック
echo    - リポジトリ名: minecraft-pack-generator
echo    - Public/Private を選択
echo    - "Create repository" をクリック
echo.
echo 2. ローカルリポジトリ初期化:
echo    git init
echo    git add .
echo    git commit -m "Initial commit"
echo    git branch -M main
echo    git remote add origin https://github.com/yourusername/minecraft-pack-generator.git
echo    git push -u origin main
echo.
echo 3. タグ作成とリリース:
echo    git tag v1.0.0
echo    git push origin v1.0.0
echo.
echo 4. GitHub Actions確認:
echo    - Actions タブでビルド状況を確認
echo    - Releases タブでリリースを確認
echo.
echo 🎯 推奨設定:
echo   - リポジトリ名: minecraft-pack-generator
echo   - 説明: MinecraftのResourcePackとDataPackを自動生成するツール
echo   - トピック: minecraft, datapack, resourcepack, generator, python
echo   - ライセンス: MIT
echo.
echo 📞 サポート情報:
echo   - ログファイル: pack_generator.log
echo   - ドキュメント: docs/
echo   - サンプル: examples/
echo.
pause 