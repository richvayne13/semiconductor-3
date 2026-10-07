import os
import shutil

def main():
    src = os.path.join(r"C:\Work\반도체3\result\261007_v1.0", "index.html")
    dest = os.path.join(r"C:\Work\반도체3", "index.html")
    
    if not os.path.exists(src):
        print(f"[ERROR] Source file not found: {src}")
        return 1
        
    shutil.copyfile(src, dest)
    print(f"[SUCCESS] Copied: {src} -> {dest}")
    return 0

if __name__ == "__main__":
    exit(main())
