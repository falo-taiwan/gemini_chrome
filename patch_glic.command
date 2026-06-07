#!/bin/bash
# ==============================================================================
#  Copyright (c) Falo x Force Cheng 2026/6/6. All rights reserved.
#  
#  Description: macOS launcher wrapper for the Glic Patcher Python script.
# ==============================================================================
cd "$(dirname "$0")"
python3 patch_glic.py
