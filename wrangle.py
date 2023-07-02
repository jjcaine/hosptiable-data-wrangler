import csv
import sys


def extract_columns(input_file, output_file):
    desired_headers = [
        'checkin_date',
        'checkout_date',
        'booking_date',
        'code',
        'platform',
        'guest_first_name',
        'guest_last_name',
        'guest_count',
        'guests_adults',
        'guests_children',
        'guests_infants',
        'nights',
        'currency',
        'base_amount',
        'cleaning_fee',
        'subtotal_amount',
        'guest_fee',
        'total_price',
        'payout_amount',
        'host_service_fee'
    ]

    with open(input_file, 'r', newline='') as csv_input:
        reader = csv.reader(csv_input)
        headers = next(reader)  # Read the header row

        # Find the indices of desired columns
        column_indices = []
        for header in desired_headers:
            try:
                column_indices.append(headers.index(header))
            except ValueError:
                print(
                    f"Header '{header}' not found in the input file. Skipping...")
                column_indices.append(None)

        with open(output_file, 'w', newline='') as csv_output:
            writer = csv.writer(csv_output)

            # Write the header row to the output file
            writer.writerow(desired_headers)

            # Iterate over the rows in the input file and extract desired columns
            for row in reader:
                extracted_row = [
                    row[i] if i is not None else '' for i in column_indices]
                writer.writerow(extracted_row)

    print('Extraction complete.')


# Check if input and output file paths are provided as command-line arguments
if len(sys.argv) >= 3:
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    extract_columns(input_file_path, output_file_path)
else:
    print('Please provide input and output file paths as command-line arguments.')
