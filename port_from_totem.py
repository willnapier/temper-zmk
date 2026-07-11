#!/usr/bin/env python3
"""Port codmiryoku Totem 38-key keymaps to Temper 36-key positions."""
from pathlib import Path

CONFIG = Path(__file__).resolve().parent / "config"


def port(text: str) -> str:
    text = text.replace("macOS-SPECIFIC TOTEM KEYMAP", "macOS-SPECIFIC TEMPER KEYMAP")
    text = text.replace("LINUX-SPECIFIC TOTEM KEYMAP", "LINUX-SPECIFIC TEMPER KEYMAP")
    text = text.replace(
        "to Totem (38-key).",
        "to Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.",
    )
    text = text.replace(
        "to Totem (38-key); the Linux twin of totem.keymap (macOS).",
        "to Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.\n"
        " * Linux twin of temper.keymap (macOS).",
    )
    text = text.replace("Totem 38-key positions", "Temper 36-key positions")
    text = text.replace("Totem positions", "Temper positions")
    text = text.replace(
        " * Ported from piantor_pro_bt_macos.keymap (42-key) to Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.",
        " * Ported from codmiryoku Totem (38-key) → Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.",
    )
    text = text.replace(
        " * Ported from piantor_pro_bt.keymap (42-key) to Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.\n"
        " * Linux twin of temper.keymap (macOS).",
        " * Ported from codmiryoku Totem Linux (38-key) → Temper (36-key, nice!nano).\n"
        " * Outer pinkies dropped; sticky-shift combos S+T / N+E carry Shift.\n"
        " * Linux twin of temper.keymap (macOS).",
    )

    # Right-hand hold triggers (for left-hand mods)
    text = text.replace(
        "hold-trigger-key-positions = <5 6 7 8 9 15 16 17 18 19 26 27 28 29 30 31 35 36 37>;",
        "hold-trigger-key-positions = <5 6 7 8 9 15 16 17 18 19 25 26 27 28 29 33 34 35>;",
    )
    # Left-hand hold triggers (for right-hand mods)
    text = text.replace(
        "hold-trigger-key-positions = <0 1 2 3 4 10 11 12 13 14 20 21 22 23 24 25 32 33 34>;",
        "hold-trigger-key-positions = <0 1 2 3 4 10 11 12 13 14 20 21 22 23 24 30 31 32>;",
    )

    # Bottom-row combos (Totem 20=L-pinky … 31=R-pinky → Temper 20=Z … 29=/)
    text = text.replace(
        "key-positions = <28 29>;\n            bindings = <&question_combo>;",
        "key-positions = <27 28>;\n            bindings = <&question_combo>;",
    )
    text = text.replace(
        "key-positions = <10 21>;  // A + Z",
        "key-positions = <10 20>;  // A + Z",
    )
    text = text.replace(
        "key-positions = <22 23>;  // X + C",
        "key-positions = <21 22>;  // X + C",
    )
    text = text.replace(
        "key-positions = <23 24>;  // C + D",
        "key-positions = <22 23>;  // C + D",
    )
    text = text.replace(
        "key-positions = <27 28>;  // H + ,",
        "key-positions = <26 27>;  // H + ,",
    )
    text = text.replace(
        "key-positions = <29 30>;  // . + /",
        "key-positions = <28 29>;  // . + /",
    )

    old_base = (
        "&smart_shift_left &z_no_ctrl    &mt RALT X      &kp C           "
        "&kp D           &kp V           &kp K           &kp H           "
        "&kp COMMA       &mt RALT DOT    &slash_morph    &smart_shift_right"
    )
    new_base = (
        "&z_no_ctrl      &mt RALT X      &kp C           &kp D           "
        "&kp V           &kp K           &kp H           &kp COMMA       "
        "&mt RALT DOT    &slash_morph"
    )
    if old_base not in text:
        raise SystemExit("base bottom row pattern not found")
    text = text.replace(old_base, new_base)

    replacements = [
        (
            "&kp TILDE       &kp EXCL        &kp AT          &kp LS(N3)      "
            "&kp PIPE        &none           &to SYM         &to MOUSE       "
            "&kp RALT        &sys_reset      &trans          &trans",
            "&kp EXCL        &kp AT          &kp LS(N3)      &kp PIPE        "
            "&none           &to SYM         &to MOUSE       &kp RALT        "
            "&sys_reset      &trans",
        ),
        (
            "&trans          &kp TILDE       &kp N1          &kp N2          "
            "&kp N3          &kp PIPE        &kp STAR        &kp EQUAL       "
            "&kp COMMA       &kp DOT         &kp FSLH        &sys_reset",
            "&kp TILDE       &kp N1          &kp N2          &kp N3          "
            "&kp PIPE        &kp STAR        &kp EQUAL       &kp COMMA       "
            "&kp DOT         &kp FSLH",
        ),
        (
            "&trans          &kp TILDE       &kp N1          &kp N2          "
            "&kp N3          &kp PIPE        &kp STAR        &kp EQUAL        "
            "&kp COMMA       &kp DOT         &kp FSLH        &sys_reset",
            "&kp TILDE       &kp N1          &kp N2          &kp N3          "
            "&kp PIPE        &kp STAR        &kp EQUAL       &kp COMMA       "
            "&kp DOT         &kp FSLH",
        ),
        (
            "&trans          &sys_reset      &kp RALT        &to NUM         "
            "&to NAV         &kp PIPE        &kp INS         &kp HOME        "
            "&kp PG_DN       &kp PG_UP       &kp END         &trans",
            "&sys_reset      &kp RALT        &to NUM         &to NAV         "
            "&kp PIPE        &kp INS         &kp HOME        &kp PG_DN       "
            "&kp PG_UP       &kp END",
        ),
        (
            "&trans          &sys_reset      &kp RALT        &to FUN         "
            "&to MEDIA       &none           &bt BT_SEL 0    &bt BT_SEL 1    "
            "&bt BT_SEL 2    &bt BT_SEL 3    &bt BT_CLR      &trans",
            "&sys_reset      &kp RALT        &to FUN         &to MEDIA       "
            "&none           &bt BT_SEL 0    &bt BT_SEL 1    &bt BT_SEL 2    "
            "&bt BT_SEL 3    &bt BT_CLR",
        ),
        (
            "&trans          &sys_reset      &kp RALT        &to SYM         "
            "&to MOUSE       &none           &none           &msc SCRL_LEFT  "
            "&msc SCRL_DOWN  &msc SCRL_UP    &msc SCRL_RIGHT &trans",
            "&sys_reset      &kp RALT        &to SYM         &to MOUSE       "
            "&none           &none           &msc SCRL_LEFT  &msc SCRL_DOWN  "
            "&msc SCRL_UP    &msc SCRL_RIGHT",
        ),
        (
            "&trans          &kp F10         &kp F1          &kp F2          "
            "&kp F3          &kp PAUSE_BREAK &none           &to FUN         "
            "&to MEDIA       &kp RALT        &sys_reset      &trans",
            "&kp F10         &kp F1          &kp F2          &kp F3          "
            "&kp PAUSE_BREAK &none           &to FUN         &to MEDIA       "
            "&kp RALT        &sys_reset",
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    return text


def main() -> None:
    for name in ("temper.keymap", "temper_linux.keymap"):
        path = CONFIG / name
        out = port(path.read_text())
        path.write_text(out)
        print(f"wrote {path} ({len(out.splitlines())} lines)")
        if "&smart_shift_left &z_no_ctrl" in out:
            raise SystemExit(f"{name}: base pinky smart_shift still present")
        if "key-positions = <29 30>" in out:
            raise SystemExit(f"{name}: unremapped combo_exclaim positions")
        if "26 27 28 29 30 31 35 36 37" in out:
            raise SystemExit(f"{name}: unremapped hold-trigger list")
    print("all ok")


if __name__ == "__main__":
    main()
