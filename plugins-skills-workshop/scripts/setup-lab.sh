#!/usr/bin/env bash
# 참가자 실습 서버 한 대를 Day 1 LAB 상태로 만든다. 여러 번 실행해도 된다.
#   bash scripts/setup-lab.sh
# 하는 일: 플러그인 마켓플레이스와 작업 폴더를 홈에 복사하고, 필요한 Python 라이브러리를 설치하고, 동작을 확인한다.
# 하지 않는 일: 플러그인 설치와 서울 MCP 등록. 이 둘은 참가자가 랩에서 직접 한다.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT_HOME="${KIT_HOME:-$HOME/workshop-kit}"
LAB_HOME="${LAB_HOME:-$HOME/seoul-lab}"

echo "[1/4] 플러그인 마켓플레이스를 $KIT_HOME 에 둡니다"
rm -rf "$KIT_HOME"
cp -r "$HERE/marketplace" "$KIT_HOME"

echo "[2/4] 작업 폴더를 $LAB_HOME 에 둡니다 (이미 만든 work, out 은 그대로 둡니다)"
mkdir -p "$LAB_HOME/work" "$LAB_HOME/out"
cp -r "$HERE/workspace/.claude" "$HERE/workspace/CLAUDE.md" "$HERE/workspace/data" "$LAB_HOME/"

echo "[3/4] Python 라이브러리를 확인합니다"
if ! python3 -c "import openpyxl, pptx" 2>/dev/null; then
  python3 -m pip install --user --quiet openpyxl python-pptx
fi
python3 "$KIT_HOME/plugins/seoul-kit/kit/kit.py" doctor

echo "[4/4] 예시 세 가지를 만들어 봅니다"
TRY="$(mktemp -d)"
for kind in board sheet deck; do
  python3 "$KIT_HOME/plugins/seoul-kit/kit/kit.py" "$kind" "$KIT_HOME/plugins/seoul-kit/kit/examples/$kind.json" --dir "$TRY" --no-serve | head -1
done
rm -rf "$TRY"

echo
echo "준비가 끝났습니다. 참가자는 랩 가이드의 준비 단계부터 시작합니다."
echo "  플러그인 마켓플레이스: $KIT_HOME"
echo "  작업 폴더:             $LAB_HOME"
