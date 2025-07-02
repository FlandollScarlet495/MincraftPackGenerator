#!/usr/bin/env python3
"""
Minecraft Pack Generator - 配布パッケージ品質チェックツール
"""

import os
import json
import zipfile
import hashlib
from pathlib import Path
from datetime import datetime

def check_file_structure(dist_dir):
    """ファイル構造のチェック"""
    print("📁 ファイル構造をチェック中...")
    
    required_files = [
        "pack_generator.py",
        "packdata.json",
        "requirements.txt",
        "install.bat",
        "install_dependencies.bat",
        "install_dependencies.py",
        "setup.py",
        "quick_start.bat",
        "build_exe.bat",
        "build_exe.py",
        "README.txt"
    ]
    
    required_dirs = [
        "examples",
        "templates",
        "docs"
    ]
    
    missing_files = []
    missing_dirs = []
    
    for file in required_files:
        if not (dist_dir / file).exists():
            missing_files.append(file)
    
    for dir_name in required_dirs:
        if not (dist_dir / dir_name).exists():
            missing_dirs.append(dir_name)
    
    if missing_files:
        print(f"❌ 不足しているファイル: {missing_files}")
        return False
    
    if missing_dirs:
        print(f"❌ 不足しているディレクトリ: {missing_dirs}")
        return False
    
    print("✅ ファイル構造は正常です")
    return True

def check_file_sizes(dist_dir):
    """ファイルサイズのチェック"""
    print("📏 ファイルサイズをチェック中...")
    
    total_size = 0
    file_count = 0
    
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            file_path = Path(root) / file
            size = file_path.stat().st_size
            total_size += size
            file_count += 1
    
    size_mb = total_size / (1024 * 1024)
    
    print(f"📊 統計情報:")
    print(f"  - ファイル数: {file_count}")
    print(f"  - 総サイズ: {size_mb:.2f} MB")
    
    if size_mb > 100:
        print("⚠️ パッケージサイズが大きすぎます（100MB以上）")
        return False
    
    print("✅ ファイルサイズは適切です")
    return True

def check_python_syntax():
    """Pythonファイルの構文チェック"""
    print("🐍 Pythonファイルの構文をチェック中...")
    
    python_files = [
        "pack_generator.py",
        "build_exe.py",
        "install_dependencies.py"
    ]
    
    for file in python_files:
        if Path(file).exists():
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    compile(f.read(), file, 'exec')
                print(f"  ✅ {file}")
            except SyntaxError as e:
                print(f"  ❌ {file}: {e}")
                return False
    
    print("✅ Pythonファイルの構文は正常です")
    return True

def check_json_syntax():
    """JSONファイルの構文チェック"""
    print("📄 JSONファイルの構文をチェック中...")
    
    json_files = [
        "packdata.json",
        "package_info.json"
    ]
    
    for file in json_files:
        if Path(file).exists():
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"  ✅ {file}")
            except json.JSONDecodeError as e:
                print(f"  ❌ {file}: {e}")
                return False
    
    print("✅ JSONファイルの構文は正常です")
    return True

def check_batch_files():
    """バッチファイルのチェック"""
    print("🔧 バッチファイルをチェック中...")
    
    batch_files = [
        "install.bat",
        "install_dependencies.bat",
        "quick_start.bat",
        "build_exe.bat"
    ]
    
    for file in batch_files:
        if Path(file).exists():
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'chcp 65001' in content and 'echo' in content:
                    print(f"  ✅ {file}")
                else:
                    print(f"  ⚠️ {file}: 文字エンコーディング設定が不足")
        else:
            print(f"  ❌ {file}: ファイルが見つかりません")
            return False
    
    print("✅ バッチファイルは正常です")
    return True

def create_file_manifest(dist_dir):
    """ファイルマニフェストを作成"""
    print("📋 ファイルマニフェストを作成中...")
    
    manifest = {
        "created_date": datetime.now().isoformat(),
        "files": []
    }
    
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            file_path = Path(root) / file
            relative_path = file_path.relative_to(dist_dir)
            
            # ファイルハッシュを計算
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            
            manifest["files"].append({
                "path": str(relative_path),
                "size": file_path.stat().st_size,
                "hash": file_hash,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            })
    
    manifest_path = Path("distribution_manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ ファイルマニフェストを作成しました: {manifest_path}")
    return manifest_path

