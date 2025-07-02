#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minecraft Pack Generator - チェックサム作成ツール
配布パッケージのチェックサムを生成するスクリプト
"""

import os
import hashlib
from datetime import datetime
import glob

def calculate_checksums(file_path):
    """ファイルのMD5とSHA256チェックサムを計算"""
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
            sha256_hash.update(chunk)
    
    return md5_hash.hexdigest(), sha256_hash.hexdigest()

def create_checksums_file():
    """チェックサムファイルを作成"""
    print("🔍 Minecraft Pack Generator - チェックサム作成ツール")
    print("=" * 60)
    
    # 現在の日時
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y%m%d")
    
    # ZIPファイルを検索
    zip_files = []
    zip_patterns = [
        "MinecraftPackGenerator_v*_nogui.zip",
        "MinecraftPackGenerator_v*_with_gui.zip",
        "MinecraftPackGenerator_v*.zip",  # 追加: v1.0.0_20250702.zip など
        "MinecraftPackGenerator-Python_v*_nogui.zip",
        "MinecraftPackGenerator-Python_v*_with_gui.zip"
    ]
    
    for pattern in zip_patterns:
        zip_files.extend(glob.glob(pattern))
    
    if not zip_files:
        print("❌ ZIPファイルが見つかりません")
        return
    
    # チェックサムファイル名
    checksums_file = f"MinecraftPackGenerator_v1.1.0_{date_str}_checksums.txt"
    
    print(f"📦 チェックサムを計算中... ({len(zip_files)}個のファイル)")
    
    # チェックサムファイルの内容を作成
    content = f"""# Minecraft Pack Generator v1.1.0 - チェックサム

生成日時: {current_time}
バージョン: 1.1.0

## 📦 配布パッケージ

"""
    
    total_size = 0
    
    for zip_file in sorted(zip_files):
        if os.path.exists(zip_file):
            # ファイルサイズを取得
            file_size = os.path.getsize(zip_file)
            total_size += file_size
            
            # チェックサムを計算
            md5_hash, sha256_hash = calculate_checksums(zip_file)
            
            # ファイルサイズを人間が読みやすい形式に変換
            if file_size < 1024:
                size_str = f"{file_size} B"
            elif file_size < 1024 * 1024:
                size_str = f"{file_size / 1024:.1f} KB"
            else:
                size_str = f"{file_size / (1024 * 1024):.1f} MB"
            
            content += f"""### {zip_file}
サイズ: {size_str}
MD5: {md5_hash}
SHA256: {sha256_hash}

"""
            print(f"  ✅ {zip_file} ({size_str})")
    
    # 合計サイズ
    if total_size < 1024 * 1024:
        total_size_str = f"{total_size / 1024:.1f} KB"
    else:
        total_size_str = f"{total_size / (1024 * 1024):.1f} MB"
    
    content += f"""
## 📊 統計情報

- ファイル数: {len(zip_files)}個
- 合計サイズ: {total_size_str}
- 生成日時: {current_time}

## 🔍 使用方法

### Windows (PowerShell)
```powershell
# MD5チェックサムを確認
Get-FileHash -Algorithm MD5 "ファイル名.zip"

# SHA256チェックサムを確認  
Get-FileHash -Algorithm SHA256 "ファイル名.zip"
```

### Windows (コマンドプロンプト)
```cmd
# MD5チェックサムを確認
certutil -hashfile "ファイル名.zip" MD5

# SHA256チェックサムを確認
certutil -hashfile "ファイル名.zip" SHA256
```

### Linux/Mac
```bash
# MD5チェックサムを確認
md5sum "ファイル名.zip"

# SHA256チェックサムを確認
sha256sum "ファイル名.zip"
```

## ✅ 検証方法

1. ダウンロードしたZIPファイルのチェックサムを計算
2. 上記の値と比較
3. 一致すればファイルが正常にダウンロードされています

## 🛡️ セキュリティ

- チェックサムはファイルの整合性を確認するために使用されます
- ダウンロード中にファイルが破損していないかチェックできます
- 改ざんされていないことを確認できます

---
作成日: {current_time}
バージョン: 1.1.0
"""
    
    # チェックサムファイルを保存
    with open(checksums_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ チェックサムファイルを作成しました: {checksums_file}")
    print()
    print("📋 作成されたファイル:")
    print(f"  - {checksums_file}")
    print()
    print("📊 統計情報:")
    print(f"  - ファイル数: {len(zip_files)}個")
    print(f"  - 合計サイズ: {total_size_str}")
    print()
    print("🔍 使用方法:")
    print("  1. ダウンロードしたZIPファイルのチェックサムを計算")
    print("  2. 上記の値と比較")
    print("  3. 一致すればファイルが正常です")

def main():
    """メイン関数"""
    create_checksums_file()

if __name__ == "__main__":
    main() 