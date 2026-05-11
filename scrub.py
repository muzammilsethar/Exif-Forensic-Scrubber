import subprocess
import os

def purge_metadata(file_path):
    """
    Strips all metadata from the target image file using ExifTool.
    """
    try:
        # The command to remove all tags
        result = subprocess.run(["exiftool", "-all=", file_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[+] Successfully scrubbed: {file_path}")
            # Optional: Remove the backup file created by ExifTool (_original)
            if os.path.exists(f"{file_path}_original"):
                os.remove(f"{file_path}_original")
        else:
            print(f"[-] Failed to scrub: {result.stderr}")
            
    except FileNotFoundError:
        print("[-] Error: ExifTool not found. Please install it first.")

if __name__ == "__main__":
    target = input("Enter the image file path: ")
    if os.path.exists(target):
        purge_metadata(target)
    else:
        print("[-] Error: File path does not exist.")
