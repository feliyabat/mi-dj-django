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
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
pip install -r requirements.txt
python manage.py runserver



# 🐍 Proyecto Django – Gestión Comercial

Este proyecto fue desarrollado en **Django** como parte de la evaluación INACAP.  
El objetivo es **modelar un sistema de gestión comercial** siguiendo un **Modelo Entidad-Relación (MER)** y exponerlo en el **Django Admin**.

Incluye la gestión de:  
- Clientes  
- Empleados  
- Proveedores  
- Categorías  
- Productos  
- Órdenes  
- Detalles de Órdenes  

---

## 📖 Paso a paso del proyecto

### 1. Crear proyecto y app
```bash
mkdir ProyectoFront
cd ProyectoFront
python -m venv .venv
.\.venv\Scripts\activate
pip install django
django-admin startproject proyectofront .
python manage.py startapp Pfront


2. Configurar templates y vista inicial

Se creó carpeta templates/Pfront con home.html.

En views.py se definió la función home.

Se conectó la app Pfront en urls.py.

python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser

Acceso luego en: http://127.0.0.1:8000/admin


Se implementaron los modelos en models.py:

Cliente: con cli_nombre, cli_ciudad, cli_pais, cli_mail.

Empleado: con datos de contrato, mail, dirección.

Proveedor: empresa, giro, contacto.

Categoría: nombre, descripción, foto (binaria).

Producto: con FK a Categoría y Proveedor.

Orden: con FK a Cliente y Empleado.

DetalleOrden: con FK a Orden y Producto, cantidad, precio unitario, descuento.

✔️ Se corrigieron métodos __str__.
✔️ Se añadieron validaciones con MinValueValidator.
✔️ Se añadió unique_together = (orden, producto) en DetalleOrden.


En admin.py se personalizó el Django Admin:

ClienteAdmin y EmpleadoAdmin con list_display, search_fields y list_filter.

ProductoAdmin con búsqueda por nombre, categoría y proveedor.

ProveedorAdmin con búsqueda por empresa y contacto.

OrdenAdmin con:

list_display de cliente, empleado y fecha.

list_filter por fecha y empleado.

date_hierarchy = 'ord_fecha'.

DetalleOrdenInline para cargar ítems de una orden desde la misma vista.

Cargar Categorías.

Cargar Proveedores.

Cargar Productos (relacionados con categoría y proveedor).

Cargar Clientes.

Cargar Empleados.

Cargar Órdenes.

Dentro de cada Orden → pestaña de Detalles (Inline) para agregar productos, cantidad, precio, descuento.

8. Confirmación en Git y GitHub

Proyecto versionado con Git y subido a GitHub.

Commit clave:
"Actualiza modelos y admin según MER: FK proveedor en Producto, inline de DetalleOrden, búsquedas y filtros en Admin"


