# GitHub配布ガイド

## 🚀 クイックスタート

### 1. 自動セットアップ（推奨）
```bash
setup_github.bat
```

これだけで以下が自動実行されます：
- GitHub配布用ファイルの作成
- 配布パッケージの作成
- 品質チェックの実行
- 最終確認

### 2. 手動セットアップ
```bash
# GitHub配布用ファイルの作成
python github_release_creator.py

# 配布パッケージの作成
python create_distribution.py

# 品質チェックの実行
python distribution_checker.py
```

## 📁 作成されるGitHub用ファイル

### メインファイル
- `README.md` - GitHub用README
- `LICENSE` - MITライセンス
- `.gitignore` - Git除外設定

### GitHub設定
- `.github/workflows/release.yml` - GitHub Actions
- `.github/ISSUE_TEMPLATE/` - Issueテンプレート
- `.github/pull_request_template.md` - PRテンプレート

### 配布ファイル
- `RELEASE_NOTES.md` - リリースノート
- `MinecraftPackGenerator_v1.0.0_YYYYMMDD.zip` - 配布パッケージ
- `*_checksums.txt` - チェックサムファイル

## 🔧 GitHub配布手順

### 1. GitHubリポジトリの作成

1. [GitHub.com](https://github.com) にアクセス
2. 右上の「+」ボタン → 「New repository」をクリック
3. リポジトリ設定：
   - **Repository name**: `minecraft-pack-generator`
   - **Description**: `MinecraftのResourcePackとDataPackを自動生成するツール`
   - **Visibility**: Public（推奨）
   - **Add a README file**: チェックしない（既に作成済み）
   - **Add .gitignore**: チェックしない（既に作成済み）
   - **Choose a license**: MIT License（既に作成済み）
4. 「Create repository」をクリック

### 2. ローカルリポジトリの初期化

```bash
# Gitリポジトリを初期化
git init

# ファイルをステージング
git add .

# 初回コミット
git commit -m "Initial commit: Minecraft Pack Generator v1.0.0"

# メインブランチに名前を変更
git branch -M main

# リモートリポジトリを追加（yourusernameを実際のユーザー名に変更）
git remote add origin https://github.com/yourusername/minecraft-pack-generator.git

# ファイルをプッシュ
git push -u origin main
```

### 3. タグの作成とリリース

```bash
# タグを作成
git tag v1.0.0

# タグをプッシュ
git push origin v1.0.0
```

### 4. GitHub Actionsの確認

1. GitHubリポジトリページで「Actions」タブをクリック
2. ワークフローの実行状況を確認
3. ビルドが成功したら「Releases」タブでリリースを確認

## 📋 GitHub設定の詳細

### リポジトリ設定

#### 基本情報
- **Name**: minecraft-pack-generator
- **Description**: MinecraftのResourcePackとDataPackを自動生成するツール
- **Website**: （空欄）
- **Topics**: minecraft, datapack, resourcepack, generator, python, automation

#### 機能設定
- ✅ Issues
- ✅ Pull requests
- ✅ Discussions
- ✅ Actions
- ✅ Projects
- ✅ Wiki
- ✅ Security

### GitHub Actionsワークフロー

`.github/workflows/release.yml` が自動的に以下を実行：

1. **環境セットアップ**
   - Windows環境の準備
   - Python 3.9のインストール

2. **依存関係のインストール**
   - requirements.txtからライブラリをインストール

3. **配布パッケージの作成**
   - create_distribution.pyを実行
   - 品質チェックを実行

4. **リリースの作成**
   - 自動的にGitHub Releasesを作成
   - ファイルをアップロード
   - リリースノートを設定

### Issueテンプレート

#### バグレポート
- バグの詳細説明
- 再現手順
- 環境情報
- ログファイル

#### 機能要求
- 問題の説明
- 提案する解決策
- 代替案
- 追加情報

### Pull Requestテンプレート

- 変更内容の説明
- 変更の種類
- テスト手順
- チェックリスト

## 🎯 リリース管理

### バージョニング

セマンティックバージョニングを使用：

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: 破壊的変更
- **MINOR**: 新機能追加
- **PATCH**: バグ修正

### リリース手順

1. **開発完了**
   ```bash
   # 変更をコミット
   git add .
   git commit -m "Add new feature"
   git push origin main
   ```

2. **バージョン更新**
   - `package_info.json` のバージョンを更新
   - `README.md` のバージョンを更新

3. **タグ作成**
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```

4. **自動リリース**
   - GitHub Actionsが自動実行
   - リリースノートが自動生成
   - ファイルが自動アップロード

## 📊 統計と分析

### GitHub Insights

- **Traffic**: ダウンロード数、クローン数
- **Contributors**: 貢献者数
- **Commits**: コミット履歴
- **Releases**: リリース履歴

### 人気指標

- **Stars**: プロジェクトの評価
- **Forks**: フォーク数
- **Issues**: 問題報告
- **Pull Requests**: 貢献

## 🔍 トラブルシューティング

### よくある問題

#### 1. GitHub Actionsが失敗する
- **原因**: 依存関係の問題
- **解決**: requirements.txtを確認

#### 2. ファイルがアップロードされない
- **原因**: ファイルサイズ制限
- **解決**: 大きなファイルは.gitignoreに追加

#### 3. リリースノートが表示されない
- **原因**: RELEASE_NOTES.mdの形式
- **解決**: Markdown形式を確認

### ログの確認

- **GitHub Actions**: Actionsタブでログを確認
- **ローカル**: pack_generator.logを確認

## 📞 サポート

### コミュニティ

- **Issues**: バグ報告・機能要求
- **Discussions**: 一般的な質問
- **Wiki**: 詳細ドキュメント

### ドキュメント

- **README.md**: 基本的な使用方法
- **docs/**: 詳細ドキュメント
- **examples/**: サンプルファイル

## 🎉 配布成功のポイント

### 1. 品質の確保
- 十分なテストの実施
- エラーハンドリングの充実
- ドキュメントの充実

### 2. コミュニティの構築
- 積極的なIssue対応
- 貢献者の歓迎
- 定期的なアップデート

### 3. プロモーション
- 適切なトピック設定
- 分かりやすい説明
- スクリーンショットの活用

### 4. 継続的な改善
- ユーザーフィードバックの収集
- 新機能の追加
- パフォーマンスの向上

---

このガイドに従って、効果的なGitHub配布を行ってください！ 