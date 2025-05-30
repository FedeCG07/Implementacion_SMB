from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
from smbprotocol.open import Open, CreateDisposition, CreateOptions, FileAttributes, FileInformationClass, ShareAccess
from smbprotocol.open import DirectoryAccessMask, FilePipePrinterAccessMask
from smbprotocol.open import ImpersonationLevel
import time
import os

#EASTER EGG
# CHANGE THESE VALUES
server_ip = "192.168.30.24"   # The IP address or name of the SMB server
share_name = "SMB_Test"  # The name of the shared folder
port = 445

# 1. Connect to the server
'''
puntitos = ''
for i in range(6):
    os.system('cls')
    puntitos += '.'
    print("Connectando al servidor SMB")
    print(puntitos)
    time.sleep(1)
    if i == 2:
        puntitos = ''
'''
connection = Connection(port, server_ip)
connection.connect()
print('Conexión establecida')
time.sleep(1)

# 2. Log in with a session
os.system('cls')
username = input('Ingrese nombre de usuario: ') #periquito
os.system('cls')
password = input('Ingrese contraseña: ') #periquito
session = Session(connection, username=username, password=password)
session.connect()


# 3. Connect to the shared folder
os.system('cls')
print('Conectando a la carpeta compartida ', share_name)
tree = TreeConnect(session, fr"\\{server_ip}\{share_name}")
tree.connect()
time.sleep(1)
print('Conexión establecida')
time.sleep(1)

opcion = 0
while (opcion != 4):
    os.system('cls')
    print('1- listar archivos \n2- Descargar archivo \n3- Subir archivo \n4- Salir')
    opcion = int(input('Eliga una opción: ')) #easter egg
    if opcion == 1:
        os.system('cls')
        # 4. List files
        print("Archivos en la carpeta compartida:")
        directory = Open(tree, "")
        directory.create(
            DirectoryAccessMask.FILE_LIST_DIRECTORY,   # desired_access     
            CreateOptions.FILE_DIRECTORY_FILE,        # create_options
            FileAttributes.FILE_ATTRIBUTE_DIRECTORY,     # file_attributes
            ShareAccess.FILE_SHARE_READ,               # share_access (FILE_SHARE_READ) 
            CreateDisposition.FILE_OPEN_IF,       # create_disposition   
            ImpersonationLevel.Impersonation          # impersonation_level
        )
        for info in directory.query_directory("*", FileInformationClass.FILE_NAMES_INFORMATION):
            filename_raw = info['file_name']
            filename = filename_raw.value.decode("utf-16le").rstrip('\x00')
            print("  -", filename)
        input('Presione enter para continuar.')
        directory.close()
    elif opcion == 2:
        os.system('cls')
        file_to_download = input('Qué archivo desea descargar? \n')
        os.system('cls')
        # 5. Download a file
        print(f"\nDescargando'{file_to_download}'...")
        file = Open(tree, file_to_download)
        file.create(
            ImpersonationLevel.Impersonation,                   # impersonation_level (optional but recommended)
            FilePipePrinterAccessMask.FILE_READ_DATA,                # desired_access
            FileAttributes.FILE_ATTRIBUTE_NORMAL,             # file_attributes
            ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE,        # share_access
            CreateDisposition.FILE_OPEN,                       # create_disposition
            CreateOptions.FILE_NON_DIRECTORY_FILE           # create_options (files, not directories)
        )
        file_size = file.end_of_file
        with open(file_to_download, "wb") as f:
            offset = 0
            chunk_size = 65536
            while offset < file_size:
                to_read = min(chunk_size, file_size - offset)
                data = file.read(offset, to_read)
                f.write(data)
                offset += to_read
        file.close()
        time.sleep(1)
        print('Archivo descargado exitosamente')
        input('Presione enter para continuar.')
    elif opcion == 3:
        os.system('cls')
        file_to_upload = input('Qué archivo desea subir? \n')
        os.system('cls')
        # 6. Upload a file
        print(f"\nSubiendo '{file_to_upload}'...")
        with open(file_to_upload, "rb") as f:
            file_data = f.read()
        upload_file = Open(tree, file_to_upload)
        upload_file.create(
            ImpersonationLevel.Impersonation,                         # impersonation_level
            FilePipePrinterAccessMask.FILE_WRITE_DATA,                # desired_access
            FileAttributes.FILE_ATTRIBUTE_NORMAL,                     # file_attributes
            ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE,  # share_access
            CreateDisposition.FILE_OVERWRITE_IF,                      # create_disposition
            CreateOptions.FILE_NON_DIRECTORY_FILE                     # create_options
        )
        upload_file.write(file_data, 0)
        upload_file.close()
        time.sleep(1)
        print('Archivo subido exitosamente')
        input('Presione enter para continuar.')
    elif opcion == 4:
        print("\nAdiós")
    else:
        print('Opción inválida, selccione otra por favor')
        time.sleep(1)