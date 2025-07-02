#!/usr/bin/env python3
"""
GitHub Releases用のリリースノート作成ツール
"""

import json
import os
from pathlib import Path
from datetime import datetime

def create_release_notes(version="1.0.0"):
    """リリースノートを作成"""
    
    release_notes = f"""# Minecraft Pack Generator v{version}

## 🎉 新機能

### ✨ 主要機能
- **カスタムアイテム生成**: オリジナルのアイテムを簡単に作成
- **カスタムスペル生成**: 魔法システムの実装
- **カスタムエンティティ生成**: 新しいモブの追加
- **レシピ生成**: クラフトレシピの自動生成
- **アドバンスメント生成**: 実績システムの構築
- **ルートテーブル生成**: ドロップアイテムの設定
- **カスタム関数生成**: 複雑な機能の実装

### 🔧 開発ツール
- **テンプレート機能**: 既存の設定をベースに新規作成
- **設定検証機能**: 設定ファイルのエラーチェック
- **プレビュー機能**: 生成前の確認表示
- **exeファイル生成**: スタンドアロンアプリケーション作成
- **配布パッケージ作成**: 簡単配布のための自動化

### 📦 配布機能
- **ワンクリック配布**: `complete_distribution.bat` で簡単配布
- **品質チェック**: 自動品質保証システム
- **チェックサム生成**: ファイル整合性の保証
- **GitHub対応**: 完全なGitHub配布サポート

## 🚀 インストール

### 簡単インストール（推奨）
1. ZIPファイルをダウンロード・展開
2. `install.bat` をダブルクリック
3. 画面の指示に従ってセットアップ

### 手動インストール
```bash
pip install -r requirements.txt
python setup.py install
```

## 📋 使用方法

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

### exeファイル作成
```bash
build_exe.bat
```

## 📁 生成されるファイル

- `datapack.zip` - データパック
- `resourcepack.zip` - リソースパック
- `output/` - 展開されたファイル
- `pack_generator.log` - ログファイル

## 🛠️ 必要な環境

- Windows 10/11
- Python 3.7以上

## 📖 ドキュメント

- [インストールガイド](docs/INSTALL_GUIDE.txt)
- [使用方法ガイド](docs/USAGE_GUIDE.txt)
- [配布ガイド](DISTRIBUTION_GUIDE.txt)

## 🎯 サンプル

`examples/` フォルダにサンプルファイルがあります：

- `sample_config.json` - 基本的な設定例
- `textures/` - テクスチャファイル例

## 🔧 設定例

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

## 🐛 修正された問題

- 初回リリースのため、修正された問題はありません

## 🔄 変更履歴

### v{version} (2025-01-27)
- 🎉 初回リリース
- ✨ 基本的なパック生成機能
- ✨ カスタムアイテム・スペル・エンティティ生成
- ✨ レシピ・アドバンスメント・ルートテーブル生成
- ✨ カスタム関数生成
- ✨ テンプレート機能
- ✨ 設定検証機能
- ✨ プレビュー機能
- ✨ ログ機能
- ✨ 進捗表示
- ✨ exeファイル生成
- ✨ 配布パッケージ作成

## 📞 サポート

問題が発生した場合は：

1. [Issues](https://github.com/yourusername/minecraft-pack-generator/issues) で報告
2. `pack_generator.log` を確認
3. [ドキュメント](docs/) を参照

## 👤 作者

**けんすけ**

- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 謝辞

- Minecraft開発チーム
- Pythonコミュニティ
- すべての貢献者

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

---

**Minecraft Pack Generator v{version}** - Minecraftのパック作成を簡単に！

生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return release_notes

def create_github_workflow():
    """GitHub Actionsワークフローを作成"""
    
    workflow_content = """name: Build and Release

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Create distribution package
      run: |
        python create_distribution.py
    
    - name: Check distribution quality
      run: |
        python distribution_checker.py
    
    - name: Create release
      uses: softprops/action-gh-release@v1
      with:
        files: |
          MinecraftPackGenerator_v*.zip
          *_checksums.txt
          distribution_manifest.json
        body_path: RELEASE_NOTES.md
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""
    
    # .github/workflows/ ディレクトリを作成
    workflow_dir = Path(".github/workflows")
    workflow_dir.mkdir(parents=True, exist_ok=True)
    
    # ワークフローファイルを作成
    with open(workflow_dir / "release.yml", "w", encoding="utf-8") as f:
        f.write(workflow_content)
    
    print("✅ GitHub Actionsワークフローを作成しました: .github/workflows/release.yml")

