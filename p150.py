import errno
 
try:
    stream = open("file", "rb")
     print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("ausente")
    else:
        print("desconocido")
 
