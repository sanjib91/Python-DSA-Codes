# Problem: Read CSV, process data, write new CSV
def process_sales_data(input_file, output_file):
    import csv
    
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['total_value']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            # Calculate total (quantity * price)
            row['total_value'] = float(row['quantity']) * float(row['price'])
            writer.writerow(row)

# Usage: process_sales_data('sales.csv', 'processed_sales.csv')