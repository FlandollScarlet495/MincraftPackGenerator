#!/bin/bash
echo "🎮 Minecraft Pack Generator - Python版 インストーラー"
echo "=================================================="
echo

echo "🔍 Pythonの確認中..."
if command -v python3 &> /dev/null; then
    echo "✅ Python3が確認されました"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo "✅ Pythonが確認されました"
    PYTHON_CMD="python"
else
    echo "❌ Pythonがインストールされていません"
    echo "Python 3.7以上をインストールしてください:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

echo
echo "📦 依存関係をインストール中..."
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ 依存関係のインストールが完了しました"
else
    echo "❌ 依存関係のインストールに失敗しました"
    exit 1
fi

echo
echo "🧪 パック生成をテスト中..."
$PYTHON_CMD pack_generator.py --preview

if [ $? -eq 0 ]; then
    echo "✅ パック生成のテストが成功しました！"
else
    echo "❌ パック生成のテストに失敗しました"
    echo "pack_generator.log を確認してください"
    exit 1
fi

echo
echo "🎉 インストールが完了しました！"
echo
echo "📚 使用方法:"
echo "  - $PYTHON_CMD pack_generator.py でパック生成"
echo "  - $PYTHON_CMD pack_generator.py --help でヘルプ表示"
echo
echo "📁 生成されるファイル:"
echo "  - datapack.zip (データパック)"
echo "  - resourcepack.zip (リソースパック)"
echo "  - output/ (展開されたファイル)"
echo
echo "📖 詳細な使用方法は docs/ フォルダを参照してください"
echo
