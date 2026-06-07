@echo off
:: ============================================================================
::  Copyright (c) Falo x Force Cheng 2026/6/6. All rights reserved.
::  
::  Description: Windows launcher wrapper for the Glic Patcher Python script.
:: ============================================================================
cd /d "%~dp0"
python patch_glic.py
