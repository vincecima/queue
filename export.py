import csv
import json
import os
import requests
import sys


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


READWISE_READER_API_TOKEN = os.environ.get("READWISE_READER_API_TOKEN")
if not READWISE_READER_API_TOKEN:
    sys.stderr.write("READWISE_READER_API_TOKEN environment variable required")
    sys.exit(1)

all_data = fetch_reader_document_list_api(READWISE_READER_API_TOKEN)
print(json.dumps(all_data))