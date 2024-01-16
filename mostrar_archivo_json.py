import csv
# Abrir el archivo e indicar acceso (r en este caso por read)
# Definir una variable para contener toda la información importada
with open('CursoAutomationPython/data.csv', 'r') as mi_archivo:
    lector = csv.reader(mi_archivo)
    next(lector)  # omitimos la primera linea que tiene el header

    for renglon in lector:
        var_id, var_first_name, var_last_name, var_email, var_gender, var_fav_color = renglon
        print(f'usuario: {var_first_name} {var_last_name}')
