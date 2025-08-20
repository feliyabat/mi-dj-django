# 🚀 Mi DJ - Proyecto Django

Este es un proyecto básico en Django.
El objetivo es aprender a estructurar un proyecto, trabajar con templates, estáticos (CSS, JS, imágenes) y practicar el flujo de trabajo con GitHub.

---

 Características
- Proyecto Django con configuración inicial.
- Plantilla base (`base.html`) con header, footer y navegación.
- Archivos estáticos organizados en `static/`:
  - `css/styles.css` → Estilos personalizados.
  - `js/main.js` → Script para cambiar entre modo claro/oscuro.
  - `img/favicon.ico` → Ícono del sitio.
- Página de inicio con mensaje de bienvenida.
- Página de contacto con formulario básico.

---

Requisitos
Antes de ejecutar el proyecto asegúrate de tener instalado:
- [Python 3.10+](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/)

Cómo ejecutar el proyecto

Clona este repositorio:
git clone https://github.com/feliyabat/mi-dj-django.git
cd mi-dj-django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