def test_zip_integrity(zip_path):
    """ZIPファイルの整合性テスト"""
    print("📦 ZIPファイルの整合性をテスト中...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            # ファイルリストを取得
            file_list = zipf.namelist()
            
            # 各ファイルの整合性をチェック
            for file in file_list:
                try:
                    zipf.read(file)
                except zipfile.BadZipFile:
                    print(f"  ❌ 破損したファイル: {file}")
                    return False
            
            print(f"  ✅ {len(file_list)} ファイルの整合性を確認")
            return True
            
    except zipfile.BadZipFile:
        print("  ❌ ZIPファイルが破損しています")
        return False

def generate_checksum_file(zip_path):
    """チェックサムファイルを生成"""
    print("🔐 チェックサムファイルを生成中...")
    
    with open(zip_path, 'rb') as f:
        content = f.read()
        md5_hash = hashlib.md5(content).hexdigest()
        sha256_hash = hashlib.sha256(content).hexdigest()
    
    checksum_content = f"""# Minecraft Pack Generator v1.0.0 - チェックサム

ファイル: {Path(zip_path).name}
生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

MD5: {md5_hash}
SHA256: {sha256_hash}

## 使用方法

### Windows (PowerShell)
```powershell
Get-FileHash -Algorithm MD5 "{Path(zip_path).name}"
Get-FileHash -Algorithm SHA256 "{Path(zip_path).name}"
```

### Windows (コマンドプロンプト)
```cmd
certutil -hashfile "{Path(zip_path).name}" MD5
certutil -hashfile "{Path(zip_path).name}" SHA256
```

### Linux/Mac
```bash
md5sum "{Path(zip_path).name}"
sha256sum "{Path(zip_path).name}"
```
"""
    
    checksum_path = Path(f"{Path(zip_path).stem}_checksums.txt")
    with open(checksum_path, 'w', encoding='utf-8') as f:
        f.write(checksum_content)
    
    print(f"✅ チェックサムファイルを作成しました: {checksum_path}")
    return checksum_path

def main():
    """メイン処理"""
    print("🔍 Minecraft Pack Generator - 配布パッケージ品質チェックツール")
    print("=" * 70)
    print()
    
    # 配布ディレクトリの確認
    dist_dir = Path("distribution/MinecraftPackGenerator")
    if not dist_dir.exists():
        print("❌ 配布ディレクトリが見つかりません")
        print("先に create_distribution.py を実行してください")
        return False
    
    # チェック項目
    checks = [
        ("ファイル構造", lambda: check_file_structure(dist_dir)),
        ("ファイルサイズ", lambda: check_file_sizes(dist_dir)),
        ("Python構文", check_python_syntax),
        ("JSON構文", check_json_syntax),
        ("バッチファイル", check_batch_files)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n🔍 {check_name}のチェック:")
        if not check_func():
            all_passed = False
            print(f"❌ {check_name}のチェックに失敗しました")
    
    # ファイルマニフェスト作成
    print(f"\n📋 ファイルマニフェスト作成:")
    manifest_path = create_file_manifest(dist_dir)
    
    # ZIPファイルの確認
    zip_files = list(Path(".").glob("MinecraftPackGenerator_v1.0.0_*.zip"))
    if zip_files:
        latest_zip = max(zip_files, key=lambda x: x.stat().st_mtime)
        print(f"\n📦 ZIPファイルのチェック:")
        if test_zip_integrity(latest_zip):
            checksum_path = generate_checksum_file(latest_zip)
        else:
            all_passed = False
    
    print()
    print("=" * 70)
    if all_passed:
        print("🎉 すべてのチェックが完了しました！")
        print("✅ 配布パッケージは品質基準を満たしています")
        print()
        print("📤 配布準備完了:")
        print(f"  - メインパッケージ: {latest_zip if zip_files else 'N/A'}")
        print(f"  - チェックサム: {checksum_path if 'checksum_path' in locals() else 'N/A'}")
        print(f"  - マニフェスト: {manifest_path}")
        print()
        print("📋 配布時の推奨事項:")
        print("  - ウイルススキャンを実行")
        print("  - 複数の環境で動作確認")
        print("  - ドキュメントの最終確認")
    else:
        print("❌ 一部のチェックに失敗しました")
        print("配布前に問題を修正してください")
    
    print()

if __name__ == "__main__":
    main() 