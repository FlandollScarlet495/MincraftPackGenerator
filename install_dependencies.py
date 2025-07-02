#!/usr/bin/env python3
"""
Minecraft Pack Generator - 依存関係インストーラー
Pythonスクリプト版
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description, required=True):
    """コマンドを実行し、結果を表示する"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        if result.returncode == 0:
            print(f"✅ {description}が完了しました")
            return True
        else:
            print(f"❌ {description}に失敗しました")
            if result.stderr:
                print(f"   エラー: {result.stderr.strip()}")
            if required:
                return False
            else:
                print(f"⚠️ {description}に失敗しましたが、続行します")
                return True
    except Exception as e:
        print(f"❌ {description}でエラーが発生しました: {e}")
        if required:
            return False
        else:
            print(f"⚠️ {description}でエラーが発生しましたが、続行します")
            return True

def check_python_version():
    """Pythonのバージョンを確認する"""
    print("🔍 Pythonのバージョンを確認中...")
    version = sys.version_info
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} がインストールされています")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7以上が必要です")
        return False
    return True

def upgrade_pip():
    """pipをアップグレードする"""
    return run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "pipのアップグレード"
    )

def install_package(package, description, required=True):
    """パッケージをインストールする"""
    return run_command(
        f"{sys.executable} -m pip install {package}",
        f"{description}のインストール",
        required
    )

def check_package(package_name, import_name=None):
    """パッケージがインストールされているか確認する"""
    if import_name is None:
        import_name = package_name
    
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: インストールされていません")
        return False

def main():
    """メイン処理"""
    print("🎮 Minecraft Pack Generator - 依存関係インストーラー")
    print("=" * 50)
    print()
    
    # Pythonのバージョン確認
    if not check_python_version():
        print("\n❌ Pythonのバージョンが要件を満たしていません")
        print("Python 3.7以上をインストールしてください: https://www.python.org/downloads/")
        input("Enterキーを押して終了...")
        return
    
    print()
    
    # pipのアップグレード
    upgrade_pip()
    print()
    
    # 必要なパッケージのインストール
    packages = [
        ("pyinstaller>=5.0.0", "PyInstaller", True),
        ("colorama>=0.4.0", "Colorama", False),
        ("tqdm>=4.64.0", "tqdm", False),
        ("jsonschema>=4.0.0", "jsonschema", False),
        ("Pillow>=9.0.0", "Pillow", False),
    ]
    
    print("📦 ライブラリをインストール中...")
    print()
    
    for package, description, required in packages:
        if not install_package(package, description, required):
            if required:
                print(f"\n❌ 必須パッケージ {description} のインストールに失敗しました")
                input("Enterキーを押して終了...")
                return
        print()
    
    # インストール状況の確認
    print("🔍 インストール状況を確認中...")
    print()
    
    check_results = [
        ("PyInstaller", "pyinstaller"),
        ("Colorama", "colorama"),
        ("tqdm", "tqdm"),
        ("jsonschema", "jsonschema"),
        ("Pillow", "PIL"),
    ]
    
    all_installed = True
    for name, import_name in check_results:
        if not check_package(name, import_name):
            all_installed = False
    
    print()
    
    if all_installed:
        print("🎉 すべての依存関係のインストールが完了しました！")
    else:
        print("⚠️ 一部のオプションライブラリのインストールに失敗しましたが、基本機能は使用できます")
    
    print()
    print("次のステップ:")
    print("  1. python pack_generator.py でパック生成をテスト")
    print("  2. build_exe.bat でexeファイルを作成")
    print()
    print("何か問題がある場合は、pack_generator.log を確認してください。")
    print()
    
    input("Enterキーを押して終了...")

if __name__ == "__main__":
    main() 