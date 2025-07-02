#!/usr/bin/env python3
"""
Minecraft Pack Generator - 配布パッケージ作成ツール
"""

import os
import shutil
import zipfile
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import argparse

def create_directory_structure():
    """配布用のディレクトリ構造を作成"""
    print("📁 配布用ディレクトリ構造を作成中...")
    
    # 配布用ディレクトリ
    dist_dir = Path("distribution")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # サブディレクトリ
    (dist_dir / "MinecraftPackGenerator").mkdir()
    (dist_dir / "MinecraftPackGenerator" / "examples").mkdir()
    (dist_dir / "MinecraftPackGenerator" / "templates").mkdir()
    (dist_dir / "MinecraftPackGenerator" / "docs").mkdir()
    
    print("✅ ディレクトリ構造を作成しました")
    return dist_dir

def copy_main_files(dist_dir):
    """メインファイルをコピー"""
    print("📋 メインファイルをコピー中...")
    
    main_files = [
        "pack_generator.py",
        "packdata.json",
        "requirements.txt",
        "README.txt"
    ]
    
    for file in main_files:
        if Path(file).exists():
            shutil.copy2(file, dist_dir / "MinecraftPackGenerator")
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} が見つかりません")
    
    print("✅ メインファイルをコピーしました")

def copy_installation_files(dist_dir):
    """インストール関連ファイルをコピー"""
    print("🔧 インストールファイルをコピー中...")
    
    install_files = [
        "install_dependencies.bat",
        "install_dependencies.py",
        "setup.py",
        "quick_start.bat"
    ]
    
    for file in install_files:
        if Path(file).exists():
            shutil.copy2(file, dist_dir / "MinecraftPackGenerator")
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} が見つかりません")
    
    print("✅ インストールファイルをコピーしました")

def copy_build_files(dist_dir):
    """ビルド関連ファイルをコピー"""
    print("🔨 ビルドファイルをコピー中...")
    
    build_files = [
        "build_exe.bat",
        "build_exe.py"
    ]
    
    for file in build_files:
        if Path(file).exists():
            shutil.copy2(file, dist_dir / "MinecraftPackGenerator")
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} が見つかりません")
    
    print("✅ ビルドファイルをコピーしました")

def create_example_files(dist_dir):
    """サンプルファイルを作成"""
    print("📝 サンプルファイルを作成中...")
    
    # サンプル設定ファイル
    example_config = {
        "pack_info": {
            "name": "サンプルパック",
            "version": "1.0.0",
            "author": "ユーザー名",
            "description": "サンプルパックの説明"
        },
        "items": [
            {
                "id": "sample_sword",
                "name": "サンプル剣",
                "damage": 10,
                "durability": 1000,
                "enchantments": ["sharpness"],
                "texture": "textures/items/sample_sword.png",
                "lore": "サンプルアイテム",
                "rarity": "common"
            }
        ],
        "spells": [
            {
                "id": "sample_spell",
                "name": "サンプルスペル",
                "description": "サンプルスペルの説明",
                "commands": [
                    "say サンプルスペル発動！",
                    "particle minecraft:flame ~ ~1 ~ 0.5 0.5 0.5 0 10 force"
                ],
                "cooldown": 10,
                "mana_cost": 20,
                "range": 5
            }
        ]
    }
    
    import json
    with open(dist_dir / "MinecraftPackGenerator" / "examples" / "sample_config.json", "w", encoding="utf-8") as f:
        json.dump(example_config, f, indent=2, ensure_ascii=False)
    
    # サンプルテクスチャ（ダミー）
    sample_texture_dir = dist_dir / "MinecraftPackGenerator" / "examples" / "textures"
    sample_texture_dir.mkdir(exist_ok=True)
    
    with open(sample_texture_dir / "sample_sword.png", "w") as f:
        f.write("# これはダミーファイルです\n# 実際のテクスチャファイルに置き換えてください")
    
    print("✅ サンプルファイルを作成しました")

def create_templates(dist_dir):
    """テンプレートファイルを作成"""
    print("📋 テンプレートファイルを作成中...")
    
    templates = [
        ("basic_template.json", "基本的なテンプレート"),
        ("magic_template.json", "魔法系テンプレート"),
        ("weapon_template.json", "武器系テンプレート")
    ]
    
    for template_name, description in templates:
        template_data = {
            "pack_info": {
                "name": f"{description}",
                "version": "1.0.0",
                "author": "ユーザー名",
                "description": f"{description}のテンプレート"
            },
            "items": [],
            "spells": []
        }
        
        import json
        with open(dist_dir / "MinecraftPackGenerator" / "templates" / template_name, "w", encoding="utf-8") as f:
            json.dump(template_data, f, indent=2, ensure_ascii=False)
    
    print("✅ テンプレートファイルを作成しました")

