import os
import subprocess
import sys
from pathlib import Path

def install_pyinstaller():
    """PyInstallerをインストールする"""
    print("🔧 PyInstallerをインストール中...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstallerのインストールが完了しました")
        return True
    except subprocess.CalledProcessError:
        print("❌ PyInstallerのインストールに失敗しました")
        return False

def build_exe():
    """exeファイルをビルドする"""
    print("🚀 exeファイルのビルドを開始します...")
    
    # ビルドコマンド
    cmd = [
        "pyinstaller",
        "--onefile",  # 単一ファイルにまとめる
        "--windowed",  # コンソールウィンドウを非表示
        "--name=MinecraftPackGenerator",  # exeファイル名
        "--icon=icon.ico",  # アイコンファイル（存在する場合）
        "--add-data=packdata.json;.",  # 設定ファイルを含める
        "--hidden-import=pathlib",
        "--hidden-import=typing",
        "--hidden-import=json",
        "--hidden-import=logging",
        "--hidden-import=argparse",
        "--hidden-import=zipfile",
        "--hidden-import=shutil",
        "pack_generator.py"
    ]
    
    try:
        # アイコンファイルが存在しない場合は除外
        if not os.path.exists("icon.ico"):
            cmd = [arg for arg in cmd if not arg.startswith("--icon")]
        
        subprocess.check_call(cmd)
        print("✅ exeファイルのビルドが完了しました")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ exeファイルのビルドに失敗しました: {e}")
        return False

def create_icon():
    """簡単なアイコンファイルを作成する（オプション）"""
    print("🎨 アイコンファイルを作成中...")
    
    # 簡単なテキストベースのアイコン（実際のアイコンではないが、エラーを避けるため）
    icon_content = """
    # これは実際のアイコンファイルではありません
    # 実際の使用では、.icoファイルを用意してください
    """
    
    try:
        with open("icon.ico", "w") as f:
            f.write(icon_content)
        print("✅ アイコンファイルを作成しました（ダミー）")
        return True
    except Exception as e:
        print(f"⚠️ アイコンファイルの作成に失敗しました: {e}")
        return False

def create_batch_file():
    """簡単に実行できるバッチファイルを作成する"""
    print("📝 バッチファイルを作成中...")
    
    batch_content = """@echo off
echo Minecraft Pack Generator
echo ========================
echo.
echo 使用方法:
echo   MinecraftPackGenerator.exe                    - 基本的なパック生成
echo   MinecraftPackGenerator.exe --template my_pack - テンプレート作成
echo   MinecraftPackGenerator.exe --validate         - 設定検証
echo   MinecraftPackGenerator.exe --preview          - プレビュー表示
echo.
echo 詳細な使用方法は README.txt を参照してください
echo.
pause
"""
    
    try:
        with open("run_generator.bat", "w", encoding="utf-8") as f:
            f.write(batch_content)
        print("✅ バッチファイルを作成しました: run_generator.bat")
        return True
    except Exception as e:
        print(f"❌ バッチファイルの作成に失敗しました: {e}")
        return False

def create_readme():
    """READMEファイルを作成する"""
    print("📖 READMEファイルを作成中...")
    
    readme_content = """# Minecraft Pack Generator

MinecraftのResourcePackとDataPackを自動生成するツールです。

## 使用方法

### 基本的な使用方法
```
MinecraftPackGenerator.exe
```

### テンプレート作成
```
MinecraftPackGenerator.exe --template my_pack
```

### 設定ファイルの検証
```
MinecraftPackGenerator.exe --validate
```

### パックのプレビュー表示
```
MinecraftPackGenerator.exe --preview
```

### カスタム設定ファイルを使用
```
MinecraftPackGenerator.exe --config my_config.json
```

## 生成されるファイル

- `datapack.zip` - データパック
- `resourcepack.zip` - リソースパック
- `output/` - 展開されたファイル
- `pack_generator.log` - ログファイル

## 設定ファイル

`packdata.json` を編集して、カスタムアイテムやスペルを追加できます。

## 必要なファイル

- `packdata.json` - 設定ファイル（自動生成されます）
- テクスチャファイル（設定で指定）

## トラブルシューティング

エラーが発生した場合は、`pack_generator.log` を確認してください。

## 作者

けんすけ
"""
    
    try:
        with open("README.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("✅ READMEファイルを作成しました: README.txt")
        return True
    except Exception as e:
        print(f"❌ READMEファイルの作成に失敗しました: {e}")
        return False

def main():
    """メイン処理"""
    print("🎮 Minecraft Pack Generator - Windows exe ビルダー")
    print("=" * 50)
    
    # PyInstallerのインストール
    if not install_pyinstaller():
        print("❌ PyInstallerのインストールに失敗しました")
        return
    
    # アイコンファイルの作成（オプション）
    create_icon()
    
    # exeファイルのビルド
    if not build_exe():
        print("❌ exeファイルのビルドに失敗しました")
        return
    
    # バッチファイルの作成
    create_batch_file()
    
    # READMEファイルの作成
    create_readme()
    
    print("\n🎉 ビルドが完了しました！")
    print("生成されたファイル:")
    print("  - dist/MinecraftPackGenerator.exe (メイン実行ファイル)")
    print("  - run_generator.bat (簡単実行用バッチファイル)")
    print("  - README.txt (使用方法)")
    print("\n使用方法:")
    print("  1. dist/MinecraftPackGenerator.exe を実行")
    print("  2. または run_generator.bat をダブルクリック")
    
    # 不要なファイルの削除
    print("\n🧹 不要なファイルを削除中...")
    try:
        if os.path.exists("build"):
            import shutil
            shutil.rmtree("build")
        if os.path.exists("MinecraftPackGenerator.spec"):
            os.remove("MinecraftPackGenerator.spec")
        print("✅ 不要なファイルを削除しました")
    except Exception as e:
        print(f"⚠️ 不要なファイルの削除に失敗しました: {e}")

if __name__ == "__main__":
    main() 