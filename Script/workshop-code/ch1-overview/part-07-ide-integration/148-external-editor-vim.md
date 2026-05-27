# Slide 148: External editor Vim

**Part 7: IDE INTEGRATION**

## Code Blocks

### Vim integration

```bash
# 1. tmux와 함께 사용 (권장)
# 첫 화면: Vim으로 코드 편집
# 두 번째 분할: claude 세션

tmux new -s coding
# Ctrl+B → % : 수평 분할
# 왼쪽: vim src/app.js
# 오른쪽: claude

# 2. Vim 플러그인 (선택)
# vim-claude (커뮤니티 플러그인)
" .vimrc
Plug 'username/vim-claude'

# 명령:
:ClaudeAsk "이 함수를 리팩토링해 주세요"
:ClaudeSelection      " 선택 영역 → Claude

# 3. 키 매핑 권장
nnoremap <leader>cc :silent !claude -p "<C-r>+"<CR>
" Yank 후 leader+cc로 Claude 호출
```

## Speaker Notes

Vim 사용자를 위한 통합 방법입니다.
1단계 tmux와 함께 사용하는 것이 권장 패턴입니다.
한 화면에는 Vim으로 코드를 편집하고 다른 분할 화면에서 claude 세션을 운영합니다.
tmux의 분할 기능 Ctrl B 백분율 기호로 수평 분할 후 한쪽은 vim, 다른 쪽은 claude를 실행합니다.
2단계 커뮤니티 Vim 플러그인을 활용하면 ClaudeAsk 명령으로 직접 호출할 수 있고 ClaudeSelection으로 선택 영역을 전송할 수 있습니다.
3단계 키 매핑으로 leader cc 같은 짧은 키 조합을 만들면 yank한 텍스트를 즉시 Claude에 전송할 수 있습니다.
