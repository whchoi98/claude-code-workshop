#!/usr/bin/env bash
# 실습 서버 한 대를 Day 1 LAB 상태로 만든다. 여러 번 실행해도 된다.
#   bash scripts/setup-lab.sh
# 참가자가 랩 가이드의 준비 1번에서 직접 실행한다. 진행자가 미리 실행해 두어도 된다.
# 하는 일: 플러그인 마켓플레이스와 작업 폴더를 홈에 복사하고, 필요한 Python 라이브러리를 설치하고, 동작을 확인한다.
# 하지 않는 일: 플러그인 설치와 서울 MCP 등록. 이 둘은 참가자가 랩에서 직접 한다.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIT_HOME="${KIT_HOME:-$HOME/workshop-kit}"
LAB_HOME="${LAB_HOME:-$HOME/seoul-lab}"

stop() {
  echo
  echo "[중단] $1"
  echo "       이 화면을 그대로 두고 진행자를 불러 주세요."
  exit 1
}

have_libs() { python3 -c "import openpyxl, pptx" 2>/dev/null; }
pip_install() { python3 -m pip install --user --quiet "$@" openpyxl python-pptx >/dev/null 2>&1; }

# pip 이 없는 서버에서만 쓴다. 관리자 권한을 암호 없이 쓸 수 있을 때만 시스템 패키지로 pip 을 넣는다.
system_pip() {
  local sudo=""
  [ "$(id -u)" -eq 0 ] || sudo="sudo -n"
  if command -v dnf >/dev/null 2>&1; then
    $sudo dnf install -y -q python3-pip
  elif command -v apt-get >/dev/null 2>&1; then
    $sudo apt-get update -qq && $sudo apt-get install -y -qq python3-pip
  else
    return 1
  fi
}

command -v python3 >/dev/null 2>&1 || stop "python3 이 없습니다."

echo "[1/4] 플러그인 마켓플레이스를 $KIT_HOME 에 둡니다"
rm -rf "$KIT_HOME"
cp -r "$HERE/marketplace" "$KIT_HOME"

echo "[2/4] 작업 폴더를 $LAB_HOME 에 둡니다 (이미 만든 work, out 은 그대로 둡니다)"
mkdir -p "$LAB_HOME/work" "$LAB_HOME/out"
cp -r "$HERE/workspace/.claude" "$HERE/workspace/CLAUDE.md" "$HERE/workspace/data" "$LAB_HOME/"

echo "[3/4] Python 라이브러리를 확인합니다"
if ! have_libs; then
  echo "  openpyxl, python-pptx 를 설치합니다"
  if ! python3 -m pip --version >/dev/null 2>&1; then
    echo "  pip 이 없어 먼저 설치합니다"
    python3 -m ensurepip --user >/dev/null 2>&1 || system_pip >/dev/null 2>&1 || true
  fi
  # 둘째 시도는 배포판이 pip 설치를 막아 둔 서버(Ubuntu 23.04 이후 등)에서 내 홈에만 설치하는 방법이다.
  pip_install || pip_install --break-system-packages || true
fi
have_libs || stop "Python 라이브러리 openpyxl, python-pptx 를 설치하지 못했습니다."
python3 "$KIT_HOME/plugins/seoul-kit/kit/kit.py" doctor

echo "[4/4] 예시 세 가지를 만들어 봅니다"
TRY="$(mktemp -d)"
for kind in board sheet deck; do
  python3 "$KIT_HOME/plugins/seoul-kit/kit/kit.py" "$kind" "$KIT_HOME/plugins/seoul-kit/kit/examples/$kind.json" --dir "$TRY" --no-serve | head -1
done
rm -rf "$TRY"

echo
echo "준비가 끝났습니다. 랩 가이드의 다음 단계(플러그인 설치)로 넘어가세요."
echo "  플러그인 마켓플레이스: $KIT_HOME"
echo "  작업 폴더:             $LAB_HOME"
