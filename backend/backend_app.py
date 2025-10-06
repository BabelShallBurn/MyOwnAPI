from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    sort_by = request.args.get('sort', 'id')
    sort_direction = request.args.get('direction', 'asc')

    if sort_by not in ['id', 'title', 'content'] and sort_by != '':
        return jsonify({"error": "Invalid sort parameter"}), 400
    if sort_direction not in ['asc', 'desc'] and sort_direction != '':
        return jsonify({"error": "Invalid direction parameter"}), 400
    if sort_by in ['id', 'title', 'content']:
        reverse = (sort_direction == 'desc')
        sorted_posts = sorted(POSTS, key=lambda x: x[sort_by], reverse=reverse)
        return jsonify(sorted_posts)

    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    new_post = request.get_json()

    if not new_post:
        return jsonify({"error": "Post must contain title and content"}), 400        
    if 'title' not in new_post:
        return jsonify({"error": "Post must contain title"}), 400        
    if 'content' not in new_post:
        return jsonify({"error": "Post must contain content"}), 400

    max_id = 0
    for post in POSTS:
        if post['id'] > max_id:
            max_id = post['id']

    new_post['id'] = max_id + 1
    POSTS.append(new_post)
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global POSTS
    if not any(post['id'] == post_id for post in POSTS):
        return jsonify({"error": "Post not found"}), 404
    POSTS = [post for post in POSTS if post['id'] != post_id]

    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    updated_post = request.get_json()
    if not updated_post:
        return jsonify({"error": "Post must contain title and content"}), 400        
    if 'title' not in updated_post:
        return jsonify({"error": "Post must contain title"}), 400        
    if 'content' not in updated_post:
        return jsonify({"error": "Post must contain content"}), 400

    for post in POSTS:
        if post['id'] == post_id:
            post['title'] = updated_post['title']
            post['content'] = updated_post['content']
            return jsonify(post), 200

    return jsonify({"error": "Post not found"}), 404

@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()

    matched_posts = [
        post for post in POSTS
        if (
            (title_query in post['title'].lower() if title_query else True)
            and (content_query in post['content'].lower() if content_query else True)
        )
    ]
    return jsonify(matched_posts), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
