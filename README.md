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

Same keymap as Temper; BLE name **`Chocofi`** (distinct from Temper). Matrix matches Temper (36-key chocofi geometry).

| File | Use |
|---|---|
| `chocofi_macos_left.uf2` / `_right.uf2` | Mac |
| `chocofi_linux_left.uf2` / `_right.uf2` | Linux |
| `chocofi_settings_reset_*.uf2` | Clear BLE bonds |

Artifact: **`chocofi-firmware`**

Flash order if the split misbehaves: **settings_reset both halves → real firmware both → power left then right**.

## Flash (USB)

1. Double-tap reset → `NICENANO` volume.
2. Copy the matching half UF2; wait for auto-eject.
3. **Left** = USB to computer (central). **Right** = USB power (or battery) for split link.

```bash
cp ~/Downloads/temper-fw/temper_macos_left.uf2 /Volumes/NICENANO/; sync
# then right half:
cp ~/Downloads/temper-fw/temper_macos_right.uf2 /Volumes/NICENANO/; sync
```

## Layout notes

- Ported from Totem 38-key position map → Temper 36-key (outer pinkies removed).
- Sticky-shift combos **S+T** / **N+E**, vertical brackets, NAV U-pivot browser
  nav, `!` on `./`, `£` on `Y+'`, backspace autorepeat, mouse keys, etc. match
  Totem intent.
- Source of truth while iterating: keep behaviour aligned with
  `~/codmiryoku/config/totem*.keymap`, then re-run `port_from_totem.py` or edit
  `config/temper*.keymap` directly.

## Repo layout

- `boards/shields/temper/` — shield from [raeedcho/temper-zmk-config](https://github.com/raeedcho/temper-zmk-config) (matrix / GPIO)
- `config/temper.keymap` — macOS keymap
- `config/temper_linux.keymap` — Linux keymap
- `config/temper.conf` — shared Kconfig
- `config/west.yml` — ZMK **v0.3** (same pin family as Totem/Piantor)
