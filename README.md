# CreacionAppAPIs
Aplicación web desarrollada con APIs de streaming (spotify), redes sociales (simulación de Meta Graphics) y bases de datos (superbase). La aplicación simula un blog donde se comparten post de instagram. El usuario puede contribuir dando me gusta, la publicación y la canción se almacenarán en una base de datos en Superbase.


##Estructura del proyecto
social_flask_app_ver2/
├── .vscode/                # Configuraciones locales del editor
├── services/               # Lógica de APIs y servicios
│   ├── __pycache__/        # Archivos temporales de Python (ignorados por git)
│   ├── database_api.py     # Integración con Supabase
│   ├── social_api.py       # Simulación de datos de Instagram
│   └── streaming_api.py    # Integración con Spotify (Spotipy)
├── static/                 # Archivos estáticos
│   ├── Actividad 6_Pantallas/
│   ├── css/
│   │   └── styles.css      # Estilos globales y diseño responsivo
│   └── img/                # Imágenes de los posts (img1.jpg, etc.)
├── templates/              # Plantillas HTML (Jinja2)
│   ├── base.html           # Estructura principal y header
│   ├── index.html          # Feed principal de publicaciones
│   └── post.html           # Detalle del post y reproductores de música
├── .cache/                 # Caché de autenticación de Spotify
├── .gitignore              # Archivos excluidos de la subida a GitHub
├── app.py                  # Archivo principal de Flask (rutas)
├── README.md               # Documentación del proyecto
└── requirements.txt        # Librerías necesarias (flask, requests, spotipy)
