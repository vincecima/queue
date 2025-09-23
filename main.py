import csv
import os
import requests
import sys

COLUMNS = [
    "id",
    "url",
    "source_url",
    "title",
    "author",
    "location",
    "tags",
    "site_name",
    "published_date",
    "image_url",
    "saved_at",
]


def fetch_reader_document_list_api(token, updated_after=None, location=None):
    full_data = []
    next_page_cursor = None
    while True:
        params = {"withHtmlContent": False, "withRawSourceUrl": False}
        if next_page_cursor:
            params["pageCursor"] = next_page_cursor
        if updated_after:
            params["updatedAfter"] = updated_after
        if location:
            params["location"] = location
        response = requests.get(
            url="https://readwise.io/api/v3/list/",
            params=params,
            headers={"Authorization": f"Token {token}"},
            # verify=False,
        )
        full_data.extend(response.json()["results"])
        next_page_cursor = response.json().get("nextPageCursor")
        if not next_page_cursor:
            break
    return full_data


def convert_document_to_csv_row(document):
    return map(lambda col: document[col], COLUMNS)


READWISE_READER_API_TOKEN = os.environ.get("READWISE_READER_API_TOKEN")
if not READWISE_READER_API_TOKEN:
    sys.stderr.write("READWISE_READER_API_TOKEN environment variable required")
    sys.exit(1)

all_data = fetch_reader_document_list_api(READWISE_READER_API_TOKEN)

csv_out = csv.writer(sys.stdout)
csv_out.writerow(map(lambda col: col, COLUMNS))
csv_out.writerows(map(convert_document_to_csv_row, all_data))
