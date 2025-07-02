# Minecraft Pack Generator - Python版

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

作成日: 2025年07月02日
