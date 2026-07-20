#!/usr/bin/env python3
"""
Prompt Architecture Validation Script
Verifies structural integrity, required XML tags, file presence, and manifest sync.
"""

import os
import json
import re
import sys

def validate():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    manifest_path = "manifest.json"
    if not os.path.exists(manifest_path):
        print("❌ ERROR: manifest.json not found!")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    print(f"🔍 Validating {len(manifest)} prompts in manifest.json...\n")

    errors = 0
    warnings = 0

    for item in manifest:
        path = item.get("new_path")
        prompt_id = item.get("id")

        if not os.path.exists(path):
            print(f"❌ [{prompt_id}] File missing: {path}")
            errors += 1
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check required tags
        if "<system_instructions>" not in content or "</system_instructions>" not in content:
            print(f"⚠️ [{prompt_id}] Missing <system_instructions> tag in {path}")
            warnings += 1

        if "<output_format>" not in content and "<required_structure>" not in content:
            print(f"⚠️ [{prompt_id}] Missing <output_format> or <required_structure> tag in {path}")
            warnings += 1

        # Verify non-empty
        if len(content.strip()) == 0:
            print(f"❌ [{prompt_id}] Empty file: {path}")
            errors += 1

    print("-" * 60)
    if errors == 0:
        print(f"✅ PASSED: All {len(manifest)} prompt files exist and are valid.")
        if warnings > 0:
            print(f"ℹ️  Notice: {warnings} structural warning(s) found.")
    else:
        print(f"❌ FAILED: {errors} error(s) and {warnings} warning(s) found.")
        sys.exit(1)

if __name__ == "__main__":
    validate()
