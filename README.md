# Plataforma de Eventos y Proveedores 

## Objetivo de la Aplicación

Desarrollar una plataforma en línea que facilite la conexión entre organizadores de eventos y proveedores de servicios. Esta plataforma proporcionará un entorno seguro y eficiente para la búsqueda, contacto y contratación de servicios para eventos. 

Los organizadores podrán encontrar proveedores que se ajusten a sus necesidades específicas, mientras que los proveedores tendrán la oportunidad de mostrar sus productos y servicios a un público objetivo, aumentando su visibilidad y generando nuevas oportunidades de negocio.

## Tecnologías Utilizadas

* **Backend:**
    * Python
    * Django
    * Django Rest Framework (DRF)
    * PostgreSQL
    * JWT (JSON Web Tokens)
* **Frontend:**
    * React
    * TailwindCSS
* **Pasarela de Pago:**
    * Redsys
* **Control de Versiones:**
    * Git
    * GitHub

## Fases del Proyecto

### Fase 1: Configuración y Base del Proyecto

* Configuración del Entorno:
    * Instalación de Python, Django, PostgreSQL, Node.js, npm.
    * Creación de la aplicación React y configuración de TailwindCSS.
    * Configuración del entorno virtual de Django.
* Control de Versiones:
    * Configuración de Git y creación del repositorio en GitHub.
    * Definición de flujos de trabajo y ramas principales.
* Diseño Inicial de la Base de Datos:
    * Modelado de entidades principales (usuarios, proveedores, productos, eventos, etc.).
    * Creación de migraciones iniciales en Django.

### Fase 2: Autenticación y Perfiles de Usuario

* **Backend:**
    * Implementación de registro y autenticación con JWT usando DRF.
    * Creación de modelos y vistas para usuarios (organizadores y proveedores).
    * Configuración de roles y permisos.
* **Frontend:**
    * Diseño y desarrollo de formularios de registro y login.
    * Manejo de tokens JWT y autenticación en el frontend.
    * Creación de páginas de perfil básicas para ambos roles.

### Fase 3: Gestión de Proveedores y Productos

* **Backend:**
    * Creación de modelos para proveedores, categorías de productos y productos.
    * Implementación de APIs para crear, editar, listar y eliminar productos.
    * Configuración de la lógica para que los proveedores solo vean sus propios productos.
* **Frontend:**
    * Desarrollo de plantillas de productos para cada categoría.
    * Creación de formularios para que los proveedores creen y editen productos.
    * Diseño de la interfaz para que los organizadores puedan ver y filtrar productos.

### Fase 4: Interacción y Búsqueda

* **Backend:**
    * Implementación de APIs para que los organizadores puedan contactar a proveedores.
    * Configuración de notificaciones automáticas para los proveedores.
    * Desarrollo de lógica de búsqueda y filtrado de proveedores.
* **Frontend:**
    * Implementación de la funcionalidad para que los organizadores contacten proveedores.
    * Diseño de la interfaz de búsqueda con filtros avanzados.
    * Visualización de notificaciones para los proveedores.

### Fase 5: Gestión de Equipos y Carpetas

* **Backend:**
    * Creación de modelos para equipos y carpetas.
    * Implementación de APIs para invitar usuarios, crear y gestionar carpetas.
* **Frontend:**
    * Desarrollo de la interfaz para invitar miembros al equipo.
    * Diseño de la funcionalidad para crear y organizar carpetas.

### Fase 6: Diseño, Pruebas y Optimización

* Diseño UI/UX:
    * Refinamiento del diseño con TailwindCSS para una experiencia de usuario óptima.
    * Asegurar la responsividad en diferentes dispositivos.
* Pruebas:
    * Pruebas unitarias y de integración tanto en backend como en frontend.
    * Pruebas de usabilidad con usuarios reales.
* Optimización:
    * Optimización de consultas a la base de datos y rendimiento general.
    * Mejora de la velocidad de carga y la eficiencia del código.

### Fase 7: Integración de Pagos y Despliegue

* Integración de Pasarela de Pago:
    * Integración con Redsys u otra pasarela de pago.
    * Implementación de la lógica de suscripción y pagos recurrentes.
    * Configuración de pruebas y manejo de errores en pagos.
* Despliegue:
    * Configuración del entorno de producción.
    * Despliegue en un servidor con dominio y SSL.
    * Implementación de CI/CD para automatizar despliegues futuros.

### Fase 8: Monitoreo y Mantenimiento Continuo

* Monitoreo:
    * Configuración de herramientas de monitoreo para detectar errores y problemas de rendimiento.
    * Análisis de registros y métricas para identificar áreas de mejora.
* Mantenimiento:
    * Corrección de errores y actualizaciones de seguridad.
    * Desarrollo de nuevas funcionalidades y mejoras basadas en el feedback de los usuarios.
