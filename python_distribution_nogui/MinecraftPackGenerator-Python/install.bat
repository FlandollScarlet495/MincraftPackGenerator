@echo off
echo 🐍 Minecraft Pack Generator - Python版インストーラー
echo ================================================

echo 📦 依存関係をインストール中...
pip install -r requirements.txt

echo 🔧 セットアップを実行中...
python setup.py install

echo ✅ インストールが完了しました！
echo.
echo 🚀 使用方法:
echo   python pack_generator.py

pause
