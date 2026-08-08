<!-- language-bar -->
<div align="center">

[English](README.en.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

</div>

---

# ICPC/OI アルゴリズムテンプレート集

**個人の競技プログラミング用コードブック — 公開することで皆さんのお役に立てれば幸いです。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![C++17/20](https://img.shields.io/badge/C%2B%2B-17%2F20-00599C.svg?logo=c%2B%2B)](https://isocpp.org/)

## 本リポジトリについて

これは競技プログラミングの練習を通じて蓄積した個人のアルゴリズムテンプレート集です。データ構造、グラフ理論、数学、文字列、動的計画法、計算幾何学、ネットワークフロー、高度なテクニックをカバーしています。

現在も改良を続けています。**バグ報告や Issue・PR を歓迎します。共に学び、成長しましょう。**

## ドキュメント

- **[algorithm-notebook-cn.md](algorithm-notebook-cn.md)** — 完全なテンプレート集（約 10,700 行）
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — コントリビューションガイド
- **[SECURITY.md](SECURITY.md)** — 脆弱性の報告

## 特徴

- **10 以上の章**で競技プログラミングの主要分野をカバー
- **約 10,000 行**の C++ テンプレート、KACTL・jiangly を参考
- **計算量チートシート**付き
- **中英バイリンガルコメント**
- **コピペで使える** — 各コードブロックが独立してコンパイル可能

## クイックスタート

```bash
git clone https://github.com/sixtdreanight/algorithm-templates.git
cd algorithm-templates

# テンプレートを閲覧
cat algorithm-notebook-cn.md

# コンパイル確認
make verify

# スニペットをテスト
g++ -std=c++20 -O2 -Wall test.cpp -o test && ./test
```

## フィードバックと貢献

バグを見つけたり改善案があれば、[Issue](../../issues) または [Pull Request](../../pulls) をお寄せください。一緒にこの板を育てましょう 🤝

## ライセンス

MIT — [LICENSE](LICENSE) を参照。

## 参考

- [CP-Algorithms](https://cp-algorithms.com/)
- [OI Wiki](https://oi-wiki.org/)
- [KACTL](https://github.com/kth-competitive-programming/kactl)
