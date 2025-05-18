# Free Youtube Backend

Contiene el **backend** del proyecto Free Youtube, que incluye la API y la base de datos, todo empaquetado en un contenedor Docker.

## Cómo ejecutar cualquier archivo singular

Para ejecutar cualquier archivo Python dentro del proyecto, utiliza el siguiente comando desde la raíz del proyecto:

```bash
python -m app.PACKAGE.FILE
```

## Nota sobre VIDEO_STORAGE

El proyecto utiliza una constante llamada `VIDEO_STORAGE` en `app/config.py` para definir la ruta donde se almacenan los videos descargados. **Ten cuidado con esta ruta**, ya que actualmente está configurada como:

```python
VIDEO_STORAGE = Path("~/FreeYoutube/app/storage")
```

Esto significa que los videos se almacenarán en una carpeta específica dentro del proyecto. Si decides cambiar esta ruta, asegúrate de que la nueva ubicación exista y tenga los permisos adecuados para escritura.

