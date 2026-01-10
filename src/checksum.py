import hashlib
import glob
import os
import sys

RAW_DIR = "data/raw"
MANIFEST_FILE = os.path.join(RAW_DIR, "checksums.sha256")

def calculate_sha256(filepath):
    """Calculates the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def generate():
    """Generates a checksum manifest for all CSV files in raw data."""
    print(f"Generating checksums for {RAW_DIR}...")
    files = glob.glob(os.path.join(RAW_DIR, "*.csv"))
    
    with open(MANIFEST_FILE, "w") as f:
        for file_path in files:
            file_hash = calculate_sha256(file_path)
            file_name = os.path.basename(file_path)
            # Format: HASH  FILENAME (Standard format)
            f.write(f"{file_hash}  {file_name}\n")
            print(f"  Hashed: {file_name}")
    
    print(f"Manifest saved to {MANIFEST_FILE}")

def verify():
    """Verifies files against the manifest."""
    print(f"Verifying integrity from {MANIFEST_FILE}...")
    if not os.path.exists(MANIFEST_FILE):
        print("Error: Manifest file not found. Run generation first.")
        sys.exit(1)
        
    all_good = True
    with open(MANIFEST_FILE, "r") as f:
        for line in f:
            stored_hash, filename = line.strip().split("  ")
            file_path = os.path.join(RAW_DIR, filename)
            
            if not os.path.exists(file_path):
                print(f"❌ MISSING: {filename}")
                all_good = False
                continue
                
            current_hash = calculate_sha256(file_path)
            if current_hash == stored_hash:
                print(f"✅ OK:      {filename}")
            else:
                print(f"❌ CORRUPT: {filename}")
                all_good = False
                
    if all_good:
        print("\nSUCCESS: All raw files are intact.")
    else:
        print("\nFAILURE: Data integrity issues detected.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        verify()
    else:
        generate()