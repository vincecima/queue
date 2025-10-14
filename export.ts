declare module "bun" {
  interface Env {
    READWISE_READER_API_TOKEN: string;
  }
}

type Document = {
    id: string,
    url: string,
    title: string,
    author: string,
    source: string,
    category: string,
    location: string,
    tags: {},
    site_name: string,
    word_count: number | null,
    reading_time: number | null,
    created_at: string,
    updated_at: string,
    published_date: number,
    summary: string,
    image_url: string,
    content: string | null,
    source_url: string,
    notes: string,
    parent_id: string | null,
    reading_progress: number,
    first_opened_at: string | null,
    last_opened_at: string | null,
    saved_at: string | null,
    last_moved_at: null
}

const fetchDocumentListApi = async (updatedAfter: string | null=null, location: string | null=null) => {
    let fullData: Array<Document> = [];
    let nextPageCursor: string | null = null;

    while (true) {
      const queryParams = new URLSearchParams();
      if (nextPageCursor) {
        queryParams.append('pageCursor', nextPageCursor);
      }
      if (updatedAfter) {
        queryParams.append('updatedAfter', updatedAfter);
      }
      if (location) {
        queryParams.append('location', location);
      }
      const response = await fetch('https://readwise.io/api/v3/list/?' + queryParams.toString(), {
        method: 'GET',
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      const responseJson = await response.json();
      fullData.push(...responseJson['results']);
      nextPageCursor = responseJson['nextPageCursor'];
      if (!nextPageCursor) {
        break;
      }
    }
    return fullData;
};

const token = process.env.READWISE_READER_API_TOKEN;
if(!token) {
    console.log("READWISE_READER_API_TOKEN environment variable required");
    process.exit(1);
}

// Get all of a user's documents from all time
const allData = await fetchDocumentListApi();
console.log(JSON.stringify(allData));