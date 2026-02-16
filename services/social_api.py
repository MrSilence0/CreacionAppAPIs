#Simulación de una API de red social con datos estáticos para alimentar la aplicación Flask ya que no se tiene acceso a una API real de Instagram. Esta API devuelve una lista de posts con información relevante como título, cuerpo, URL de la imagen, enlace al post original y el ID de la pista de Spotify asociada.

import requests

PROFILE_IMAGE = "/static/img/profile.jpg"

def get_posts():
    return [
        {
            "id": "post1",
            "title": "Dissolve-Joji",
            "body": "Bienvenido a mi nuevo proyecto de integración de Spotify con Flask. Aquí compartiré mis canciones favoritas y cómo las integro en esta aplicación.",
            "media_url": "/static/img/img1.jpg",
            "permalink": "https://www.instagram.com/p/DErLUZouCTl/",
            "track_id": "2auDby4pkRmpD6EmHKWlhG",
            "profile_image": PROFILE_IMAGE
        },
        {
            "id": "post2",
            "title": "Audio- Sia ft. Diplo & Labrinth",
            "body": "Poco a poco voy agregando más canciones a mi playlist. Esta es una de mis favoritas para animar el día.",
            "media_url": "/static/img/img2.jpg",
            "permalink": "https://www.instagram.com/p/DK6aYDys2VS/",
            "track_id": "100eDEmpWV5YGVCqHI0leU",
            "profile_image": PROFILE_IMAGE
        },
        {
            "id": "post3",
            "title": "Amor de Cine- Humbre",
            "body": "𝑄𝑢𝑒 𝑛𝑢𝑒𝑠𝑡𝑟𝑜 𝑣í𝑛𝑐𝑢𝑙𝑜 𝑡𝑟𝑎𝑠𝑐𝑖𝑒𝑛𝑑𝑎 ℎ𝑎𝑠𝑡𝑎 𝑓𝑜𝑟𝑗𝑎𝑟 𝑢𝑛𝑎 𝑒𝑛𝑡𝑖𝑑𝑎𝑑 𝑛𝑢𝑒𝑣𝑎, 𝑢𝑛𝑎 𝑓𝑢𝑒𝑟𝑧𝑎 𝑞𝑢𝑒 𝑑𝑒𝑠𝑏𝑜𝑟𝑑𝑒 𝑦 𝑎𝑙𝑐𝑎𝑛𝑐𝑒 𝑎 𝑞𝑢𝑖𝑒𝑛𝑒𝑠 𝑛𝑜𝑠 𝑟𝑜𝑑𝑒𝑎𝑛. 𝑆𝑒𝑎𝑚𝑜𝑠 𝑢𝑛 𝑠𝑜𝑙𝑜 𝑝𝑢𝑙𝑠𝑜, 𝑢𝑛𝑎 𝑠í𝑛𝑡𝑒𝑠𝑖𝑠 𝑞𝑢𝑒 𝑠𝑢𝑝𝑒𝑟𝑒 𝑙𝑎 𝑠𝑢𝑚𝑎 𝑑𝑒 𝑛𝑢𝑒𝑠𝑡𝑟𝑎𝑠 𝑝𝑎𝑟𝑡𝑒𝑠. 𝐻𝑎𝑔𝑎𝑚𝑜𝑠, 𝑑𝑒 𝑛𝑢𝑒𝑠𝑡𝑟𝑎 𝑒𝑥𝑖𝑠𝑡𝑒𝑛𝑐𝑖𝑎, 𝑢𝑛𝑎 𝑜𝑏𝑟𝑎 𝑠𝑢𝑝𝑒𝑟𝑖𝑜𝑟.",
            "media_url": "/static/img/img3.jpg",
            "permalink": "https://www.instagram.com/p/DUxEP2eDe7o/",
            "track_id": "0v9UztY5A12cJUsWD7PZzS",
            "profile_image": PROFILE_IMAGE
        },
        {
            "id": "post4",
            "title": "One Dance- Drake ft. Kyla & Wizkid",
            "body": "Explorando nuevas vibras.",
            "media_url": "/static/img/img4.jpg",
            "permalink": "https://www.instagram.com/p/DT4YScqDc5j/",
            "track_id": "1zi7xx7UVEFkmKfv06H8x0",
            "profile_image": PROFILE_IMAGE
        },
        {
            "id": "post5",
            "title": "Romantika- Brutalismus 3000",
            "body": "¿Quién dijo que el techno no puede ser romántico?",
            "media_url": "/static/img/img5.jpg",
            "permalink": "https://www.instagram.com/p/DBiIi13uzOT/",
            "track_id": "4nOOoo9OJbgnTBNHe5b6nD",
            "profile_image": PROFILE_IMAGE
        },
        {
            "id": "post6",
            "title": "The Color Violet- Tory Lanez",
            "body": "¿Qué es el amor? A veces es tan simple como un color.",
            "media_url": "/static/img/img6.jpg",
            "permalink": "https://www.instagram.com/p/DUhj_WfDZUN/",
            "track_id": "3azJifCSqg9fRij2yKIbWz",
            "profile_image": PROFILE_IMAGE
        }
    ]


def get_post(post_id):
    """Busca un post por su ID comparándolo como string."""
    posts = get_posts()
    for post in posts:
        if str(post['id']) == str(post_id):
            return post
    return None