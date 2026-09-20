# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project Overview

Claude Code Deep Dive Workshop — a Korean-language training curriculum distributed as rendered PDF slide decks plus a searchable markdown archive of every code example. This is a **content repository**: no build system, no tests, no application code.

## Repository Layout

- `20260525/`, `20260703/`, `20260905/` — chapter PDFs, one directory per curriculum edition (date-stamped `YYYYMMDD`). `20260905/` is the latest edition, newly authored against Claude Code v2.1.261. Six chapters per edition: Ch1 Overview, Ch2 Agents & Subagents, Ch3 Admin Setup, Ch4 Settings, Ch5 CLI Reference, Ch6 Agent SDK. `20260901/` holds a session-ordered (D1/D2-prefixed) delivery build of the decks; do not name the client in documents.
- `tech_doc/` — supplementary technical documents (`ClaudeCode-Architecture.pdf`, `Claude_Cost_Efficiency.pdf`), kept separate from the chapter curriculum.
- `Script/workshop-code/` — 502 extracted code snippets as markdown, organized `chN-topic/part-NN-slug/NNN-slug.md` where `NNN` is the source slide number. Each file contains the slide title, the code block, and a Korean speaker note.
- `ccw-hands-on-lab/` — HTML hands-on lab guides in the 2026-09-19 "My Workshop" reader build: chapter labs (`ClaudeCode_Ch{1..6}_HandsOnLab.html`), capstone missions 1–6 (`ClaudeCode_Capstone{1..6}_HandsOnLab.html`), a capstone setup guide, a preflight-check page, reference pages 1–3, a session intro (`eDM.html`), and the portal entry point `index.html`. Pages load a shared `assets/` directory (reader/workshop CSS and JS, per-page `assets/legacy/*.css`, NanumSquare fonts, highlight.js) by relative path, so HTML files and `assets/` must stay in the same directory. `v1/` archives the previous standalone build, including legacy capstone labs A–D and the old `theme.css`/`theme.js`. Published to the `whchoi98/whchoi98.github.io` repository at `/ccw-hands-on-lab/`.
- `README.md`, `CHANGELOG.md` — bilingual documents (English section first, Korean second).

## Conventions

- **PDFs are rendered artifacts — never edit them.** They are regenerated from source decks maintained outside this repository.
- **Lab HTML pages are also regenerated** from source decks outside this repository — page-level fixes can be silently overwritten on the next regeneration, so re-audit after bulk lab updates. The current build carries no inline `<style>`: `assets/theme.js` sets `html[data-theme]` from `localStorage` or the OS preference, and theme rules live in `assets/reader.css`, `assets/workshop.css`, and the per-page `assets/legacy/*.css`; light-mode fixes belong in those files. The archived `v1/` pages instead embed a `<style id="hol-theme">` block with a `#themeToggle` button. The light palette targets projector legibility.
- After changing `ccw-hands-on-lab/`, sync the directory to the `whchoi98.github.io` repository (`rsync -a --delete --exclude='*.zip'`) so GitHub Pages stays current. The offline archive `ccw-hands-on-lab/ClaudeCode_Workshop_HandsOnLab.zip` is not committed: the Pages deploy workflow runs `scripts/build-lab-zip.sh` before `jekyll build`, packing the top-level pages, `START_HERE.txt`, and `assets/` (excluding `v1/`) with the toolbar ZIP button stripped from the offline copy; run the same script locally before a local Jekyll build to verify. Every lab page's top-right toolbar links that archive via the `<!-- zip-download -->` block, and `assets/reader.css` hides the button label below 560px. Update the `docs/workshop/claude-code-workshop.md` nav page when labs are added or renamed.
- Snippet filenames follow `NNN-meaningful-slug.md` (`NNN` = slide number). Keep numbering stable. When changing snippet content, cite the source slide number in the commit body.
- Bilingual docs: identical structure in both language sections. Language toggle uses HTML `<a href="#english"><img ...></a>` badges with ASCII anchors and explicit `<a id="english">` / `<a id="korean">` tags — not Markdown badge links. No emojis in documents.
- Changelog entries: English imperative ("Add X") / Korean 명사형 종결 ("X 추가"). Category headings stay in English in both sections.
- Do not mention AWS organization or standard names (AWS Korea, V-team, AWS PPT template, AWS Confidential) in documents; use neutral wording such as "consistent design system" and "Proprietary" license.
- Commits follow Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).
- Version strings live in two places — bump both on release: the README version badge (`img.shields.io/badge/version-X.Y.Z-green.svg`) and the CHANGELOG compare-link definitions at the bottom of each language section. Releases are tagged `vX.Y.Z` (first tag: v1.1.0; 1.0.x were never tagged, so their compare links do not resolve).
- Ignore `.DS_Store` files; they are macOS artifacts.

## Common Tasks

```bash
# Find snippets by keyword
grep -rn "PreToolUse" Script/workshop-code/

# Find snippets by filename
find Script/workshop-code/ -name "*auth*"

# List snippets in a part
ls Script/workshop-code/ch6-sdk/part-01-sdk-basics/
```
