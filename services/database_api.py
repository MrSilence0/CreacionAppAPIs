import requests

SUPABASE_URL = "https://url_de_tu_instancia.supabase.co"
SUPABASE_KEY = "annon_key_de_api_supabase"

def save_to_favorites(post_id, title, track_id):
    url = f"{SUPABASE_URL}/rest/v1/favorites"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    payload = {
        "post_id": post_id,   
        "title": title,
        "track_id": track_id
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.status_code in (200, 201)
