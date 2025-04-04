# Free Youtube Backend

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgr](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=dockersitorio contiene el **backend** del proyecto Free Youtube, que incluye la API y la base de datos, todo empaquetado en un contenedor Docker.

## Características

### Implementadas
- API para gestionar descargas de videos de YouTube.
- Base de datos PostgreSQL para almacenar información relacionada con las descargas.
- Backend desarrollado con FastAPI.

### Futuras mejoras
- Soporte para otras plataformas como Instagram Reels.
- Funcionalidades avanzadas de gestión de usuarios y permisos.

## Despliegue

### Requisitos previos
Para desplegar este backend, asegúrate de tener instalado Docker en tu sistema. Sigue las instrucciones según tu sistema operativo:

#### Windows
Descarga e instala Docker Desktop desde su sitio oficial.

#### Linux
Instala Docker siguiendo las guías oficiales para tu distribución.

### Instrucciones para ejecutar el backend localmente

1. Clona este repositorio:
   ```bash
   git clone 
   cd 
   ```

2. Construye y ejecuta el contenedor Docker:
   ```bash
   docker-compose up --build
   ```

3. Accede a la API en `http://localhost:8000`.

## FAQ

#### ¿Qué tecnologías se usan en este backend?
FastAPI para la API y PostgreSQL como base de datos, todo empaquetado en Docker.

#### ¿Es necesario configurar algo antes de usarlo?
No, el contenedor incluye todas las dependencias necesarias.

#### ¿Se puede usar este backend para otros propósitos?
Sí, pero recuerda que está diseñado específicamente para el proyecto Free Youtube.

