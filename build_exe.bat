@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - Windows exe ビルダー
echo ================================================
echo.

echo 🔧 PyInstallerをインストール中...
python -m pip install pyinstaller
if %errorlevel% neq 0 (
    echo ❌ PyInstallerのインストールに失敗しました
    pause
    exit /b 1
)
echo ✅ PyInstallerのインストールが完了しました
echo.

echo 🚀 exeファイルのビルドを開始します...
pyinstaller --onefile --windowed --name=MinecraftPackGenerator --add-data=packdata.json;. --hidden-import=pathlib --hidden-import=typing --hidden-import=json --hidden-import=logging --hidden-import=argparse --hidden-import=zipfile --hidden-import=shutil pack_generator.py
if %errorlevel% neq 0 (
    echo ❌ exeファイルのビルドに失敗しました
    pause
    exit /b 1
)
echo ✅ exeファイルのビルドが完了しました
echo.

echo 📝 バッチファイルを作成中...
echo @echo off > run_generator.bat
echo echo Minecraft Pack Generator >> run_generator.bat
echo echo ======================== >> run_generator.bat
echo echo. >> run_generator.bat
echo echo 使用方法: >> run_generator.bat
echo echo   MinecraftPackGenerator.exe                    - 基本的なパック生成 >> run_generator.bat
echo echo   MinecraftPackGenerator.exe --template my_pack - テンプレート作成 >> run_generator.bat
echo echo   MinecraftPackGenerator.exe --validate         - 設定検証 >> run_generator.bat
echo echo   MinecraftPackGenerator.exe --preview          - プレビュー表示 >> run_generator.bat
echo echo. >> run_generator.bat
echo echo 詳細な使用方法は README.txt を参照してください >> run_generator.bat
echo echo. >> run_generator.bat
echo pause >> run_generator.bat
echo ✅ バッチファイルを作成しました: run_generator.bat
echo.

echo 📖 READMEファイルを作成中...
echo # Minecraft Pack Generator > README.txt
echo. >> README.txt
echo MinecraftのResourcePackとDataPackを自動生成するツールです。 >> README.txt
echo. >> README.txt
echo ## 使用方法 >> README.txt
echo. >> README.txt
echo ### 基本的な使用方法 >> README.txt
echo MinecraftPackGenerator.exe >> README.txt
echo. >> README.txt
echo ### テンプレート作成 >> README.txt
echo MinecraftPackGenerator.exe --template my_pack >> README.txt
echo. >> README.txt
echo ### 設定ファイルの検証 >> README.txt
echo MinecraftPackGenerator.exe --validate >> README.txt
echo. >> README.txt
echo ### パックのプレビュー表示 >> README.txt
echo MinecraftPackGenerator.exe --preview >> README.txt
echo. >> README.txt
echo ## 生成されるファイル >> README.txt
echo. >> README.txt
echo - datapack.zip - データパック >> README.txt
echo - resourcepack.zip - リソースパック >> README.txt
echo - output/ - 展開されたファイル >> README.txt
echo - pack_generator.log - ログファイル >> README.txt
echo. >> README.txt
echo ## 作者 >> README.txt
echo. >> README.txt
echo けんすけ >> README.txt
echo ✅ READMEファイルを作成しました: README.txt
echo.

echo 🧹 不要なファイルを削除中...
if exist build rmdir /s /q build
if exist MinecraftPackGenerator.spec del MinecraftPackGenerator.spec
echo ✅ 不要なファイルを削除しました
echo.

echo 🎉 ビルドが完了しました！
echo.
echo 生成されたファイル:
echo   - dist\MinecraftPackGenerator.exe (メイン実行ファイル)
echo   - run_generator.bat (簡単実行用バッチファイル)
echo   - README.txt (使用方法)
echo.
echo 使用方法:
echo   1. dist\MinecraftPackGenerator.exe を実行
echo   2. または run_generator.bat をダブルクリック
echo.
pause 