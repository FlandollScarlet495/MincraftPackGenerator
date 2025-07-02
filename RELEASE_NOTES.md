# Minecraft Pack Generator v1.0.0

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

## 🐛 修正された問題

- 初回リリースのため、修正された問題はありません

## 🔄 変更履歴

### v1.0.0 (2025-01-27)
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

**Minecraft Pack Generator v1.0.0** - Minecraftのパック作成を簡単に！

生成日時: 2025-07-02 12:07:21
