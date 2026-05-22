import json
import sys
import os

# Updated file targeting version 5
DATA_FILE = 'data-resources-gemini-v5.json'

def validate_resources():
    # Attempt to locate file in root or a common 'data/' subdirectory
    if not os.path.exists(DATA_FILE):
        fallback = os.path.join('data', DATA_FILE)
        if os.path.exists(fallback):
            current_file = fallback
        else:
            print(f"❌ Error: Could not find {DATA_FILE} in root or 'data/' directory.")
            sys.exit(1)
    else:
        current_file = DATA_FILE

    print(f"🔍 Reading and validating: {current_file}...")
    with open(current_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Error: JSON is malformed: {e}")
            sys.exit(1)

    errors = []

    # 1. Structural Validation (Top-Level Keys)
    required_top_fields = ["metadata_version", "last_updated", "data_types", "info_types", "areas", "items"]
    for field in required_top_fields:
        if field not in data:
            errors.append(f"Top-level structure: Missing required field '{field}'.")

    if errors:
        print(f"--- ❌ Validation Failed: {len(errors)} structural errors found ---")
        for err in errors:
            print(err)
        sys.exit(1)

    # 2. Extract Master Lists
    master_studies = set(data.get('study_types', []))
    master_data = set(data.get('data_types', []))
    master_info = set(data.get('info_types', []))
    master_areas = set(data.get('areas', []))

    items = data.get('items', [])
    
    # 3. Unique IDs Check
    all_item_ids = set()
    for item in items:
        item_id = item.get('id')
        if item_id:
            if item_id in all_item_ids:
                errors.append(f"Global Registry: Duplicate item ID found: '{item_id}'.")
            all_item_ids.add(item_id)

    # Tracking sets to identify dead/unused metadata values
    used_studies = set()
    used_data = set()
    used_info = set()
    used_areas = set()

    # Schema-enforced required fields per item
    required_item_fields = ["title", "short_title", "id", "related", "description", "url", "info_type", "area", "data_type"]

    # 4. Item-Level Validation Deep Dive
    for item in items:
        title = item.get('title', 'Unknown Title')
        item_id = item.get('id', 'unknown_id')

        # Check for missing required properties
        for field in required_item_fields:
            if field not in item:
                errors.append(f"Resource '{title}' ({item_id}): Missing required property field '{field}'.")

        # Validate Info Types & ensure template won't crash on index 0
        item_info = item.get('info_type', [])
        if isinstance(item_info, list):
            if len(item_info) == 0:
                errors.append(f"Resource '{title}' ({item_id}): 'info_type' array cannot be empty (Hugo template relies on 'index .info_type 0').")
            for info in item_info:
                if info not in master_info:
                    errors.append(f"Resource '{title}' ({item_id}): Info type '{info}' is missing from the top-level master list.")
                used_info.add(info)

        # Validate Study Areas
        item_areas = item.get('area', [])
        if isinstance(item_areas, list):
            for area in item_areas:
                if area not in master_areas:
                    errors.append(f"Resource '{title}' ({item_id}): Study area '{area}' is missing from the top-level master list.")
                used_areas.add(area)

        # Validate Data Types
        item_data = item.get('data_type', [])
        if isinstance(item_data, list):
            for d in item_data:
                if d not in master_data:
                    errors.append(f"Resource '{title}' ({item_id}): Data type '{d}' is missing from the top-level master list.")
                used_data.add(d)

        # Validate Study Types (Optional field validation if it happens to be present)
        item_studies = item.get('study_type', [])
        if isinstance(item_studies, list):
            for s in item_studies:
                if s not in master_studies:
                    errors.append(f"Resource '{title}' ({item_id}): Study type '{s}' is missing from the top-level master list.")
                used_studies.add(s)

        # Relational Cross-Reference Check (Validates 'related' cross-links)
        item_related = item.get('related', [])
        if isinstance(item_related, list):
            for rel_id in item_related:
                if rel_id not in all_item_ids:
                    errors.append(f"Resource '{title}' ({item_id}): Mentions a cross-link relationship to ID '{rel_id}', but no item matching that ID exists.")

    # 5. Output Execution Summaries
    if errors:
        print(f"\n--- ❌ Validation Failed: {len(errors)} formatting or relational errors discovered ---")
        for err in errors:
            print(err)
        sys.exit(1)
    else:
        print("\n--- ✅ Validation Passed: All fields, tags, and cross-reference links match perfectly! ---")
        
        # Cleanup intelligence: Highlight master entries sitting idle
        unused_s = master_studies - used_studies
        unused_d = master_data - used_data
        unused_i = master_info - used_info
        unused_a = master_areas - used_areas
        
        if unused_s:
            print(f"⚠️  Note: Defined Study Types not active in any item: {unused_s}")
        if unused_d:
            print(f"⚠️  Note: Defined Data Types not active in any item: {unused_d}")
        if unused_i:
            print(f"⚠️  Note: Defined Info Types not active in any item: {unused_i}")
        if unused_a:
            print(f"⚠️  Note: Defined Study Areas not active in any item: {unused_a}")
        
        sys.exit(0)

if __name__ == "__main__":
    validate_resources()
    