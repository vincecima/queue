import "./app.css";
import data from "./readwise.json";
import DataTable from 'datatables.net-dt';

let table = new DataTable('#items', {
    data: data,
    columns: [
        { data: 'title', title: 'Title' },
        { data: 'location', title: 'Location' },
        { data: 'published_date', title: 'Published At', render: DataTable.render.date()},
        { data: 'saved_at', title: 'Saved At', render: DataTable.render.datetime()},
        { data: 'url', render: function (data, type, row, meta) {
            return '<a href="' + data + '">Readwise</a>';
        }},
        { data: 'source_url', render: function (data, type, row, meta) {
            return '<a href="' + data + '">Original</a>';
        }}
    ],
    paging: false
});