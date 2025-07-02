#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minecraft Pack Generator - Python版配布パッケージ作成ツール
Python版の配布パッケージを作成するスクリプト
"""

import os
import shutil
import zipfile
import json
from datetime import datetime
import argparse

def create_python_distribution(with_gui=False):
    """Python版配布パッケージを作成"""
    print("🐍 Minecraft Pack Generator - Python版配布パッケージ作成ツール")
    print("=" * 70)
    
    # バージョン情報
    version = "1.1.0"
    date_str = datetime.now().strftime("%Y%m%d")
    
    # 配布ディレクトリ名
    if with_gui:
        dist_dir = "python_distribution_with_gui"
        zip_name = f"MinecraftPackGenerator-Python_v{version}_{date_str}_with_gui.zip"
    else:
        dist_dir = "python_distribution_nogui"
        zip_name = f"MinecraftPackGenerator-Python_v{version}_{date_str}_nogui.zip"
    
    print(f"📁 Python版配布用ディレクトリ構造を作成中...")
    
    # 既存ディレクトリを削除
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    
    # ディレクトリ構造作成
    os.makedirs(dist_dir, exist_ok=True)
    os.makedirs(os.path.join(dist_dir, "MinecraftPackGenerator-Python"), exist_ok=True)
    
    print("✅ ディレクトリ構造を作成しました")
    
    # Python版ファイルをコピー
    print("📋 Python版ファイルをコピー中...")
    
    python_files = [
        "pack_generator.py",
        "packdata.json", 
        "requirements.txt",
        "setup.py",
        "package_info.json"
    ]
    
    for file in python_files:
        if os.path.exists(file):
            shutil.copy2(file, os.path.join(dist_dir, "MinecraftPackGenerator-Python", file))
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️ {file} (ファイルが見つかりません)")
    
    # GUI版を同梱する場合
    if with_gui and os.path.exists("gui_generator.py"):
        shutil.copy2("gui_generator.py", os.path.join(dist_dir, "MinecraftPackGenerator-Python", "gui_generator.py"))
        print("  ✅ gui_generator.py (GUI版)")
    
    print("✅ Python版ファイルをコピーしました")
    
    # Python版READMEを作成
    print("📖 Python版READMEを作成中...")
    
    readme_content = f"""# Minecraft Pack Generator - Python版 v{version}

## 🐍 Python版 Minecraft Pack Generator

MinecraftのResourcePackとDataPackを自動生成するPythonツールです。

## 📦 インストール方法

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. セットアップ
```bash
python setup.py install
```

## 🚀 使用方法

### コマンドライン版
```bash
python pack_generator.py
```

"""
    
    if with_gui:
        readme_content += """
### GUI版
```bash
python gui_generator.py
```
"""
    
    readme_content += f"""
## 🌍 対応プラットフォーム
- Windows (Python 3.7+)
- macOS (Python 3.7+)
- Linux (Python 3.7+)

## 📋 機能
- カスタムアイテムの生成
- カスタムスペルの生成
- カスタムエンティティの生成
- レシピの生成
- アドバンスメントの生成
- ルートテーブルの生成
- カスタム関数の生成
- テンプレート機能
- 設定検証機能
- プレビュー機能
- ログ機能
- 進捗表示

"""
    
    if with_gui:
        readme_content += """
## 🖥️ GUI機能
- プロジェクト管理
- ビジュアル設定
- リアルタイムプレビュー
- テンプレートエディター
- 統合ログ表示

"""
    
    readme_content += f"""
## 📞 サポート
- ログファイル: pack_generator.log
- ドキュメント: docs/
- サンプル: examples/

## 📄 ライセンス
MIT License

---
作成日: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
バージョン: {version}
"""
    
    with open(os.path.join(dist_dir, "MinecraftPackGenerator-Python", "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ Python版READMEを作成しました")
    
    # サンプルとテンプレートをコピー
    print("📝 サンプルとテンプレートをコピー中...")
    
    sample_dirs = ["examples", "templates", "docs"]
    for dir_name in sample_dirs:
        if os.path.exists(dir_name):
            shutil.copytree(dir_name, os.path.join(dist_dir, "MinecraftPackGenerator-Python", dir_name))
            print(f"  ✅ {dir_name}/")
    
    print("✅ サンプルとテンプレートをコピーしました")
    
    # Python版インストールスクリプトを作成
    print("🔧 Python版インストールスクリプトを作成中...")
    
    # Windows用インストールスクリプト
    install_bat_content = f"""@echo off
echo 🐍 Minecraft Pack Generator - Python版インストーラー
echo ================================================

echo 📦 依存関係をインストール中...
pip install -r requirements.txt

echo 🔧 セットアップを実行中...
python setup.py install

echo ✅ インストールが完了しました！
echo.
echo 🚀 使用方法:
echo   python pack_generator.py
"""
    
    if with_gui:
        install_bat_content += """echo   python gui_generator.py (GUI版)
"""
    
    install_bat_content += """
pause
"""
    
    with open(os.path.join(dist_dir, "MinecraftPackGenerator-Python", "install.bat"), 'w', encoding='utf-8') as f:
        f.write(install_bat_content)
    
    # Linux/Mac用インストールスクリプト
    install_sh_content = f"""#!/bin/bash
echo "🐍 Minecraft Pack Generator - Python版インストーラー"
echo "================================================"

echo "📦 依存関係をインストール中..."
pip3 install -r requirements.txt

echo "🔧 セットアップを実行中..."
python3 setup.py install

echo "✅ インストールが完了しました！"
echo ""
echo "🚀 使用方法:"
echo "  python3 pack_generator.py"
"""
    
    if with_gui:
        install_sh_content += """echo "  python3 gui_generator.py (GUI版)"
"""
    
    install_sh_content += """
echo ""
echo "Press Enter to continue..."
read
"""
    
    with open(os.path.join(dist_dir, "MinecraftPackGenerator-Python", "install.sh"), 'w', encoding='utf-8') as f:
        f.write(install_sh_content)
    
    # 実行権限を付与（Linux/Mac用）
    os.chmod(os.path.join(dist_dir, "MinecraftPackGenerator-Python", "install.sh"), 0o755)
    
    print("✅ Python版インストールスクリプトを作成しました")
    
    # Python版ZIPパッケージを作成
    print("📦 Python版ZIPパッケージを作成中...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, dist_dir)
                zipf.write(file_path, arcname)
    
    print(f"✅ Python版ZIPパッケージを作成しました: {zip_name}")
    
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
    
    return zip_name, dist_dir

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='Python版配布パッケージ作成ツール')
    parser.add_argument('--with-gui', action='store_true', help='GUI版も同梱する')
    args = parser.parse_args()
    
    create_python_distribution(args.with_gui)

if __name__ == "__main__":
    main() 