# `` Complete los espacios en blanco en este código para devolver el tamaño en kilobytes (un kilobyte son 1024 bytes) 
#  hasta con 2 decimales.



def file_size(file_info):
	a, b, c= file_info
	return("{:.2f}".format(c / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21