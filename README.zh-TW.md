<!-- language-bar -->
<div align="center">

[English](README.en.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

</div>

---

# ICPC/OI 演算法模板集

**我個人的競賽程式設計板子，公開出來希望能幫到大家。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![C++17/20](https://img.shields.io/badge/C%2B%2B-17%2F20-00599C.svg?logo=c%2B%2B)](https://isocpp.org/)

## 關於本倉庫

這是我在競賽程式設計中積累的個人演算法模板集，涵蓋資料結構、圖論、數學、字串、動態規劃、計算幾何、網路流及進階技巧。所有實作參考了 KACTL、jiangly 等競賽標竿，附有中英雙語註釋，方便自己賽時使用，也希望能對各位有所幫助。

板子還在不斷完善中，**歡迎大家指出錯誤、提 Issue 或 PR，共同學習進步。**

## 文件

- **[algorithm-notebook-cn.md](algorithm-notebook-cn.md)** — 完整模板集（~10,700 行）
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — 貢獻指南
- **[SECURITY.md](SECURITY.md)** — 安全漏洞回報

## 特性

- **10+ 章節**覆蓋競賽程式設計主要領域
- **~10,000 行** C++ 模板，參考 KACTL、jiangly 等競賽標竿
- **複雜度速查表**，每個演算法標註時間/空間複雜度
- **中英雙語註釋**，逐步解釋演算法原理
- **即拷即用**，每個程式碼區塊依賴最小化、可獨立編譯

## 快速開始

```bash
git clone https://github.com/sixtdreanight/algorithm-templates.git
cd algorithm-templates

# 瀏覽模板
cat algorithm-notebook-cn.md

# 驗證程式碼可編譯
make verify

# 編譯測試某個片段
g++ -std=c++20 -O2 -Wall test.cpp -o test && ./test
```

## 回饋與貢獻

發現錯誤或有改進建議？歡迎提 [Issue](../../issues) 或直接發 [Pull Request](../../pulls)。大家一起完善這個板子 🤝

## 授權條款

MIT — 詳見 [LICENSE](LICENSE)。

## 參考

- [CP-Algorithms](https://cp-algorithms.com/)
- [OI Wiki](https://oi-wiki.org/)
- [KACTL](https://github.com/kth-competitive-programming/kactl)
