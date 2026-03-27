import json
import sys
import os

# Path to your data file relative to the root
DATA_FILE = 'data/data-resources-gemini-v2.json'

def validate_resources():
    if not os.path.exists(DATA_FILE):
        print(f"❌ Error: Could not find {DATA_FILE}")
        sys.exit(1)

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Error: JSON is malformed: {e}")
            sys.exit(1)

    # 1. Prepare master lists (sets for faster lookup)
    master_studies = set(data.get('study_types', []))
    master_data = set(data.get('data_types', []))
    
    errors = []
    
    # 2. Track usage (optional but helpful to find unused types)
    used_studies = set()
    used_data = set()

    # 3. Iterate through resources
    items = data.get('items', [])
    for item in items:
        title = item.get('title', 'Unknown Title')
        
        # Check Study Types
        item_studies = item.get('study_type', [])
        for s in item_studies:
            if s not in master_studies:
                errors.append(f"Resource '{title}': Study type '{s}' is not in the master list.")
            used_studies.add(s)
            
        # Check Data Types
        item_data = item.get('data_type', [])
        for d in item_data:
            if d not in master_data:
                errors.append(f"Resource '{title}': Data type '{d}' is not in the master list.")
            used_data.add(d)

    # 4. Report Results
    if errors:
        print(f"--- ❌ Validation Failed: {len(errors)} errors found ---")
        for err in errors:
            print(err)
        sys.exit(1) # Exit with error code for CI/CD
    else:
        print("--- ✅ Validation Passed: All tags match master lists ---")
        
        # Bonus: Check for unused types in your master list
        unused_s = master_studies - used_studies
        unused_d = master_data - used_data
        
        if unused_s:
            print(f"⚠️  Note: These Study Types are defined but not used by any item: {unused_s}")
        if unused_d:
            print(f"⚠️  Note: These Data Types are defined but not used by any item: {unused_d}")
        
        sys.exit(0)

if __name__ == "__main__":
    validate_resources()
    