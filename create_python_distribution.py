#!/usr/bin/env python3
"""
Minecraft Pack Generator - Python版配布パッケージ作成ツール
"""

import os
import shutil
import zipfile
import subprocess
import sys
from pathlib import Path
from datetime import datetime

def create_python_directory_structure():
    """Python版配布用のディレクトリ構造を作成"""
    print("📁 Python版配布用ディレクトリ構造を作成中...")
    
    # 配布用ディレクトリ
    dist_dir = Path("python_distribution")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # サブディレクトリ
    (dist_dir / "MinecraftPackGenerator-Python").mkdir()
    (dist_dir / "MinecraftPackGenerator-Python" / "examples").mkdir()
    (dist_dir / "MinecraftPackGenerator-Python" / "templates").mkdir()
    (dist_dir / "MinecraftPackGenerator-Python" / "docs").mkdir()
    
    print("✅ ディレクトリ構造を作成しました")
    return dist_dir

def copy_python_files(dist_dir):
    """Python版用ファイルをコピー"""
    print("📋 Python版ファイルをコピー中...")
    
    # メインファイル
    main_files = [
        "pack_generator.py",
        "packdata.json",
        "requirements.txt",
        "setup.py",
        "package_info.json"
    ]
    
    for file in main_files:
        if Path(file).exists():
            shutil.copy2(file, dist_dir / "MinecraftPackGenerator-Python")
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} が見つかりません")
    
    # Python版用README
    create_python_readme(dist_dir)
    
    print("✅ Python版ファイルをコピーしました")

