#!/bin/bash

echo "Descargando paquete de oracle"
wget https://download.oracle.com/otn-pub/otn_software/db-express/oracle-database-xe-18c-1.0-1.x86_64.rpm -P ./download/
echo "Clonando el repositorio"
git clone https://github.com/oracle/docker-images.git
echo "Copiando el binario a la carpeta de creación de imagenes"
cp ./download/oracle-database-xe-18c-1.0-1.x86_64.rpm ./docker-images/OracleDatabase/SingleInstance/dockerfiles/18.4.0/
echo "Ejecutando el creador de la imagen"
./docker-images/OracleDatabase/SingleInstance/dockerfiles/buildContainerImage.sh -x -v 18.4.0
echo "Comprobación de la creación de la imagen"
docker image ls | grep "oracle/database"

