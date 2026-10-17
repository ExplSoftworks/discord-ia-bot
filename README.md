# discord-ia-bot

Bot de Discord con IA (Python + OpenAI).

Este repositorio contiene un bot básico en Python que responde a comandos y menciones usando la API de OpenAI.

Contenido principal:
- main.py: código del bot
- requirements.txt: dependencias
- .env-example: plantilla de variables de entorno

Instalación y uso

1) Clona el repositorio

   git clone https://github.com/ExplSoftworks/discord-ia-bot.git
   cd discord-ia-bot

2) Crea y activa un entorno virtual

   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate

3) Instala dependencias

   pip install -r requirements.txt

4) Crea un archivo .env basado en .env-example y añade tus claves

   DISCORD_TOKEN=...   # token del bot de Discord
   OPENAI_API_KEY=...  # clave de OpenAI (u otro proveedor compatible)
   OPENAI_MODEL=gpt-3.5-turbo

5) Ejecuta el bot

   python main.py

Comandos y comportamiento

- !ask <pregunta>: Envía la pregunta al modelo y responde en el canal.
- Menciona al bot (@Bot) con un mensaje y responderá usando la IA.

Notas de seguridad y operación

- No subas tu .env ni tokens a repositorios públicos.
- Controla el uso de la API (costes).
- Para entornos de producción considera:
  - Manejo de errores y reintentos (rate limit/backoff)
  - Guardar logs y métricas
  - Limitar la longitud de entrada y salida
  - Añadir moderación de contenido

Mejoras sugeridas

- Memoria conversacional por usuario o canal
- Comandos avanzados (resumen, traducción)
- Dockerfile para despliegue
- Versión en Node.js con discord.js

Si quieres, puedo añadir un Dockerfile y configurar acciones de GitHub para deploy.
