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
    echo Python 3.7以上をインストールしてください
    pause
    exit /b 1
)
echo ✅ Pythonが確認されました
echo.

echo 🚀 ステップ1: Windows版配布パッケージの作成
echo ----------------------------------------
echo 📦 通常版（GUIなし）を作成中...
python create_distribution.py
if %errorlevel% neq 0 (
    echo ❌ Windows版通常版の作成に失敗しました
    pause
    exit /b 1
)

echo 📦 GUI同梱版を作成中...
python create_distribution.py --with-gui
if %errorlevel% neq 0 (
    echo ❌ Windows版GUI同梱版の作成に失敗しました
    pause
    exit /b 1
)

echo ✅ Windows版配布パッケージの作成が完了しました
echo.

echo 🐍 ステップ2: Python版配布パッケージの作成
echo ----------------------------------------
echo 📦 通常版（GUIなし）を作成中...
python create_python_distribution.py
if %errorlevel% neq 0 (
    echo ❌ Python版通常版の作成に失敗しました
    pause
    exit /b 1
)

echo 📦 GUI同梱版を作成中...
python create_python_distribution.py --with-gui
if %errorlevel% neq 0 (
    echo ❌ Python版GUI同梱版の作成に失敗しました
    pause
    exit /b 1
)

echo ✅ Python版配布パッケージの作成が完了しました
echo.

echo 📊 ステップ3: 最終確認
echo ----------------------------------------
echo 📁 作成されたファイル:
echo   Windows版:
echo     - MinecraftPackGenerator_vYYYYMMDD_nogui.zip (通常版)
echo     - MinecraftPackGenerator_vYYYYMMDD_with_gui.zip (GUI同梱版)
echo   Python版:
echo     - MinecraftPackGenerator-Python_v1.1.0_YYYYMMDD_nogui.zip (通常版)
echo     - MinecraftPackGenerator-Python_v1.1.0_YYYYMMDD_with_gui.zip (GUI同梱版)
echo.

echo 📂 配布ディレクトリ:
echo   - distribution/ (Windows版展開ファイル)
echo   - distribution_with_gui/ (Windows版GUI同梱展開ファイル)
echo   - python_distribution_nogui/ (Python版展開ファイル)
echo   - python_distribution_with_gui/ (Python版GUI同梱展開ファイル)
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
echo   2. 新しいリリースを作成 (v1.1.0)
echo   3. 4つのZIPファイルをアップロード
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