# Temper ZMK (Will Napier)

ZMK config for the [Temper](https://github.com/raeedcho/temper) 36-key split
(**nice!nano**), carrying the same behaviour as
[`codmiryoku`](https://github.com/willnapier/codmiryoku) on the Totem — minus the
two outer pinky keys.

## Hardware

| | |
|---|---|
| Keyboard | Temper (choc, 3×5+3 per half) |
| MCU | nice!nano v2 |
| Display | **nice!view** (`nice_view_adapter` + `nice_view`) |
| Central | **Left** half |

## Firmware artifacts (GitHub Actions)

### Temper (nice!view)

| File | Use |
|---|---|
| `temper_macos_left.uf2` / `_right.uf2` | Mac Totem-parity (Cmd) + nice!view |
| `temper_linux_left.uf2` / `_right.uf2` | Linux Totem-parity |
| `temper_settings_reset_*.uf2` | Clear BLE bonds |

Artifact: **`temper-firmware`**

### Chocofi (no display; same layout)

**Same keymap source as Temper** — GHA always passes
`KEYMAP_FILE=config/temper.keymap` (Mac) or `temper_linux.keymap` (Linux).
BLE names (2026-07-24): **Temper Mac** / **Temper Linux**, **Chocofi Mac** / **Chocofi Linux**
(via `EXTRA_CONF_FILE` in CI). Matrix = 36-key chocofi geometry.

| File | Use |
|---|---|
| `chocofi_macos_left.uf2` / `_right.uf2` | Mac |
| `chocofi_linux_left.uf2` / `_right.uf2` | Linux |
| `chocofi_settings_reset_*.uf2` | Clear BLE bonds |

Artifact: **`chocofi-firmware`**

`boards/shields/chocofi/chocofi.keymap` is a **deprecated stub** (not used in CI).
Do not edit it for layout work — edit `config/temper*.keymap` only.

Flash order if the split misbehaves: **settings_reset both halves → real firmware both → power left then right**.

## Flash (USB)

1. Double-tap reset → `NICENANO` volume (or whatever `ls /Volumes` shows).
2. Copy the matching half UF2; `sync`; wait for auto-eject.
3. **Left** = USB to computer (central). **Right** = USB power (or battery) for split link.

```bash
cp ~/Desktop/temper-fw-esc-yquote-2026-07-19/temper-firmware/temper_macos_left.uf2 /Volumes/NICENANO/; sync
cp ~/Desktop/temper-fw-esc-yquote-2026-07-19/temper-firmware/temper_macos_right.uf2 /Volumes/NICENANO/; sync
```

## Layout notes (2026-07-19 experiment, aligned with Totem)

- Outer thumbs: dual Shift (tap sticky / hold held); **no** paren morphs
- Esc: **Q+W** and **Y+'** (bilateral); BASE £ combo removed → NUM+Shift+D
- `:` = **J+L**, `;` = **B+P** (horizontal trial 2026-07-24); backup Shift+`.` / Shift+`,` (Urob); `-` = **N+H** vertical
- Brackets vertical including `<>` on Q+A / '+O
- MEDIA = hold **xcd**; FUN = sticky **h,.**
- Source of truth: `config/temper*.keymap` ↔ `~/codmiryoku/config/totem*.keymap`

## Repo layout

- `boards/shields/temper/` — shield from [raeedcho/temper-zmk-config](https://github.com/raeedcho/temper-zmk-config) (matrix / GPIO)
- `config/temper.keymap` — macOS keymap
- `config/temper_linux.keymap` — Linux keymap
- `config/temper.conf` — shared Kconfig
- `config/west.yml` — ZMK **v0.3** (same pin family as Totem/Piantor)