def create_documentation(dist_dir):
    """ドキュメントを作成"""
    print("📖 ドキュメントを作成中...")
    
    # インストールガイド
    install_guide = """# Minecraft Pack Generator - インストールガイド

## 必要な環境
- Windows 10/11
- Python 3.7以上

## インストール手順

### 1. クイックスタート（推奨）
1. `quick_start.bat` をダブルクリック
2. 画面の指示に従ってセットアップ

### 2. 手動インストール
1. `install_dependencies.bat` を実行
2. `python pack_generator.py --preview` でテスト

### 3. exeファイル作成
1. `build_exe.bat` を実行
2. `dist/MinecraftPackGenerator.exe` が作成されます

## 使用方法
- `python pack_generator.py` - 基本的なパック生成
- `python pack_generator.py --template my_pack` - テンプレート作成
- `python pack_generator.py --validate` - 設定検証
- `python pack_generator.py --preview` - プレビュー表示

## トラブルシューティング
エラーが発生した場合は、`pack_generator.log` を確認してください。
"""
    
    with open(dist_dir / "MinecraftPackGenerator" / "docs" / "INSTALL_GUIDE.txt", "w", encoding="utf-8") as f:
        f.write(install_guide)
    
    # 使用方法ガイド
    usage_guide = """# Minecraft Pack Generator - 使用方法ガイド

## 基本的な使用方法

### 1. 設定ファイルの作成
`packdata.json` を編集して、カスタムアイテムやスペルを追加します。

### 2. パックの生成
```bash
python pack_generator.py
```

### 3. 生成されたファイル
- `datapack.zip` - データパック
- `resourcepack.zip` - リソースパック
- `output/` - 展開されたファイル

## 設定ファイルの構造

### pack_info
パックの基本情報を設定します。

### items
カスタムアイテムを定義します。

### spells
カスタムスペルを定義します。

## テンプレートの使用
```bash
python pack_generator.py --template my_pack
```

## 設定の検証
```bash
python pack_generator.py --validate
```

## プレビュー表示
```bash
python pack_generator.py --preview
```
"""
    
    with open(dist_dir / "MinecraftPackGenerator" / "docs" / "USAGE_GUIDE.txt", "w", encoding="utf-8") as f:
        f.write(usage_guide)
    
    print("✅ ドキュメントを作成しました")

def create_installer_script(dist_dir):
    """インストーラースクリプトを作成"""
    print("🚀 インストーラースクリプトを作成中...")
    
    installer_content = """@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - インストーラー
echo ============================================
echo.

echo 👋 Minecraft Pack Generatorへようこそ！
echo.
echo このツールは、MinecraftのResourcePackとDataPackを
echo 簡単に作成できるツールです。
echo.

echo 📋 インストール手順:
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
    echo インストール後、このインストーラーを再実行してください。
    echo.
    pause
    exit /b 1
)
echo ✅ Pythonがインストールされています
echo.

echo 📦 必要なライブラリをインストールします...
call install_dependencies.bat
if %errorlevel% neq 0 (
    echo ❌ 依存関係のインストールに失敗しました
    pause
    exit /b 1
)

echo.
echo 🧪 パック生成をテストします...
python pack_generator.py --preview
if %errorlevel% neq 0 (
    echo ❌ パック生成のテストに失敗しました
    echo pack_generator.log を確認してください
    pause
    exit /b 1
)
echo ✅ パック生成のテストが成功しました！

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
    echo ✅ exeファイルの作成が完了しました！
    echo dist\\MinecraftPackGenerator.exe が使用可能です
)

echo.
echo 🎉 インストールが完了しました！
echo.
echo 📚 使用方法:
echo   - python pack_generator.py でパック生成
echo   - python pack_generator.py --help でヘルプ表示
echo   - または dist\\MinecraftPackGenerator.exe を使用
echo.
echo 📁 生成されるファイル:
echo   - datapack.zip (データパック)
echo   - resourcepack.zip (リソースパック)
echo   - output\\ (展開されたファイル)
echo.
echo 📖 詳細な使用方法は docs\\ フォルダを参照してください
echo.
echo 何か問題がある場合は、pack_generator.log を確認してください。
echo.
pause
"""
    
    with open(dist_dir / "MinecraftPackGenerator" / "install.bat", "w", encoding="utf-8") as f:
        f.write(installer_content)
    
    print("✅ インストーラースクリプトを作成しました")

