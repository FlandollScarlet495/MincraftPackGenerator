#!/bin/bash
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

echo ""
echo "Press Enter to continue..."
read
