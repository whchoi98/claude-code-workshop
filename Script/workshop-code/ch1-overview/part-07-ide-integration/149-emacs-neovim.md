# Slide 149: Emacs/Neovim

**Part 7: IDE INTEGRATION**

## Code Blocks

### Emacs/Neovim

```bash
# Neovim - claude.nvim 플러그인 (커뮤니티)
-- ~/.config/nvim/lua/plugins/claude.lua
return {
  "anthropics/claude.nvim",
  config = function()
    require("claude").setup({
      model = "sonnet",
      keymaps = {
        ask = "<leader>ca",
        edit = "<leader>ce",
        explain = "<leader>cx",
      },
    })
  end,
}

# Emacs - claude.el (커뮤니티)
;; init.el
(use-package claude
  :ensure t
  :bind (("C-c C-a" . claude-ask)
         ("C-c C-e" . claude-edit-region)))

# 두 경우 모두 기본은 claude CLI 호출
# 따라서 CLI 설치만 되어 있으면 즉시 사용 가능
```

## Speaker Notes

Neovim과 Emacs 사용자를 위한 플러그인 생태계입니다.
Neovim은 claude.nvim 커뮤니티 플러그인이 가장 일반적입니다.
lazy.nvim 또는 packer.nvim 같은 플러그인 매니저에 등록하면 됩니다.
setup 함수에서 모델과 키맵을 지정할 수 있습니다.
leader ca는 ask, leader ce는 edit, leader cx는 explain 같은 키맵이 일반적입니다.
Emacs는 claude.el 패키지를 use-package로 등록하고 C-c C-a 같은 키 바인딩으로 사용합니다.
두 플러그인 모두 내부적으로는 claude CLI를 호출하므로 CLI 설치만 되어 있으면 즉시 사용 가능합니다.