def create_readme(dist_dir):
    """配布用READMEを作成"""
    print("📖 配布用READMEを作成中...")
    
    readme_content = f"""# Minecraft Pack Generator v1.0.0

MinecraftのResourcePackとDataPackを自動生成するツールです。

## 🚀 クイックスタート

1. **install.bat** をダブルクリック
2. 画面の指示に従ってセットアップ
3. パック生成を開始！

## 📁 ファイル構成

```
MinecraftPackGenerator/
├── install.bat              # インストーラー
├── pack_generator.py        # メインプログラム
├── packdata.json           # 設定ファイル
├── examples/               # サンプルファイル
├── templates/              # テンプレート
├── docs/                   # ドキュメント
└── [その他のファイル]
```

## 📚 使用方法

### 基本的な使用方法
```bash
python pack_generator.py
```

### テンプレート作成
```bash
python pack_generator.py --template my_pack
```

### 設定検証
```bash
python pack_generator.py --validate
```

### プレビュー表示
```bash
python pack_generator.py --preview
```

## 🎮 生成されるファイル

- `datapack.zip` - データパック
- `resourcepack.zip` - リソースパック
- `output/` - 展開されたファイル
- `pack_generator.log` - ログファイル

## 📖 ドキュメント

- `docs/INSTALL_GUIDE.txt` - インストールガイド
- `docs/USAGE_GUIDE.txt` - 使用方法ガイド

## 🛠️ 必要な環境

- Windows 10/11
- Python 3.7以上

## 📞 サポート

問題が発生した場合は、`pack_generator.log` を確認してください。

## 👤 作者

けんすけ

## 📅 作成日

{datetime.now().strftime('%Y年%m月%d日')}

---
Minecraft Pack Generator v1.0.0
"""
    
    with open(dist_dir / "MinecraftPackGenerator" / "README.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ 配布用READMEを作成しました")

def create_zip_package(dist_dir):
    """ZIPパッケージを作成"""
    print("📦 ZIPパッケージを作成中...")
    
    zip_name = f"MinecraftPackGenerator_v1.0.0_{datetime.now().strftime('%Y%m%d')}.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = Path(root) / file
                arc_name = file_path.relative_to(dist_dir)
                zipf.write(file_path, arc_name)
    
    print(f"✅ ZIPパッケージを作成しました: {zip_name}")
    return zip_name

def main():
    parser = argparse.ArgumentParser(description='配布パッケージ作成ツール')
    parser.add_argument('--with-gui', action='store_true', help='GUI版も同梱する')
    args = parser.parse_args()

    print("🎮 Minecraft Pack Generator - 配布パッケージ作成ツール")
    print("=" * 60)
    print()
    
    # ディレクトリ構造作成
    dist_dir = create_directory_structure()
    
    # ファイルコピー
    copy_main_files(dist_dir)
    copy_installation_files(dist_dir)
    copy_build_files(dist_dir)
    
    # サンプルとテンプレート作成
    create_example_files(dist_dir)
    create_templates(dist_dir)
    
    # ドキュメント作成
    create_documentation(dist_dir)
    
    # インストーラー作成
    create_installer_script(dist_dir)
    
    # README作成
    create_readme(dist_dir)
    
    # ZIPパッケージ作成
    if args.with_gui:
        # gui_generator.pyを同梱
        shutil.copy('gui_generator.py', os.path.join(dist_dir, 'gui_generator.py'))
        zip_name = f"MinecraftPackGenerator_v{datetime.now().strftime('%Y%m%d')}_with_gui.zip"
    else:
        # gui_generator.pyを除外
        zip_name = f"MinecraftPackGenerator_v{datetime.now().strftime('%Y%m%d')}_nogui.zip"
    create_zip_package(dist_dir)
    
    print()
    print("🎉 配布パッケージの作成が完了しました！")
    print()
    print("📦 作成されたファイル:")
    print(f"  - {zip_name} (配布用ZIPパッケージ)")
    print(f"  - {dist_dir} (展開されたファイル)")
    print()
    print("📤 配布方法:")
    print("  1. ZIPファイルを配布")
    print("  2. ユーザーはZIPを展開")
    print("  3. install.bat を実行")
    print()
    print("📖 配布時の注意事項:")
    print("  - ファイルサイズを確認")
    print("  - ウイルススキャンを実行")
    print("  - 動作確認を実施")
    print()

if __name__ == "__main__":
    main() 