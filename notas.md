
# 🧾 Resumen curso de Django

python -m venv env
source env/bin/activate       # Linux/macOS
env\Scripts\activate          # Windows

pip install django


## ✅ Lección 1: Crear el proyecto y la primera app

- Comando para iniciar un proyecto:
  ```bash
  django-admin startproject customer360
  ```
- Comando para crear una app:
  ```bash
  python manage.py startapp clientes
  ```
- Registrar la app en `settings.py` → `INSTALLED_APPS`
- Ejecutar servidor:
  ```bash
  python manage.py runserver
  ```

---

## ✅ Lección 2: Configurar las URLs

- Crear `urls.py` en la app.
- Agregar las rutas de la app al archivo principal (`customer360/urls.py`) usando `include()`.
- Estructura recomendada:

  ```python
  # customer360/urls.py
  path('clientes/', include('clientes.urls')),
  ```

  ```python
  # clientes/urls.py
  app_name = 'clientes'
  urlpatterns = [
      path('', views.saludo, name='saludo'),
  ]
  ```

---

## ✅ Lección 3: Templates y vistas

- `render(request, 'clientes/saludo.html', contexto)`
- Crear carpeta `templates/clientes/` y dentro colocar archivos `.html`.
- Pasar contexto desde la vista:

  ```python
  def saludo(request):
      return render(request, 'clientes/saludo.html', {'nombre': 'Israel'})
  ```

---

## ✅ Lección 4: Modelos y base de datos

- Definir modelo en `clientes/models.py`:

  ```python
  class Cliente(models.Model):
      nombre = models.CharField(max_length=100)
      correo = models.EmailField()
  ```

- Comandos para aplicar modelo:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- Registrar modelo en `admin.py` para verlo en el panel de administración.
- Consultar datos con `Cliente.objects.all()` y mostrarlos en el template.

---

## ✅ Lección 5: Formulario con `ModelForm`

- Crear archivo `forms.py` y definir:

  ```python
  class ClienteForm(forms.ModelForm):
      class Meta:
          model = Cliente
          fields = ['nombre', 'correo']
  ```

- Vista para manejar formulario:

  ```python
  def registrar_cliente(request):
      if request.method == 'POST':
          form = ClienteForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('clientes:saludo')
      else:
          form = ClienteForm()
      return render(request, 'clientes/registrar.html', {'form': form})
  ```

- Template con el formulario:

  ```html
  <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Guardar</button>
  </form>
  ```

---

## ✅ Lección 6: Introducción formal a formularios

- Django usa clases `Form` y `ModelForm` para generar formularios HTML.
- `form.is_valid()` valida automáticamente.
- `form.cleaned_data` da acceso a los datos ya validados.
- `form.save()` guarda directamente el modelo.
- `{% csrf_token %}` protege contra ataques CSRF.