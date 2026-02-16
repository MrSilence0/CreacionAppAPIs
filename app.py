from flask import Flask, render_template, request, redirect
from services.social_api import get_posts, get_post
from services.database_api import save_to_favorites 

app = Flask(__name__)

@app.route("/")
def index():
    """Renderiza el feed principal con todos los posts."""
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/post/<post_id>")
def post_detail(post_id):
    """
    Renderiza el detalle de un post. 
    Busca el post en social_api.py y lo envía al template.
    """
    post = get_post(post_id)
    
    if not post:
        return "Post no encontrado", 404

    # Al usar iframes estáticos en post.html, solo necesitamos pasar el objeto 'post'.
    # El HTML se encargará de mostrar el iframe correcto según el post.id.
    return render_template("post.html", post=post)

@app.route("/favorite/<post_id>", methods=["POST"])
def favorite(post_id):
    title = request.form.get("title")
    track_id = request.form.get("track_id")

    save_to_favorites(
        post_id=int(post_id.replace("post", "")),
        title=title,
        track_id=track_id
    )
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)