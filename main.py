import pandas as pd
from books import get_page
from logs import logging

output_path = "gutenberg_books.csv"


def json_to_csv(json, output_file_path):
    try:
        df = pd.read_json(json)

        # Save the DataFrame to a CSV file
        df.to_csv(output_file_path, mode="a", index=False)

        logging.Info(f'Data successfully saved to {output_file_path}')
    except Exception as e:
        logging.Error(f'An error occurred: {e}')


def get_all_books():
    page_one = get_page(1),
    pages_num = page_one["count"]

    for page in range(2, pages_num):
        json_to_csv(get_page(page), output_path)


get_all_books()
