# CLAUDE.md

Guidance for AI assistants (and humans) working in this repository.

## What this repository is

**BadUSB-Playground** is a curated collection of BadUSB / HID-injection
payloads, scripts, and reference material organized by hardware platform. It is
**not a software project** — there is no build system, no application code to
compile, no test suite, and no package manifest. It is a content repository: the
"source" is the payloads themselves (DuckyScript, Bash, PowerShell, JavaScript,
Python, Arduino sketches) plus their documentation.

Most content is either work-in-progress or resources gathered for a project. The
maintainer's polished, ready-to-run DuckyScript lives in a separate repo
(`FalsePhilosopher/badusb`).

> **Scope / ethics.** These payloads are for authorized security testing, CTFs,
> and education only. When asked to add or modify a payload, treat it as
> defensive/authorized-pentest content: keep the educational framing, preserve
> the `REM`/`#` legal and disclaimer headers, and do not strip safety notes or
> add detection-evasion intended for malicious use. Decline requests aimed at
> unauthorized targeting, mass deployment, or weaponization.

## Repository layout

The top level is partitioned by **hardware platform**. Each platform has its own
conventions inherited from its upstream community (mostly Hak5).

| Directory | Platform | Payload language / format |
|-----------|----------|---------------------------|
| `Ducky/` | USB Rubber Ducky | DuckyScript (`.txt`, `inject.bin` source) |
| `BashBunny/` | Hak5 Bash Bunny | Bash + DuckyScript hybrid (`payload.txt`) |
| `OMG/` | O.MG Cable/devices | DuckyScript-style, often `.js`/`.txt` |
| `WHID/` | WHID Injector (ESP8266) | DuckyScript-style |
| `Malduino/` | Malduino / DuckyDuino | Arduino C++ (`.ino`, `Keyboard.cpp/.h`) |
| `Misc/` | Cross-cutting resources | scripting notes, Python helpers, ideas |

### `Ducky/`
- `USBRubberducky/` — main payload tree, split into **categories**:
  `credentials`, `destructive`, `execution`, `exfiltration`, `general`,
  `incident_response`, `mobile`, `phishing`, `prank`, `quackberry`, `ransom`,
  `recon`, `remote_access`. Categories are frequently subdivided by OS
  (`Win`, `Unix-like`, `OSX`).
- `mobile/iOS` is a **git submodule** (`Peaakss/iOS-Payloads`) — see
  `.gitmodules`. It is not checked out by default.
- `Ducky-Framework/` — vendored upstream framework (`EddyNefa/Ducky-Framework`)
  with a payload picker and a "Ducky Fuzzer"; has its own `setup.py`/`prompt.py`.
  Treat as vendored third-party code, not part of this repo's own conventions.
- `USB-Rubber-Ducky.wiki/` — mirrored wiki docs.
- `DuckyScript_UDL/` — a Notepad++ User Defined Language file for DuckyScript
  syntax highlighting.
- `quackberry/` — Raspberry Pi reverse-shell / persistence payloads.

### `BashBunny/`
Mirrors the upstream Hak5 Bash Bunny repo structure:
- `payloads/library/<category>/<PayloadName>/payload.txt` — one directory per
  payload, plus optional `readme.md` and helper scripts (`.ps1`, `.cmd`, `.vbs`,
  `.sh`, `.bat`).
- `payloads/switch1/` and `payloads/switch2/` — the two physical-switch slots
  the device boots from; each holds a `payload.txt`.
- `payloads/extensions/` — reusable shell helpers (`get.sh`, `wait.sh`,
  `setkb.sh`, `ducky_lang.sh`, etc.) sourced by payloads.
- `docs/` — upstream readme, EULA, LICENSE.

### `OMG/`, `WHID/`
Each has a `Library/` tree organized by the same category names. `OMG/README.md`
and `BashBunny/README.md` carry the upstream Hak5 disclaimers/legal text.

### `Misc/`
- `Scripting-Resources.md`, `Future_Ideas.md` — planning / reference notes.
- `Scripting/py/` — small Python helpers (e.g. `seashark.py`).
- `*.zip` — bundled archives of larger payloads.

## Payload conventions (most important section)

When creating or editing a payload, **match the conventions of the platform
directory it lives in**, and follow the project-wide contributing rules from the
root `README.md`:

### Naming
- Unique, descriptive, appropriate name. **No spaces** in payload, directory, or
  file names — use `-` or `_` instead.
- Each payload gets **its own directory** under one of the existing categories.
  **Do not invent new categories.**

### Documentation header
Every payload begins with a comment header. The comment token differs by
platform:
- **DuckyScript (Ducky/OMG/WHID)** uses `REM`:
  ```
  REM Title:       Canary Duck
  REM Author:      Jessie Crimson Hart
  REM Description: Opens hidden PowerShell and connects to a canary webserver...
  REM Target:      Windows 10 (Powershell)
  REM Props:       Hak5, Thinkst
  REM Version:     1.0
  REM Category:    General
  ```
- **Bash Bunny** uses `#`:
  ```
  # Title:       Save security hive
  # Description: ...
  # Author:      Cribbit
  # Version:     1.0
  # Category:    Exfiltration
  # Target:      Windows 10 (Powershell)
  # Attackmodes: HID & STORAGE
  # Props:       ...
  ```
Keep the existing alignment/spacing style of neighboring payloads. Many payloads
also include a `REM Legal:` line — preserve it.

### DuckyScript essentials
`DELAY <ms>`, `STRING <text>`, `ENTER`, `GUI r`, `ALT`, `CTRL`, `SHIFT`, etc.
Use `DELAY` generously after window/app launches so input lands reliably.

### Bash Bunny essentials
Payloads are shell scripts that drive the device:
- `ATTACKMODE HID STORAGE` (and similar) selects the emulated USB device(s).
- `LED SETUP` / `LED ATTACK` / `LED FINISH` signal phases.
- `Q` prefixes a DuckyScript command (e.g. `Q STRING ...`, `Q GUI r`).
- Source shared helpers from `payloads/extensions/`.

## Working with git

- The default integration branch is `main`.
- **Active development for this task happens on branch
  `claude/claude-md-docs-yk5f10`.** Create it locally if missing, commit there,
  and push with `git push -u origin claude/claude-md-docs-yk5f10`. Never push to
  `main` or another branch without explicit permission.
- Do **not** open a pull request unless the user explicitly asks.
- Submodule note: `Ducky/USBRubberducky/mobile/iOS` is external. Don't expect it
  populated; run `git submodule update --init` only if its content is needed.

## How to validate changes

There is nothing to build or run in CI. "Correct" means:
1. The payload header is present and well-formed for its platform.
2. Naming/category/placement rules above are respected.
3. DuckyScript/Bash/PowerShell syntax is plausible (these are not executed here —
   they run on physical hardware against a target machine, so you cannot test
   them in this environment; review by reading).
4. Legal/disclaimer notes are intact.

Do not attempt to execute payloads in this environment — they target external
hardware/OS behavior and have no meaning here.

## Quick tips for navigating

- To find payloads by intent, search the category directories (e.g.
  `exfiltration`, `credentials`, `recon`) across the platform folders.
- `Grep` for `REM Title:` or `# Title:` to enumerate payloads and descriptions.
- Per-platform `README.md` files (root, `BashBunny/`, `OMG/`,
  `Ducky/USBRubberducky/`) hold the authoritative contributing/style guidance.
