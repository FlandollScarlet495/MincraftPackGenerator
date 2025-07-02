import json
import os
import shutil
import zipfile
import logging
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pack_generator.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PackGenerator:
    def __init__(self, config_path: str = 'packdata.json'):
        self.config_path = config_path
        self.data = None
        self.output_dir = Path('output')
        self.datapack_dir = self.output_dir / 'datapack'
        self.resourcepack_dir = self.output_dir / 'resourcepack'
        
    def create_template(self, template_name: str = 'template') -> bool:
        """設定ファイルのテンプレートを作成する"""
        template_data = {
            "pack_info": {
                "name": "カスタムパック",
                "version": "1.0.0",
                "author": "作者名",
                "description": "カスタムMinecraftパックの説明"
            },
            "items": [
                {
                    "id": "custom_item",
                    "name": "カスタムアイテム",
                    "damage": 10,
                    "durability": 1000,
                    "enchantments": ["sharpness"],
                    "texture": "textures/items/custom_item.png",
                    "lore": "カスタムアイテムの説明",
                    "rarity": "common"
                }
            ],
            "spells": [
                {
                    "id": "custom_spell",
                    "name": "カスタムスペル",
                    "description": "カスタムスペルの説明",
                    "commands": [
                        "say カスタムスペル発動！",
                        "particle minecraft:flame ~ ~1 ~ 0.5 0.5 0.5 0 10 force"
                    ],
                    "cooldown": 10,
                    "mana_cost": 20,
                    "range": 5
                }
            ]
        }
        
        template_path = f"{template_name}.json"
        try:
            with open(template_path, 'w', encoding='utf-8') as f:
                json.dump(template_data, f, indent=2, ensure_ascii=False)
            logger.info(f"テンプレートファイルを作成しました: {template_path}")
            return True
        except Exception as e:
            logger.error(f"テンプレート作成エラー: {e}")
            return False

    def validate_config(self) -> List[str]:
        """設定ファイルの検証"""
        errors = []
        
        if self.data is None:
            errors.append("データが読み込まれていません")
            return errors
        
        # パック情報の検証
        pack_info = self.data.get('pack_info', {})
        if not pack_info.get('name'):
            errors.append("パック名が設定されていません")
        if not pack_info.get('version'):
            errors.append("バージョンが設定されていません")
        
        # アイテムの検証
        items = self.data.get('items', [])
        for i, item in enumerate(items):
            if not item.get('id'):
                errors.append(f"アイテム {i+1}: IDが設定されていません")
            if not item.get('name'):
                errors.append(f"アイテム {i+1}: 名前が設定されていません")
        
        # スペルの検証
        spells = self.data.get('spells', [])
        for i, spell in enumerate(spells):
            if not spell.get('id'):
                errors.append(f"スペル {i+1}: IDが設定されていません")
            if not spell.get('name'):
                errors.append(f"スペル {i+1}: 名前が設定されていません")
            if not spell.get('commands'):
                errors.append(f"スペル {i+1}: コマンドが設定されていません")
        
        return errors

    def preview_pack(self) -> bool:
        """パックのプレビューを表示"""
        if self.data is None:
            logger.error("データが読み込まれていません")
            return False
        
        logger.info("=== パックプレビュー ===")
        
        # パック情報
        pack_info = self.data.get('pack_info', {})
        logger.info(f"📦 パック名: {pack_info.get('name', 'Unknown')}")
        logger.info(f"📋 バージョン: {pack_info.get('version', 'Unknown')}")
        logger.info(f"👤 作者: {pack_info.get('author', 'Unknown')}")
        logger.info(f"📝 説明: {pack_info.get('description', '説明なし')}")
        
        # アイテム一覧
        items = self.data.get('items', [])
        logger.info(f"\n🗡️ アイテム ({len(items)}個):")
        for item in items:
            logger.info(f"  - {item.get('name', 'Unknown')} (ID: {item.get('id', 'Unknown')})")
        
        # スペル一覧
        spells = self.data.get('spells', [])
        logger.info(f"\n✨ スペル ({len(spells)}個):")
        for spell in spells:
            cooldown = spell.get('cooldown', 'なし')
            mana_cost = spell.get('mana_cost', 'なし')
            logger.info(f"  - {spell.get('name', 'Unknown')} (クールダウン: {cooldown}秒, マナ: {mana_cost})")
        
        return True

    def load_pack_data(self) -> bool:
        """パックデータを読み込む"""
        try:
            # exeファイル内に埋め込まれたリソースファイルを読み込む
            if getattr(sys, 'frozen', False):
                # exeファイルとして実行されている場合
                application_path = getattr(sys, '_MEIPASS', '')
                config_path = os.path.join(application_path, self.config_path)
            else:
                # 通常のPythonスクリプトとして実行されている場合
                config_path = self.config_path
            
            with open(config_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            logger.info(f"パックデータを読み込みました: {config_path}")
            
            # パック情報を表示
            pack_info = self.data.get('pack_info', {})
            logger.info(f"パック名: {pack_info.get('name', 'Unknown')}")
            logger.info(f"バージョン: {pack_info.get('version', 'Unknown')}")
            logger.info(f"作者: {pack_info.get('author', 'Unknown')}")
            
            return True
        except FileNotFoundError:
            logger.error(f"設定ファイルが見つかりません: {self.config_path}")
            return False
        except json.JSONDecodeError as e:
            logger.error(f"JSONの解析エラー: {e}")
            return False
        except Exception as e:
            logger.error(f"予期しないエラー: {e}")
            return False

    def validate_spell_commands(self, spell: Dict[str, Any]) -> List[str]:
        """スペルのコマンドを検証する"""
        errors = []
        commands = spell.get('commands', [])
        
        if not commands:
            errors.append(f"スペル '{spell.get('name', 'Unknown')}' にコマンドが設定されていません")
            return errors
            
        for i, cmd in enumerate(commands):
            if not isinstance(cmd, str):
                errors.append(f"コマンド {i+1} が文字列ではありません: {cmd}")
            elif not cmd.strip():
                errors.append(f"コマンド {i+1} が空です")
            elif cmd.startswith('/'):
                errors.append(f"コマンド {i+1} に不要な '/' が含まれています: {cmd}")
                
        return errors

    def generate_mcfunctions(self, spells: List[Dict[str, Any]], out_dir: Path) -> bool:
        """mcfunctionファイルを生成する"""
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            total_spells = len(spells)
            
            for i, spell in enumerate(spells, 1):
                logger.info(f"スペル生成中... ({i}/{total_spells}): {spell.get('name', 'Unknown')}")
                
                # コマンド検証
                errors = self.validate_spell_commands(spell)
                if errors:
                    for error in errors:
                        logger.warning(error)
                
                filepath = out_dir / f"{spell['id']}.mcfunction"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# {spell['name']} 発動コマンド\n")
                    f.write(f"# 説明: {spell.get('description', '説明なし')}\n")
                    f.write(f"# クールダウン: {spell.get('cooldown', 'なし')}秒\n")
                    f.write(f"# マナ消費: {spell.get('mana_cost', 'なし')}\n")
                    f.write(f"# 射程: {spell.get('range', 'なし')}ブロック\n\n")
                    
                    # マナチェック
                    if spell.get('mana_cost'):
                        f.write(f"# マナチェック\n")
                        f.write(f"execute unless score @s mana matches {spell['mana_cost']}.. run tellraw @s {{\"text\":\"マナが足りません！\",\"color\":\"red\"}}\n")
                        f.write(f"execute unless score @s mana matches {spell['mana_cost']}.. run return 0\n")
                        f.write(f"scoreboard players remove @s mana {spell['mana_cost']}\n\n")
                    
                    # クールダウン処理を追加
                    if spell.get('cooldown'):
                        f.write(f"# クールダウン確認\n")
                        f.write(f"execute unless score @s cooldown_{spell['id']} matches 0.. run tellraw @s {{\"text\":\"クールダウン中です\",\"color\":\"red\"}}\n")
                        f.write(f"execute unless score @s cooldown_{spell['id']} matches 0.. run return 0\n\n")
                    
                    # メインコマンド
                    f.write("# メインコマンド\n")
                    for cmd in spell['commands']:
                        f.write(cmd + "\n")
                    
                    # クールダウン設定
                    if spell.get('cooldown'):
                        f.write(f"\n# クールダウン設定\n")
                        f.write(f"scoreboard players set @s cooldown_{spell['id']} {spell['cooldown'] * 20}\n")
                        f.write(f"schedule function {spell['id']}_cooldown {spell['cooldown']}s\n")
                
                # クールダウン用の関数も生成
                if spell.get('cooldown'):
                    cooldown_filepath = out_dir / f"{spell['id']}_cooldown.mcfunction"
                    with open(cooldown_filepath, 'w', encoding='utf-8') as f:
                        f.write(f"# {spell['name']} クールダウン処理\n")
                        f.write(f"scoreboard players remove @s cooldown_{spell['id']} 1\n")
                        f.write(f"execute if score @s cooldown_{spell['id']} matches 1.. run schedule function {spell['id']}_cooldown 1t\n")
            
            logger.info(f"mcfunctionファイルを {out_dir} に生成しました")
            return True
            
        except Exception as e:
            logger.error(f"mcfunction生成エラー: {e}")
            return False

    def copy_textures(self, items: List[Dict[str, Any]], resourcepack_dir: Path) -> bool:
        """テクスチャをコピーする"""
        try:
            textures_dir = resourcepack_dir / 'assets' / 'minecraft' / 'textures' / 'items'
            textures_dir.mkdir(parents=True, exist_ok=True)
            
            total_items = len(items)
            copied_count = 0
            
            for i, item in enumerate(items, 1):
                logger.info(f"テクスチャコピー中... ({i}/{total_items}): {item.get('name', 'Unknown')}")
                
                src_path = Path(item['texture'])
                dst_path = textures_dir / src_path.name
                
                try:
                    if src_path.exists():
                        shutil.copy2(src_path, dst_path)
                        copied_count += 1
                        logger.info(f"テクスチャをコピーしました: {src_path} -> {dst_path}")
                    else:
                        logger.warning(f"テクスチャファイルが見つかりません: {src_path}")
                except Exception as e:
                    logger.error(f"テクスチャコピーエラー {src_path}: {e}")
            
            logger.info(f"テクスチャコピー完了: {copied_count}/{total_items}")
            return True
            
        except Exception as e:
            logger.error(f"テクスチャコピー処理エラー: {e}")
            return False

    def create_datapack_structure(self) -> bool:
        """データパックの完全な構造を作成する"""
        try:
            if self.data is None:
                logger.error("データが読み込まれていません")
                return False
                
            # データパックの基本構造
            datapack_structure = [
                'pack.mcmeta',
                'data/minecraft/tags/functions/load.json',
                'data/minecraft/tags/functions/tick.json'
            ]
            
            for path in datapack_structure:
                full_path = self.datapack_dir / path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                if path.endswith('pack.mcmeta'):
                    pack_info = self.data.get('pack_info', {})
                    content = {
                        "pack": {
                            "pack_format": 15,
                            "description": pack_info.get('description', 'カスタムデータパック')
                        }
                    }
                    with open(full_path, 'w', encoding='utf-8') as f:
                        json.dump(content, f, indent=4, ensure_ascii=False)
                        
                elif path.endswith('load.json'):
                    content = {
                        "values": [
                            "minecraft:load"
                        ]
                    }
                    with open(full_path, 'w', encoding='utf-8') as f:
                        json.dump(content, f, indent=4)
                        
                elif path.endswith('tick.json'):
                    content = {
                        "values": [
                            "minecraft:tick"
                        ]
                    }
                    with open(full_path, 'w', encoding='utf-8') as f:
                        json.dump(content, f, indent=4)
            
            # スコアボード初期化関数
            init_file = self.datapack_dir / 'data' / 'minecraft' / 'functions' / 'load.mcfunction'
            init_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write("# スコアボード初期化\n")
                f.write("scoreboard objectives add mana dummy \"マナ\"\n")
                f.write("scoreboard objectives add level dummy \"レベル\"\n")
                f.write("scoreboard objectives add experience dummy \"経験値\"\n")
                
                spells = self.data.get('spells', [])
                for spell in spells:
                    if spell.get('cooldown'):
                        f.write(f"scoreboard objectives add cooldown_{spell['id']} dummy \"{spell['name']} クールダウン\"\n")
                
                f.write("\n# プレイヤー初期化\n")
                f.write("execute as @a unless score @s mana matches 1.. run scoreboard players set @s mana 100\n")
                f.write("execute as @a unless score @s level matches 1.. run scoreboard players set @s level 1\n")
                f.write("execute as @a unless score @s experience matches 1.. run scoreboard players set @s experience 0\n")
                
                f.write("\n# ロード完了メッセージ\n")
                pack_info = self.data.get('pack_info', {})
                pack_name = pack_info.get('name', 'カスタムパック')
                f.write(f"tellraw @a {{\"text\":\"{pack_name}が読み込まれました！\",\"color\":\"green\"}}\n")
            
            # ティック関数
            tick_file = self.datapack_dir / 'data' / 'minecraft' / 'functions' / 'tick.mcfunction'
            with open(tick_file, 'w', encoding='utf-8') as f:
                f.write("# ティック処理\n")
                f.write("# マナ回復\n")
                f.write("execute as @a run scoreboard players add @s mana 1\n")
                f.write("execute as @a[score={mana=100..}] run scoreboard players set @s mana 100\n")
                f.write("\n# 経験値からレベルアップ\n")
                f.write("execute as @a if score @s experience matches 100.. run scoreboard players remove @s experience 100\n")
                f.write("execute as @a if score @s experience matches 0 run scoreboard players add @s level 1\n")
                f.write("execute as @a if score @s experience matches 0 run tellraw @s {\"text\":\"レベルアップ！\",\"color\":\"yellow\"}\n")
            
            logger.info("データパック構造を作成しました")
            return True
            
        except Exception as e:
            logger.error(f"データパック構造作成エラー: {e}")
            return False

    def create_resourcepack_structure(self) -> bool:
        """リソースパックの完全な構造を作成する"""
        try:
            if self.data is None:
                logger.error("データが読み込まれていません")
                return False
                
            # pack.mcmeta
            pack_mcmeta = self.resourcepack_dir / 'pack.mcmeta'
            pack_mcmeta.parent.mkdir(parents=True, exist_ok=True)
            
            pack_info = self.data.get('pack_info', {})
            content = {
                "pack": {
                    "pack_format": 15,
                    "description": pack_info.get('description', 'カスタムリソースパック')
                }
            }
            with open(pack_mcmeta, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=4, ensure_ascii=False)
            
            # アイテムモデルファイル
            models_dir = self.resourcepack_dir / 'assets' / 'minecraft' / 'models' / 'item'
            models_dir.mkdir(parents=True, exist_ok=True)
            
            items = self.data.get('items', [])
            for item in items:
                model_file = models_dir / f"{item['id']}.json"
                model_content = {
                    "parent": "item/generated",
                    "textures": {
                        "layer0": f"item/{Path(item['texture']).stem}"
                    }
                }
                with open(model_file, 'w', encoding='utf-8') as f:
                    json.dump(model_content, f, indent=4)
            
            logger.info("リソースパック構造を作成しました")
            return True
            
        except Exception as e:
            logger.error(f"リソースパック構造作成エラー: {e}")
            return False

    def zip_folder(self, folder_path: Path, output_zip: str) -> bool:
        """フォルダをZIP圧縮する"""
        try:
            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        full_path = Path(root) / file
                        rel_path = full_path.relative_to(folder_path)
                        zipf.write(full_path, rel_path)
            
            logger.info(f"ZIPファイルを作成しました: {output_zip}")
            return True
            
        except Exception as e:
            logger.error(f"ZIP作成エラー: {e}")
            return False

    def generate(self) -> bool:
        """メイン生成処理"""
        logger.info("=== カスタムパック生成開始 ===")
        
        # データ読み込み
        if not self.load_pack_data():
            return False
        
        # 設定検証
        errors = self.validate_config()
        if errors:
            logger.error("設定エラーが見つかりました:")
            for error in errors:
                logger.error(f"  - {error}")
            return False
        
        # プレビュー表示
        self.preview_pack()
        
        # 出力ディレクトリ作成
        self.output_dir.mkdir(exist_ok=True)
        
        # データパック生成
        logger.info("データパック生成中...")
        if not self.create_datapack_structure():
            return False
        
        if self.data is None:
            logger.error("データが読み込まれていません")
            return False
            
        # スペル関数生成
        functions_dir = self.datapack_dir / 'data' / 'minecraft' / 'functions'
        if not self.generate_mcfunctions(self.data.get('spells', []), functions_dir):
            return False
        
        # リソースパック生成
        logger.info("リソースパック生成中...")
        if not self.create_resourcepack_structure():
            return False
        
        if not self.copy_textures(self.data.get('items', []), self.resourcepack_dir):
            logger.warning("テクスチャコピーでエラーが発生しましたが、処理を続行します")
        
        # ZIP圧縮
        logger.info("ZIP圧縮中...")
        self.zip_folder(self.datapack_dir, 'datapack.zip')
        self.zip_folder(self.resourcepack_dir, 'resourcepack.zip')
        
        # 統計情報の表示
        self.show_statistics()
        
        logger.info("=== パック生成完了！ ===")
        logger.info(f"出力ディレクトリ: {self.output_dir}")
        logger.info("生成されたファイル:")
        logger.info("  - datapack.zip (データパック)")
        logger.info("  - resourcepack.zip (リソースパック)")
        logger.info("  - pack_generator.log (ログファイル)")
        
        return True

    def show_statistics(self):
        """生成統計を表示する"""
        if self.data is None:
            return
            
        logger.info("=== 生成統計 ===")
        logger.info(f"アイテム数: {len(self.data.get('items', []))}")
        logger.info(f"スペル数: {len(self.data.get('spells', []))}")

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='Minecraft ResourcePack & DataPack 自動生成ツール')
    parser.add_argument('--config', '-c', default='packdata.json', help='設定ファイルのパス')
    parser.add_argument('--template', '-t', help='テンプレートファイルを作成')
    parser.add_argument('--preview', '-p', action='store_true', help='パックのプレビューを表示')
    parser.add_argument('--validate', '-v', action='store_true', help='設定ファイルを検証')
    
    args = parser.parse_args()
    
    generator = PackGenerator(args.config)
    
    # テンプレート作成
    if args.template:
        generator.create_template(args.template)
        return
    
    # 設定検証
    if args.validate:
        if generator.load_pack_data():
            errors = generator.validate_config()
            if errors:
                print("❌ 設定エラーが見つかりました:")
                for error in errors:
                    print(f"  - {error}")
            else:
                print("✅ 設定ファイルは正常です")
        return
    
    # プレビュー表示
    if args.preview:
        if generator.load_pack_data():
            generator.preview_pack()
        return
    
    # 通常の生成処理
    success = generator.generate()
    
    if success:
        print("\n🎉 パック生成が成功しました！")
        print("📁 生成されたファイルを確認してください")
        print("🎮 Minecraftでパックを有効化して楽しんでください！")
    else:
        print("\n❌ パック生成でエラーが発生しました")
        print("📋 ログファイルを確認してください: pack_generator.log")

if __name__ == "__main__":
    main()
