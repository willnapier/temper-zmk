# Temper ZMK (Will Napier)

ZMK config for the [Temper](https://github.com/raeedcho/temper) 36-key split
(**nice!nano**), kept in line with
[`codmiryoku`](https://github.com/willnapier/codmiryoku) Totem keymaps — minus the
two outer pinky keys.

## Role (2026-07-24)

| Board | Host | BLE name | Notes |
|---|---|---|---|
| **Temper** | **Mac only** | `Temper` | Maintained alongside Totem Mac keymap |
| Totem ×2 | Mac | `Totem-Mac-1`, `Totem-Mac-2` | See codmiryoku |
| Totem ×1 | Linux | `Totem-Linux-1` | `Totem-Linux-2` built but no HW yet |
| Chocofi | — | — | **Deprecated** — not built in CI |

`config/temper_linux.keymap` remains in-tree for a possible later Linux swap; CI does not build it.

## Hardware

| | |
|---|---|
| Keyboard | Temper (choc, 3×5+3 per half) |
| MCU | nice!nano v2 |
| Display | **nice!view** (`nice_view_adapter` + `nice_view`) |
| Central | **Left** half |

## Firmware artifacts (GitHub Actions)

Artifact: **`temper-firmware`**

| File | Use |
|---|---|
| `temper_left.uf2` / `temper_right.uf2` | Mac (Cmd) Totem-parity + nice!view |
| `temper_settings_reset_*.uf2` | Clear BLE bonds |

Flash order if the split misbehaves: **settings_reset both halves → real firmware both → power left then right**.

## Flash (USB)

1. Double-tap reset → `NICENANO` volume (or whatever `ls /Volumes` shows).
2. Copy the matching half UF2; `sync`; wait for auto-eject.
3. **Left** = USB to computer (central). **Right** = USB power (or battery) for split link.

```bash
cp ~/Desktop/temper-firmware/temper_left.uf2 /Volumes/NICENANO/; sync
cp ~/Desktop/temper-firmware/temper_right.uf2 /Volumes/NICENANO/; sync
```

## Layout notes (aligned with Totem)

- Outer thumbs: dual Shift (tap sticky / hold held); **no** paren morphs
- Esc: **Q+W** and **Y+'** (bilateral); BASE £ combo removed → NUM+Shift+D
- `:` = **J+L**, `;` = **B+P** (horizontal 2026-07-24); backup Shift+`.` / Shift+`,` (Urob); `-` = **N+H** vertical
- Brackets vertical including `<>` on Q+A / '+O
- MEDIA = hold **xcd**; FUN = sticky **h,.**
- Source of truth: `config/temper.keymap` ↔ `~/codmiryoku/config/totem.keymap`

## Repo layout

- `boards/shields/temper/` — shield from [raeedcho/temper-zmk-config](https://github.com/raeedcho/temper-zmk-config)
- `boards/shields/chocofi/` — **deprecated** (not built)
- `config/temper.keymap` — macOS keymap (active)
- `config/temper_linux.keymap` — Linux twin (not built; keep for later)
- `config/temper.conf` — shared Kconfig + BLE name `Temper`
- `config/west.yml` — ZMK **v0.3**
