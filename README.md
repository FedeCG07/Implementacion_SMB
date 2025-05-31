Para poder utilizar el código es necesario contar con un servidor SMB y configurar el código para que se conecte a este.

Pasos para crear un servidor SMB en windows:
- Abrir el panel de control. Ir a "Redes e Internet", luego a "Centro de redes y recursos compartidos" y por último entrar a "Cambiar configuración de uso compartido avanzado" (a la izquierda)
- Encender "Detección de redes" y "Uso compartido de archivos e impresoras" y guardar los cambios
- Crear o elegir una carpeta para compartir
- Hacer click derecho en la carpeta, elegir "Propiedades", entrar en la pestaña "Compartir" y tocar el botón "Compartir"
- Escribir "Todos" y hacer click en agregar, luego cambiar el nivel de permiso a Lectura y escritura. Hacer click en "Comparit" y en "Listo", y cerrar los archivos
- Es necesario saber el nombre de usuario y la contraseña de la cuenta de la computadora, ya que estos se usarán para iniciar sesión durante la ejecucción del programa. En caso de no tener contraseña, SMB puede rechazar la conexión por lo que se recomienda agregarla
- Finalmente, abrir una terminal cmd y utilizar "ipconfig". Luego buscar una linea similar a "IPv4 Address. . . . . . . . . . . : 192.168.1.123" y copiar la dirección IP que sale para utilizarla en el código

Pasos para crear un servidor SMB en Linux:
- Abrir la terminal cmd
- Instalar Samba utilizando los comandos "sudo apt update" y "sudo apt install samba"
- Crear una carpeta compartida con los comandos "sudo mkdir -p /srv/samba/shared" y "sudo chmod 777 /srv/samba/shared" 
- Crear un ususario de Samba con el comando "sudo adduser smbuser". Al hacer esto va a pedir una contraseña, que luego se va a cambiar, y muchos otros datos que se pueden dejar en blanco solo tocando enter
- Configurar la contraseña del usuario con "sudo smbpasswd -a smbuser". Esta contraseña y usuario son los que después se tienen que utilizar para iniciar sesión durante la ejecucción del programa
- Configurar Samba para compartir la carpeta. Para esto vamos a utilizar "sudo nano /etc/samba/smb.conf", lo que nos va a abrir un archivo de texto en el cual hay que ir al fondo y agregar las siguientes lineas:
[SMB_Test]
   path = /srv/samba/shared
   browseable = yes
   read only = no
   guest ok = no
   valid users = smbuser
- Reiniciar Samba con "sudo systemctl restart smbd" para aplicar los cambios 
- Permitir el paso por el firewall, si es que lo hay, con "sudo ufw allow 'Samba'"
- Obtener dirección IP con "hostname -I". Esta dirección es la que se utiliza para conectarse desde el código

Pasos para poder utilizar el código:
- Crear un python environment venv
- Ejecutar en la terminal "pip install smbprotocol"
- Cambiar "server_ip" por la dirección ip del servidor correspondiente
- Cambiar "share_name" por el nombre de la carpeta compartida a utilizar (si se sigue todos los pasos en la configuración del servidor exactamente, no es necesario cambiarlo)
- Configurar el puerto si fuera necesario (SMB suele utilizar por default el 445)