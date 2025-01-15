# Proyecto: Módulo "manage" para Odoo ERP

Este repositorio contiene el código fuente del módulo **"manage"**, desarrollado para Odoo ERP. Este módulo está diseñado para facilitar la gestión de proyectos mediante la metodología Scrum, permitiendo organizar tareas, sprints y equipos de forma eficiente.

## Características principales
- **Integración con Scrum**: Soporte para la organización de proyectos en sprints, con tareas asignadas y seguimiento del progreso.
- **Conexión con Trello**: Importación de tareas desde tableros de Trello para integrarlas en la gestión centralizada de Odoo.
- **Desarrollo modular**: Construido siguiendo las buenas prácticas de desarrollo de módulos en Odoo.

## Requisitos
- **Odoo ERP**: Versión 16 o superior.
- **Docker**: Para crear un entorno de desarrollo estable.
- **Python**: Versión 3.8 o superior.
- **PyCharm**: Recomendado para escribir y depurar el código.

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/AngelChv/managechicote.git
   ```
2. Configura tu entorno de desarrollo usando Docker:
   - Asegúrate de tener un archivo `docker-compose.yml` configurado correctamente.
   - Levanta los servicios necesarios:
     ```bash
     docker-compose up -d
     ```
3. Copia el código del módulo en la carpeta `addons` de tu entorno de Odoo.
4. Reinicia el servidor de Odoo y activa el módulo en la sección de aplicaciones.

## Uso
1. Accede al módulo "manage" desde el panel principal de Odoo.
2. Configura la conexión con Trello proporcionando tu API Key, Token y el ID del tablero.
3. Crea y organiza proyectos, sprints y tareas directamente desde el módulo.
