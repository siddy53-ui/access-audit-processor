import pandas as pd
from datetime import datetime

def process_audit_logs(input_csv_path, output_excel_path, analyst_name="Sourav"):
    # 1. Read the synthetic data
    df = pd.read_csv(input_csv_path)

    # 2. String Manipulation: Split Account_ID into Domain and User
    account_split = df['Account_ID'].str.split('\\', n=1, expand=True)
    df['Domain'] = account_split[0]
    df['User'] = account_split[1]
    df = df.drop(columns=['Account_ID'])

    # 3. Vectorized Exclusions
    # Mimics filtering out legacy domains and service/temp accounts
    exclusion_mask = (df['Domain'] == 'OLD_DOMAIN.LEGACY.COM') | \
                     (df['User'].str.startswith('SVC_')) | \
                     (df['User'].str.startswith('TEMP_'))
    
    exclusions_df = df[exclusion_mask].copy()
    
    # 4. Filter for Valid (BAU) data
    valid_df = df[~exclusion_mask].copy()

    # 5. Deduplication
    duplicates_mask = valid_df.duplicated(
        subset=['Hostname', 'Event_Type', 'Target_Group', 'Domain', 'User'], 
        keep='first'
    )
    duplicates_df = valid_df[duplicates_mask].copy()
    
    # Retain only unique rows for the final validated dataset
    final_valid_df = valid_df[~duplicates_mask].copy()

    # Add tracking metadata for the auditor
    final_valid_df['Processed_At'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_valid_df['Added_By'] = analyst_name
    
    # 6. Multi-Sheet Excel Generation
    with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
        final_valid_df.to_excel(writer, sheet_name='Validated_Access', index=False)
        exclusions_df.to_excel(writer, sheet_name='Exclusions', index=False)
        duplicates_df.to_excel(writer, sheet_name='Duplicates', index=False)
        
    return len(df), len(final_valid_df), len(exclusions_df), len(duplicates_df)

if __name__ == "__main__":
    print("Processing audit logs...")
    in_file = "synthetic_audit_logs.csv"
    out_file = "processed_audit_report.xlsx"
    
    total, valid, excluded, duplicates = process_audit_logs(in_file, out_file)
    
    print(f"\nProcessing Complete! Saved to {out_file}")
    print(f"Total Rows Processed: {total}")
    print(f"Valid Records: {valid}")
    print(f"Excluded Records: {excluded}")
    print(f"Duplicates Removed: {duplicates}")