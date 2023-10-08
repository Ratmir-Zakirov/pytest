# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "number"
        },
        "title": {
            "type": "string",
            "enum": ["Post 1", "Post 2", "Post 3"]
        }
    },
    "requiared": ["id"]
}