import os
import pyreadstat
import pandas as pd

def search_all_files(base_dir, varname):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.sav') or file.endswith('.csv'):
                filepath = os.path.join(root, file)
                try:
                    if file.endswith('.sav'):
                        df, meta = pyreadstat.read_sav(filepath, metadataonly=True)
                        columns = [col.lower() for col in meta.column_names]
                    else:
                        df = pd.read_csv(filepath, nrows=0)  # just headers
                        columns = [col.lower() for col in df.columns]
                    
                    if varname.lower() in columns:
                        print(f"✓ Found in: {filepath}")
                    else:
                        print(f"✗ Not in: {file}")
                except Exception as e:
                    print(f"! Could not read {file}: {e}")