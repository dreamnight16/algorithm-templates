#!/usr/bin/env bash
set -euo pipefail

# === Build printable PDF from algorithm notebook ===
# Requires: pandoc, weasyprint (brew install weasyprint)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
INPUT="$PROJECT_DIR/algorithm-notebook-cn.md"
OUTPUT="$PROJECT_DIR/algorithm-notebook-cn.pdf"
STYLE="$SCRIPT_DIR/print-style.css"

echo "==> Converting Markdown → PDF"
echo "    Input : $INPUT"
echo "    Output: $OUTPUT"

TMP_HTML=$(mktemp -t algo-notebook-XXXXXX.html)
trap 'rm -f "$TMP_HTML"' EXIT

# Step 1: pandoc: Markdown → HTML5
# --mathml converts TeX math to MathML for weasyprint compatibility
# --syntax-highlighting replaces deprecated --highlight-style
pandoc "$INPUT" \
  --from markdown+smart \
  --to html5 \
  --standalone \
  --toc --toc-depth=3 \
  --metadata title="ICPC/OI 算法模板集" \
  --metadata lang="zh-CN" \
  --syntax-highlighting=tango \
  --mathml \
  --css="$STYLE" \
  -o "$TMP_HTML"

echo "    HTML: $TMP_HTML"

# Step 2: weasyprint: HTML → PDF
weasyprint "$TMP_HTML" "$OUTPUT" \
  --encoding utf-8 \
  --presentational-hints \
  --optimize-images

echo ""
echo "==> Done: $OUTPUT"
ls -lh "$OUTPUT"
