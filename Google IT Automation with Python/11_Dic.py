# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong
#  to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

#La idea es invertir el diccionario, o sea en lugar de que la key sea los tipos de permisos y la llave los usuarios
#hacemos un diccionario en que la key es el tipo de user y el valor el tipo de permiso
#empezamos con un diccionario vacio user_groups y recorremos decimos para el primer dominio (local, public, private)
#recorremos los usuarios usamos el get, 
# con el metodo get llamamos al usuario, si no existe el usuario (us) me crea una lista vacia por defecto
#pero si existe, concatena otra lista con el dominio

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for dominio, users in group_dictionary.items():
		# Now go through the users in the group
		for us in users:
			user_groups[us]=user_groups.get(us, []) + [dominio]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))