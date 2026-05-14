import re
from collections import defaultdict # or Counter

def count_errors_by_hour(log_lines):
    # Using defaultdict is perfect here!
    hour_counts = defaultdict(int)

    for line in log_lines:
        if "ERROR" in line:
            match = re.search(r'\[(\d{2}):\d{2}:\d{2}]',line)
            hour = match.group(1)
            hour_counts[hour] += 1
    return dict(sorted(hour_counts.items()))                    

# Example usage (exactly as you had it, no need to change!)
logs = [
    "[10:15:30] INFO: Process started", 
    "[10:16:45] ERROR: Connection failed",
    "[10:30:10] INFO: Another process",
    "[11:05:22] ERROR: Timeout occurred",
    "[11:45:00] ERROR: Disk full"
]
print(count_errors_by_hour(logs))