# Problem: Parse a log file and count ERROR occurrences per hour
def count_errors_by_hour(log_lines):
    from collections import defaultdict
    import re
    
    hour_count = defaultdict(int)

    for line in log_lines:
        if "ERROR" in line:
            match = re.search(r'\[(\d{2}):\d{2}:\d{2}]',line) 
            hour = match.group(1)
            hour_count[hour] += 1

    return dict(sorted(hour_count.items()))                                    

# Example input
logs = [
    "[10:15:30] INFO: Process started",
    "[10:16:45] ERROR: Connection failed",
    "[11:05:22] ERROR: Timeout occurred"
]
print(count_errors_by_hour(logs))  # {'10': 1, '11': 1}