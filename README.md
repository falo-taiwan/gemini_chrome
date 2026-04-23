# Chrome Gemini / Glic Visibility Research

> Force Cheng x Falo 版權宣告 2026/4/22  
> 教學展示用：AI 人機協作、系統觀察、範例學習與遷移學習案例

## Project Overview

This repository documents a real-world teaching case about Chrome Gemini / Glic visibility behavior.

The starting point was simple but educational:

- A friend in the United States could use Chrome Gemini / Glic features.
- The same type of feature disappeared or did not show after moving into a Taiwan usage context.
- Taiwan later became supported, but not every account, profile, or device showed the feature immediately.
- This suggested that feature visibility was not controlled by one simple switch.

Force used this case to demonstrate how AI-assisted investigation can turn a confusing product behavior into a structured system-learning project.

The goal of this repo is not to provide a universal patch.  
The goal is to teach how to:

- Observe system state safely
- Separate OS-level signals from Chrome local state
- Compare Mac and Windows behavior
- Build backup and inspection tools
- Turn one troubleshooting session into reusable teaching material

## Core Idea

Chrome Gemini / Glic visibility appears to depend on a bundle of signals:

- Chrome version and feature availability
- Region and safe seed signals
- Chrome app language and profile language
- Profile-level eligibility
- Glic / AI experiment flags
- First-run / FRE state
- Account capability
- Runtime launch environment

In short:

```text
backup -> inspect -> compare -> document -> only then decide what to test next
```

## What This Repo Contains

```text
Agent_news/
├── README.md
└── gemini_chrome/
    ├── README.md
    ├── CROSS_PLATFORM_VALIDATION_SUMMARY.md
    ├── CROSS_PLATFORM_VALIDATION_SUMMARY.single-file.html
    ├── internal_team_reference.md
    ├── internal_team_reference.single-file.html
    ├── MAC_REFERENCE_PACKAGE.md
    ├── WINDOWS_REFERENCE_PACKAGE.md
    ├── tools/
    │   ├── backup_chrome_settings.command
    │   ├── restore_chrome_settings.command
    │   ├── backup_macair_glic_working_state.command
    │   ├── backup_windows_chrome_state.ps1
    │   └── inspect_windows_glic_state.ps1
    └── package_exports/
        ├── Agent_news_glic_mac_reference_*.zip
        └── Agent_news_glic_windows_reference_*.zip
```

## Recommended Reading

Start here:

- [Cross-Platform Validation Summary](gemini_chrome/CROSS_PLATFORM_VALIDATION_SUMMARY.md)
- [Internal Team Reference](gemini_chrome/internal_team_reference.md)
- [Gemini Chrome Folder README](gemini_chrome/README.md)

HTML versions are included for easier reading and teaching:

- [Cross-Platform Validation Summary HTML](gemini_chrome/CROSS_PLATFORM_VALIDATION_SUMMARY.single-file.html)
- [Internal Team Reference HTML](gemini_chrome/internal_team_reference.single-file.html)

## Reference Packages

This repo also contains minimal reference packages for platform-specific handoff.

### Mac Reference Package

See:

- [MAC_REFERENCE_PACKAGE.md](gemini_chrome/MAC_REFERENCE_PACKAGE.md)

Included tools:

- `backup_chrome_settings.command`
- `restore_chrome_settings.command`
- `backup_macair_glic_working_state.command`

### Windows / Win365 Reference Package

See:

- [WINDOWS_REFERENCE_PACKAGE.md](gemini_chrome/WINDOWS_REFERENCE_PACKAGE.md)

Included tools:

- `backup_windows_chrome_state.ps1`
- `inspect_windows_glic_state.ps1`

## Tools

### macOS

Backup current Chrome settings:

```bash
./gemini_chrome/tools/backup_chrome_settings.command
```

Restore from a local backup:

```bash
./gemini_chrome/tools/restore_chrome_settings.command
```

Capture a working live snapshot:

```bash
./gemini_chrome/tools/backup_macair_glic_working_state.command
```

### Windows / Win365

Backup Chrome state:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\gemini_chrome\tools\backup_windows_chrome_state.ps1
```

Inspect Glic / AI related state:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\gemini_chrome\tools\inspect_windows_glic_state.ps1
```

## Important Safety Notes

- Do not blindly copy one machine's Chrome profile to another machine.
- Do not edit or overwrite Chrome settings while Chrome is running.
- Always create a backup before any experiment.
- Treat OS language and region settings as environment signals, not universal instructions.
- This repo intentionally prioritizes backup, inspection, reporting, and teaching workflows.
- Aggressive environment-specific patching is not part of the default toolchain.

## Teaching Value

This repo is designed as a teaching artifact.

It can be used to explain:

- How feature visibility can be controlled by multiple layers
- How to separate global state from profile state
- How to inspect JSON-based application state safely
- How AI tools can be used collaboratively
- How to convert troubleshooting into reusable documentation
- How to perform migration learning from Mac to Windows

## License / Copyright

Force Cheng x Falo 版權宣告 2026/4/22。  
This repository is provided for educational demonstration, internal learning, and case-study purposes.