def create_python_readme(dist_dir):
    """Python版用READMEを作成"""
    print("📖 Python版READMEを作成中...")
    
    readme_content = f"""# Minecraft Pack Generator - Python版

MinecraftのResourcePackとDataPackを自動生成するPythonツールです。

## 🚀 クイックスタート

### 1. ダウンロード
[Releases](https://github.com/FlandollScarlet495/MincraftPackGenerator/releases) からPython版をダウンロード

### 2. インストール
```bash
# 依存関係のインストール
pip install -r requirements.txt

# セットアップ（オプション）
python setup.py install
```

### 3. 使用開始
```bash
python pack_generator.py
```

## 📋 機能

- ✅ カスタムアイテムの生成
- ✅ カスタムスペルの生成
- ✅ カスタムエンティティの生成
- ✅ レシピの生成
- ✅ アドバンスメントの生成
- ✅ ルートテーブルの生成
- ✅ カスタム関数の生成
- ✅ テンプレート機能
- ✅ 設定検証機能
- ✅ プレビュー機能
- ✅ クロスプラットフォーム対応

## 🎮 使用方法

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

## 📁 生成されるファイル

- `datapack.zip` - データパック
- `resourcepack.zip` - リソースパック
- `output/` - 展開されたファイル
- `pack_generator.log` - ログファイル

## 🛠️ 必要な環境

- Python 3.7以上
- 対応OS: Windows, macOS, Linux

## 📦 インストール

### 依存関係のインストール
```bash
pip install -r requirements.txt
```

### セットアップ（オプション）
```bash
python setup.py install
```

## 🔧 設定

`packdata.json` を編集してカスタムアイテムやスペルを追加します：

```json
{{
  "pack_info": {{
    "name": "マイパック",
    "version": "1.0.0",
    "author": "ユーザー名",
    "description": "パックの説明"
  }},
  "items": [
    {{
      "id": "custom_sword",
      "name": "カスタム剣",
      "damage": 10,
      "durability": 1000,
      "enchantments": ["sharpness"],
      "texture": "textures/items/custom_sword.png",
      "lore": "カスタムアイテム",
      "rarity": "common"
    }}
  ],
  "spells": [
    {{
      "id": "fire_spell",
      "name": "火炎スペル",
      "description": "火炎を発射するスペル",
      "commands": [
        "summon minecraft:fireball ~ ~1 ~ {{direction:[0.0,-1.0,0.0]}}"
      ],
      "cooldown": 5,
      "mana_cost": 10,
      "range": 10
    }}
  ]
}}
```

## 📖 ドキュメント

- [インストールガイド](docs/INSTALL_GUIDE.txt)
- [使用方法ガイド](docs/USAGE_GUIDE.txt)
- [配布ガイド](DISTRIBUTION_GUIDE.txt)

## 🎯 サンプル

`examples/` フォルダにサンプルファイルがあります：

- `sample_config.json` - 基本的な設定例
- `textures/` - テクスチャファイル例

## 🔨 開発

### 環境構築
```bash
# リポジトリをクローン
git clone https://github.com/FlandollScarlet495/MincraftPackGenerator.git
cd MincraftPackGenerator

# 依存関係をインストール
pip install -r requirements.txt
```

### テスト
```bash
# 基本的なテスト
python pack_generator.py --preview

# 設定検証
python pack_generator.py --validate
```

## 📊 プロジェクト構造

```
MinecraftPackGenerator-Python/
├── pack_generator.py          # メインプログラム
├── packdata.json             # 設定ファイル
├── requirements.txt          # 依存関係
├── setup.py                 # セットアップスクリプト
├── examples/                # サンプルファイル
├── templates/               # テンプレート
├── docs/                    # ドキュメント
└── [その他のファイル]
```

## 🤝 貢献

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 👤 作者

**けんすけ**

- GitHub: [@FlandollScarlet495](https://github.com/FlandollScarlet495)

## 🙏 謝辞

- Minecraft開発チーム
- Pythonコミュニティ
- すべての貢献者

## 📞 サポート

問題が発生した場合は：

1. [Issues](https://github.com/FlandollScarlet495/MincraftPackGenerator/issues) で報告
2. `pack_generator.log` を確認
3. [ドキュメント](docs/) を参照

## ⭐ スター

このプロジェクトが役に立ったら、⭐ を押してください！

## 🔄 プラットフォーム対応

### Windows
```bash
python pack_generator.py
```

### macOS
```bash
python3 pack_generator.py
```

### Linux
```bash
python3 pack_generator.py
```

---

**Minecraft Pack Generator - Python版** - クロスプラットフォーム対応！

作成日: {datetime.now().strftime('%Y年%m月%d日')}
"""
    
    with open(dist_dir / "MinecraftPackGenerator-Python" / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ Python版READMEを作成しました")

def copy_examples_and_templates(dist_dir):
    """サンプルとテンプレートをコピー"""
    print("📝 サンプルとテンプレートをコピー中...")
    
    # examplesディレクトリをコピー
    if Path("distribution/MinecraftPackGenerator/examples").exists():
        shutil.copytree(
            "distribution/MinecraftPackGenerator/examples",
            dist_dir / "MinecraftPackGenerator-Python" / "examples",
            dirs_exist_ok=True
        )
        print("  ✅ examples/")
    
    # templatesディレクトリをコピー
    if Path("distribution/MinecraftPackGenerator/templates").exists():
        shutil.copytree(
            "distribution/MinecraftPackGenerator/templates",
            dist_dir / "MinecraftPackGenerator-Python" / "templates",
            dirs_exist_ok=True
        )
        print("  ✅ templates/")
    
    # docsディレクトリをコピー
    if Path("distribution/MinecraftPackGenerator/docs").exists():
        shutil.copytree(
            "distribution/MinecraftPackGenerator/docs",
            dist_dir / "MinecraftPackGenerator-Python" / "docs",
            dirs_exist_ok=True
        )
        print("  ✅ docs/")
    
    print("✅ サンプルとテンプレートをコピーしました")

def create_python_install_script(dist_dir):
    """Python版用インストールスクリプトを作成"""
    print("🔧 Python版インストールスクリプトを作成中...")
    
    # Unix系用インストールスクリプト
    install_sh = """#!/bin/bash
echo "🎮 Minecraft Pack Generator - Python版 インストーラー"
echo "=================================================="
echo

echo "🔍 Pythonの確認中..."
if command -v python3 &> /dev/null; then
    echo "✅ Python3が確認されました"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo "✅ Pythonが確認されました"
    PYTHON_CMD="python"
else
    echo "❌ Pythonがインストールされていません"
    echo "Python 3.7以上をインストールしてください:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

echo
echo "📦 依存関係をインストール中..."
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ 依存関係のインストールが完了しました"
else
    echo "❌ 依存関係のインストールに失敗しました"
    exit 1
fi

echo
echo "🧪 パック生成をテスト中..."
$PYTHON_CMD pack_generator.py --preview

if [ $? -eq 0 ]; then
    echo "✅ パック生成のテストが成功しました！"
else
    echo "❌ パック生成のテストに失敗しました"
    echo "pack_generator.log を確認してください"
    exit 1
fi

echo
echo "🎉 インストールが完了しました！"
echo
echo "📚 使用方法:"
echo "  - $PYTHON_CMD pack_generator.py でパック生成"
echo "  - $PYTHON_CMD pack_generator.py --help でヘルプ表示"
echo
echo "📁 生成されるファイル:"
echo "  - datapack.zip (データパック)"
echo "  - resourcepack.zip (リソースパック)"
echo "  - output/ (展開されたファイル)"
echo
echo "📖 詳細な使用方法は docs/ フォルダを参照してください"
echo
"""
    
    with open(dist_dir / "MinecraftPackGenerator-Python" / "install.sh", "w", encoding="utf-8") as f:
        f.write(install_sh)
    
    # Windows用インストールスクリプト
    install_bat = """@echo off
chcp 65001 >nul
echo 🎮 Minecraft Pack Generator - Python版 インストーラー
echo ==================================================
echo.

echo 🔍 Pythonの確認中...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pythonがインストールされていません
    echo Python 3.7以上をインストールしてください:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Pythonが確認されました
echo.

echo 📦 依存関係をインストール中...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ 依存関係のインストールに失敗しました
    pause
    exit /b 1
)
echo ✅ 依存関係のインストールが完了しました
echo.

echo 🧪 パック生成をテスト中...
python pack_generator.py --preview
if %errorlevel% neq 0 (
    echo ❌ パック生成のテストに失敗しました
    echo pack_generator.log を確認してください
    pause
    exit /b 1
)
echo ✅ パック生成のテストが成功しました！
echo.

echo 🎉 インストールが完了しました！
echo.
echo 📚 使用方法:
echo   - python pack_generator.py でパック生成
echo   - python pack_generator.py --help でヘルプ表示
echo.
echo 📁 生成されるファイル:
echo   - datapack.zip (データパック)
echo   - resourcepack.zip (リソースパック)
echo   - output/ (展開されたファイル)
echo.
echo 📖 詳細な使用方法は docs/ フォルダを参照してください
echo.
pause
"""
    
    with open(dist_dir / "MinecraftPackGenerator-Python" / "install.bat", "w", encoding="utf-8") as f:
        f.write(install_bat)
    
    print("✅ Python版インストールスクリプトを作成しました")

def create_python_zip_package(dist_dir):
    """ZIPパッケージを作成"""
    print("📦 Python版ZIPパッケージを作成中...")
    
    zip_name = f"MinecraftPackGenerator-Python_v1.0.0_{datetime.now().strftime('%Y%m%d')}.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = Path(root) / file
                arc_name = file_path.relative_to(dist_dir)
                zipf.write(file_path, arc_name)
    
    print(f"✅ Python版ZIPパッケージを作成しました: {zip_name}")
    return zip_name

def main():
    """メイン処理"""
    print("🐍 Minecraft Pack Generator - Python版配布パッケージ作成ツール")
    print("=" * 70)
    print()
    
    # ディレクトリ構造作成
    dist_dir = create_python_directory_structure()
    
    # ファイルコピー
    copy_python_files(dist_dir)
    copy_examples_and_templates(dist_dir)
    
    # インストールスクリプト作成
    create_python_install_script(dist_dir)
    
    # ZIPパッケージ作成
    zip_name = create_python_zip_package(dist_dir)
    
    print()
    print("🎉 Python版配布パッケージの作成が完了しました！")
    print()
    print("📦 作成されたファイル:")
    print(f"  - {zip_name} (Python版配布用ZIPパッケージ)")
    print(f"  - {dist_dir} (展開されたファイル)")
    print()
    print("📤 配布方法:")
    print("  1. ZIPファイルをGitHub Releasesにアップロード")
    print("  2. ユーザーはZIPを展開")
    print("  3. install.sh (Linux/Mac) または install.bat (Windows) を実行")
    print()
    print("🌍 対応プラットフォーム:")
    print("  - Windows (Python 3.7+)")
    print("  - macOS (Python 3.7+)")
    print("  - Linux (Python 3.7+)")
    print()

if __name__ == "__main__":
    main() 