import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define synthetic enterprise constants
DOMAINS = ['CORP', 'DEV', 'GUEST', 'OLD_DOMAIN.LEGACY.COM']
EVENT_TYPES = [
    'A member was added to a security-enabled local group',
    'A member was added to a security-enabled global group',
    'A member was removed from a security-enabled local group',
    'User account locked out',
    'Logon failure'
]
GROUPS = [
    'Administrators', 
    'Remote Desktop Users', 
    'Domain Admins', 
    'Marketing_Share', 
    'IT_Helpdesk',
    'All_Staff_Read_Only'
]

def generate_account_id(domain):
    """Generates standard, service, or temporary accounts."""
    account_type = random.choices(['standard', 'service', 'temp'], weights=[80, 15, 5])[0]
    
    if account_type == 'service':
        # Mimics specific service account naming conventions (e.g., for exclusion logic)
        return f"{domain}\\SVC_{fake.user_name()}"
    elif account_type == 'temp':
        return f"{domain}\\TEMP_{fake.user_name()}"
    else:
        # Standard user account
        return f"{domain}\\{fake.user_name()}"

def generate_synthetic_logs(num_records=500):
    data = []
    
    for _ in range(num_records):
        domain = random.choice(DOMAINS)
        
        row = {
            'Hostname': f"{fake.hostname().upper()}",
            'Event_Type': random.choice(EVENT_TYPES),
            'Target_Group': random.choice(GROUPS),
            'Account_ID': generate_account_id(domain),
            'Timestamp': fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    
    # Inject intentional duplicates to test your duplicate removal logic
    duplicate_rows = df.sample(frac=0.05) # 5% of data duplicated
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    # Shuffle the dataset so duplicates aren't directly next to each other
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    print("Generating synthetic endpoint security logs...")
    
    # Generate 1000 rows of data
    log_data = generate_synthetic_logs(1000)
    
    # Save to CSV
    output_filename = "synthetic_audit_logs.csv"
    log_data.to_csv(output_filename, index=False)
    
    print(f"Success! {len(log_data)} records saved to {output_filename}")
    print("\nData Preview:")
    print(log_data.head())