def create_issue_templates():
    """Issueテンプレートを作成"""
    
    # .github/ISSUE_TEMPLATE/ ディレクトリを作成
    issue_dir = Path(".github/ISSUE_TEMPLATE")
    issue_dir.mkdir(parents=True, exist_ok=True)
    
    # バグレポートテンプレート
    bug_report = """---
name: バグレポート
about: バグを報告して改善に協力してください
title: '[BUG] '
labels: 'bug'
assignees: ''
---

## 🐛 バグの説明
バグの簡潔な説明を記入してください。

## 🔄 再現手順
バグを再現するための手順:
1. '...' に移動
2. '....' をクリック
3. '....' までスクロール
4. エラーを確認

## 📋 期待される動作
何が起こるべきかの簡潔で明確な説明。

## 📸 スクリーンショット
該当する場合、スクリーンショットを追加して問題を説明してください。

## 🖥️ 環境情報
 - OS: [例: Windows 10]
 - Python バージョン: [例: 3.9.0]
 - ツールバージョン: [例: 1.0.0]

## 📄 ログファイル
`pack_generator.log` の内容を添付してください（該当する場合）。

## 💡 追加情報
問題に関するその他の情報やコンテキストをここに追加してください。
"""
    
    # 機能要求テンプレート
    feature_request = """---
name: 機能要求
about: このプロジェクトのアイデアを提案してください
title: '[FEATURE] '
labels: 'enhancement'
assignees: ''
---

## 🎯 問題の説明
この機能要求が解決する問題の説明。例: いつも [問題] に困っています。

## 💡 提案する解決策
望む解決策の簡潔な説明。

## 🔄 代替案
検討した代替の解決策や機能の簡潔な説明。

## 📋 追加情報
機能要求に関するその他の情報やスクリーンショットをここに追加してください。
"""
    
    # テンプレートファイルを作成
    with open(issue_dir / "bug_report.md", "w", encoding="utf-8") as f:
        f.write(bug_report)
    
    with open(issue_dir / "feature_request.md", "w", encoding="utf-8") as f:
        f.write(feature_request)
    
    print("✅ Issueテンプレートを作成しました: .github/ISSUE_TEMPLATE/")

def create_pull_request_template():
    """Pull Requestテンプレートを作成"""
    
    # .github/ ディレクトリを作成
    github_dir = Path(".github")
    github_dir.mkdir(exist_ok=True)
    
    pr_template = """## 📝 変更内容
このPRで変更された内容の簡潔な説明。

## 🔄 変更の種類
以下の該当するものにチェックを入れてください:

- [ ] バグ修正 (既存の機能を修正する変更)
- [ ] 新機能 (新機能を追加する変更)
- [ ] 破壊的変更 (既存の機能を変更または削除する変更)
- [ ] ドキュメント更新 (ドキュメントのみの変更)

## 🧪 テスト
変更をテストするための手順:

1. 
2. 
3. 

## 📸 スクリーンショット
該当する場合、スクリーンショットを追加してください。

## 📋 チェックリスト
以下の項目にチェックを入れてください:

- [ ] コードが既存のスタイルガイドラインに従っている
- [ ] 自己レビューを実行した
- [ ] コードにコメントを追加した（特に理解しにくい部分）
- [ ] 対応するドキュメントを更新した
- [ ] 変更が既存のテストに影響しないことを確認した
- [ ] 新しいテストを追加した（該当する場合）

## 📄 追加情報
その他の情報やコンテキストをここに追加してください。
"""
    
    with open(github_dir / "pull_request_template.md", "w", encoding="utf-8") as f:
        f.write(pr_template)
    
    print("✅ Pull Requestテンプレートを作成しました: .github/pull_request_template.md")

def main():
    """メイン処理"""
    print("🚀 GitHub Releases用ファイル作成ツール")
    print("=" * 50)
    print()
    
    # バージョンを取得
    version = "1.0.0"
    if Path("package_info.json").exists():
        with open("package_info.json", "r", encoding="utf-8") as f:
            package_info = json.load(f)
            version = package_info.get("package_info", {}).get("version", "1.0.0")
    
    # リリースノートを作成
    print("📝 リリースノートを作成中...")
    release_notes = create_release_notes(version)
    
    with open("RELEASE_NOTES.md", "w", encoding="utf-8") as f:
        f.write(release_notes)
    
    print("✅ リリースノートを作成しました: RELEASE_NOTES.md")
    
    # GitHub Actionsワークフローを作成
    print("\n🔧 GitHub Actionsワークフローを作成中...")
    create_github_workflow()
    
    # Issueテンプレートを作成
    print("\n📋 Issueテンプレートを作成中...")
    create_issue_templates()
    
    # Pull Requestテンプレートを作成
    print("\n🔀 Pull Requestテンプレートを作成中...")
    create_pull_request_template()
    
    print()
    print("🎉 GitHub配布用ファイルの作成が完了しました！")
    print()
    print("📁 作成されたファイル:")
    print("  - RELEASE_NOTES.md (リリースノート)")
    print("  - .github/workflows/release.yml (GitHub Actions)")
    print("  - .github/ISSUE_TEMPLATE/ (Issueテンプレート)")
    print("  - .github/pull_request_template.md (PRテンプレート)")
    print()
    print("📤 GitHub配布手順:")
    print("  1. リポジトリを作成")
    print("  2. ファイルをプッシュ")
    print("  3. タグを作成 (v1.0.0)")
    print("  4. GitHub Actionsが自動実行")
    print("  5. Releasesページで確認")
    print()

if __name__ == "__main__":
    main() 