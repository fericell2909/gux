# gux
prueba Gux


#### Crear y Activar entorno virtual Linux
python3 -m venv env source env/bin/activate

#### Crear y Activar entorno virtual windows
python -m venv env env\Scripts\activate.bat

#### Instalación de requerimientos
pip install -r requirements.txt

#### un test
./manage.py test app

run
./manage.py runserver

como es una prueba no se requiere hacer migraciones la base de datos esta adjunta. http://localhost:8000/api/

#### Filtros 

http://localhost:8000/api/testings/?numero_rol__contains=&numero_rol=&nombre_paciente__contains=&nombre_paciente=&fecha_alta__gte=&fecha_alta__lte=&codigo_prevision__contains=&codigo_prevision=

#### Admin 

http://localhost:8000/admin/problem_1/testings/