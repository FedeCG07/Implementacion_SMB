Para poder utilizar el código es necesario contar con un servidor SMB y configurar el código para que se conecte a este.

Pasos para crear un servidor SMB en Linux:
- Instalar Samba utilizando los comandos "sudo apt update" y "sudo apt install samba"
- Crear una carpeta compartida con los comandos "

Pasos para poder utilizar el código:
- Crear un python environment venv
- Ejecutar en la terminal "pip install smbprotocol"
- Cambiar "server_ip" por la del servidor correspondiente
- Cambiar "share_name" por el nombre de la carpeta compartida a utilizar
- Configurar el puerto si fuera necesario (SMB suele utilizar por default el 445)