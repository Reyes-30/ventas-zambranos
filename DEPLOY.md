# Despliegue en la Web

Esta app se puede desplegar gratis en servicios como:

- Streamlit Community Cloud (recomendado)
- Hugging Face Spaces (Gradio/Streamlit)
- Railway/Render/Fly.io (requiere Procfile)

## Opción A: Streamlit Community Cloud (recomendado)

1. Sube el proyecto a GitHub (main con app.py y requirements.txt)
2. Ve a https://share.streamlit.io/ (sign in con GitHub)
3. "New app" y selecciona tu repo + rama `main` + archivo `app.py`
4. Deploy. Obtendrás una URL pública.

Notas:
- Asegúrate de que `requirements.txt` incluya todas las dependencias
- Si necesitas Chrome/Kaleido, ya está listado `kaleido` en requirements
- Usa `data/` para persistencia simple (no garantizada en reinicios)

## Opción B: Hugging Face Spaces

1. Crea un Space nuevo (tipo: Streamlit)
2. Conecta tu repo o sube los archivos (app.py, requirements.txt)
3. Añade un `README.md` y (opcional) `runtime.txt` para Python
4. El Space generará una URL pública.

## Opción C: Railway/Render/Fly.io

- Usa el `Procfile` incluido:

```
web: streamlit run app.py --server.headless true --server.port $PORT --server.address 0.0.0.0
```

- Define variable de entorno PORT si hace falta.

## Mantener secretos y archivos

- No subas datos sensibles al repo.
- Usa variables de entorno o servicios externos para datos privados.
- Los archivos generados en runtime pueden no persistir.
