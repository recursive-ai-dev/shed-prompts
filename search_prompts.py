#!/usr/bin/env python3
"""
Prompt Search & Query CLI
Search prompts by domain, subcategory, keyword, or output artifact.
"""

import os
import json
import argparse
import sys

def search_prompts(query=None, domain=None, subcat=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(script_dir, "manifest.json")

    if not os.path.exists(manifest_path):
        print("❌ ERROR: manifest.json not found!")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    results = []
    query_lower = query.lower() if query else None

    for item in manifest:
        if domain and item.get("domain") != domain:
            continue
        if subcat and item.get("subcategory") != subcat:
            continue

        if query_lower:
            searchable_text = " ".join([
                item.get("id", ""),
                item.get("legacy_filename", ""),
                item.get("domain", ""),
                item.get("subcategory", ""),
                item.get("summary", ""),
                item.get("output_artifact", ""),
                item.get("new_path", "")
            ]).lower()

            if query_lower not in searchable_text:
                continue

        results.append(item)

    print(f"\n🔍 Found {len(results)} matching prompt(s):\n")
    print(f"{'ID':<24} | {'Domain/Subcat':<38} | {'Output Artifact':<24}")
    print("-" * 90)

    for item in results:
        dom_sub = f"{item['domain']}/{item['subcategory']}"
        print(f"{item['id']:<24} | {dom_sub:<38} | {item['output_artifact']:<24}")
        print(f"   Path:    {item['new_path']}")
        print(f"   Summary: {item['summary']}")
        print("-" * 90)

def main():
    parser = argparse.ArgumentParser(description="Search prompt repository.")
    parser.add_argument("query", nargs="?", help="Keyword search across prompt title, summary, or artifact")
    parser.add_argument("--domain", choices=["android", "software-engineering", "worldbuilding"], help="Filter by domain")
    parser.add_argument("--subcat", help="Filter by subcategory")

    args = parser.parse_args()
    search_prompts(query=args.query, domain=args.domain, subcat=args.subcat)

if __name__ == "__main__":
    main()
