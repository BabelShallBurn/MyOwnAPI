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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
