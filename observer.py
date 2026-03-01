import sys
import requests
import json
import re

def stream_to_horizon():
    print("[OBSERVER] Monitoring Kissat-Sovereign output...")
    # Pattern to catch conflict counts or variable assignments from stdout
    pattern = re.compile(r"conflicts:\s+(\d+)") 
    
    for line in sys.stdin:
        # Print the output so you can still see it in the terminal
        sys.stdout.write(line)
        
        # Look for progress markers
        match = pattern.search(line)
        if match:
            conflict_count = int(match.group(1))
            
            # Generate a 1024-bit state based on the current conflict hash
            # This visualizes the "Search Space" shifting in real-time
            bits = [(1 if (i ^ conflict_count) % 7 == 0 else 0) for i in range(1024)]
            
            try:
                requests.post("http://localhost:8000/update", json={"bits": bits})
            except:
                pass

if __name__ == "__main__":
    stream_to_horizon()
