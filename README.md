# Minecraft Pack Generator

MinecraftのResourcePackとDataPackを自動生成するツールです。

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 クイックスタート

### 1. ダウンロード
[Releases](https://github.com/yourusername/minecraft-pack-generator/releases) から最新版をダウンロード

### 2. インストール
```bash
# ZIPファイルを展開
# install.bat をダブルクリック
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
- ✅ exeファイル生成
- ✅ 配布パッケージ作成

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

## 📦 インストール

### 自動インストール（推奨）
1. `install.bat` をダブルクリック
2. 画面の指示に従ってセットアップ

### 手動インストール
```bash
# 依存関係のインストール
pip install -r requirements.txt

# セットアップ
python setup.py install
```

## 🔧 設定

`packdata.json` を編集してカスタムアイテムやスペルを追加します：

```json
{
  "pack_info": {
    "name": "マイパック",
    "version": "1.0.0",
    "author": "ユーザー名",
    "description": "パックの説明"
  },
  "items": [
    {
      "id": "custom_sword",
      "name": "カスタム剣",
      "damage": 10,
      "durability": 1000,
      "enchantments": ["sharpness"],
      "texture": "textures/items/custom_sword.png",
      "lore": "カスタムアイテム",
      "rarity": "common"
    }
  ],
  "spells": [
    {
      "id": "fire_spell",
      "name": "火炎スペル",
      "description": "火炎を発射するスペル",
      "commands": [
        "summon minecraft:fireball ~ ~1 ~ {direction:[0.0,-1.0,0.0]}"
      ],
      "cooldown": 5,
      "mana_cost": 10,
      "range": 10
    }
  ]
}
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
git clone https://github.com/yourusername/minecraft-pack-generator.git
cd minecraft-pack-generator

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

### 配布パッケージ作成
```bash
# 完全配布パッケージ作成
complete_distribution.bat
```

## 📊 プロジェクト構造

```
minecraft-pack-generator/
├── pack_generator.py          # メインプログラム
├── packdata.json             # 設定ファイル
├── requirements.txt          # 依存関係
├── setup.py                 # セットアップスクリプト
├── build_exe.py             # exeビルドスクリプト
├── create_distribution.py   # 配布パッケージ作成
├── distribution_checker.py  # 品質チェック
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

- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 謝辞

- Minecraft開発チーム
- Pythonコミュニティ
- すべての貢献者

## 📞 サポート

問題が発生した場合は：

1. [Issues](https://github.com/yourusername/minecraft-pack-generator/issues) で報告
2. `pack_generator.log` を確認
3. [ドキュメント](docs/) を参照

## ⭐ スター

このプロジェクトが役に立ったら、⭐ を押してください！

---

**Minecraft Pack Generator** - Minecraftのパック作成を簡単に！ 