@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - クイックスタート
echo ============================================
echo.

echo 👋 ようこそ！Minecraft Pack Generatorへ
echo.
echo このツールは、MinecraftのResourcePackとDataPackを
echo 簡単に作成できるツールです。
echo.

echo 📋 セットアップ手順:
echo.
echo 1. Pythonのインストール確認
echo 2. 必要なライブラリのインストール
echo 3. パック生成のテスト
echo 4. exeファイルの作成（オプション）
echo.

echo 🔍 Pythonのインストールを確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo.
    echo Pythonをインストールしてください:
    echo https://www.python.org/downloads/
    echo.
    echo インストール後、このバッチファイルを再実行してください。
    echo.
    pause
    exit /b 1
)
echo ✅ Pythonがインストールされています
echo.

echo 📦 必要なライブラリをインストールしますか？ (Y/N)
set /p choice="選択してください: "
if /i "%choice%"=="Y" (
    echo.
    echo 🔧 依存関係インストーラーを実行中...
    call install_dependencies.bat
    if %errorlevel% neq 0 (
        echo ❌ 依存関係のインストールに失敗しました
        pause
        exit /b 1
    )
) else (
    echo.
    echo ⚠️ ライブラリのインストールをスキップしました
    echo 後で install_dependencies.bat を実行してください
)

echo.
echo 🧪 パック生成をテストしますか？ (Y/N)
set /p choice="選択してください: "
if /i "%choice%"=="Y" (
    echo.
    echo 🚀 パック生成をテスト中...
    python pack_generator.py --preview
    if %errorlevel% neq 0 (
        echo ❌ パック生成のテストに失敗しました
        echo pack_generator.log を確認してください
        pause
        exit /b 1
    )
    echo.
    echo ✅ パック生成のテストが成功しました！
)

echo.
echo 🎯 exeファイルを作成しますか？ (Y/N)
set /p choice="選択してください: "
if /i "%choice%"=="Y" (
    echo.
    echo 🔨 exeファイルを作成中...
    call build_exe.bat
    if %errorlevel% neq 0 (
        echo ❌ exeファイルの作成に失敗しました
        pause
        exit /b 1
    )
    echo.
    echo ✅ exeファイルの作成が完了しました！
    echo dist\MinecraftPackGenerator.exe が使用可能です
)

echo.
echo 🎉 セットアップが完了しました！
echo.
echo 📚 使用方法:
echo   - python pack_generator.py でパック生成
echo   - python pack_generator.py --help でヘルプ表示
echo   - または dist\MinecraftPackGenerator.exe を使用
echo.
echo 📁 生成されるファイル:
echo   - datapack.zip (データパック)
echo   - resourcepack.zip (リソースパック)
echo   - output\ (展開されたファイル)
echo.
echo 📖 詳細な使用方法は README.txt を参照してください
echo.
echo 何か問題がある場合は、pack_generator.log を確認してください。
echo.
pause 