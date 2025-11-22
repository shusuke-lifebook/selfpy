# WSL2 + Ubuntu + Python3 + VSCode(Remote) 学習環境セットアップ

## 1. WSL2 + Ubuntu の準備
- WindowsにWSL2をインストール
- Ubuntuを導入
- VSCodeに **Remote - WSL** 拡張をインストール

## 2. Python3 仮想環境の作成
```bash
cd ~/projects/my-python-app
python3 -m venv .venv
source .venv/bin/activate
