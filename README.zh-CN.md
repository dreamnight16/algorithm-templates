<!-- language-bar -->
<div align="center">

[English](README.en.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md)

</div>

---

# ICPC/OI 算法模板集

**我个人的竞赛编程板子，公开出来希望能帮到大家。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![C++17/20](https://img.shields.io/badge/C%2B%2B-17%2F20-00599C.svg?logo=c%2B%2B)](https://isocpp.org/)

## 关于本仓库

这是我在竞赛编程中积累的个人算法模板集，涵盖数据结构、图论、数学、字符串、动态规划、计算几何、网络流及高级技巧。所有实现参考了 KACTL、jiangly 等竞赛标杆，带有中英双语注释，方便自己赛时使用，也希望能对各位有所帮助。

板子还在不断完善中，**欢迎大家指出错误、提 Issue 或 PR，共同学习进步。**

## 文档

- **[algorithm-notebook-cn.md](algorithm-notebook-cn.md)** — 完整模板集（~10,700 行）
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — 贡献指南
- **[SECURITY.md](SECURITY.md)** — 安全漏洞报告

## 特性

- **10+ 章节**覆盖竞赛编程主要领域
- **~10,000 行** C++ 模板，参考 KACTL、jiangly 等竞赛标杆
- **复杂度速查表**，每个算法标注时间/空间复杂度
- **中英双语注释**，逐步解释算法原理
- **即拷即用**，每个代码块依赖最小化、可独立编译

## 快速开始

```bash
git clone https://github.com/sixtdreanight/algorithm-templates.git
cd algorithm-templates

# 浏览模板
cat algorithm-notebook-cn.md

# 验证代码可编译
make verify

# 编译测试某个片段
g++ -std=c++20 -O2 -Wall test.cpp -o test && ./test
```

## 反馈与贡献

发现错误或有改进建议？欢迎提 [Issue](../../issues) 或直接发 [Pull Request](../../pulls)。大家一起完善这个板子 🤝

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

## 参考

- [CP-Algorithms](https://cp-algorithms.com/)
- [OI Wiki](https://oi-wiki.org/)
- [KACTL](https://github.com/kth-competitive-programming/kactl)
