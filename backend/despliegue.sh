#!/bin/bash

FILEC=./fisproject/requirements.txt
FILEL=./local/requirements.txt
FILED=./deploy/requirements.txt

deploy_local(){
  prompt -i "\n Desplegando docker en local"
  if has_command docker-compose; then
    if [[ -e "$FILEC" && -e "$FILEL" ]]; then
      prompt -i "\n Copiando requirements.txt al despliegue"
      rm -v ./local/requirements.txt
      cp -v ./fisproject/requirements.txt ./local/requirements.txt
      cd ./local
      docker-compose up -d --build
      cd ..
    else
      prompt -e "\n El archivo requirements.txt no existe, verifique su existencia"
    fi
  else
    prompt -e "\n Docker compose no está instalado"
  fi
}

deploy(){
  prompt -i "\n Desplegando docker en producción"
  if has_command docker-compose; then
    if [[ -e "$FILED" && -e "$FILEL" ]]; then
      prompt -i "\n Copiando requirements.txt al despliegue"
      rm -v ./deploy/requirements.txt
      cp -v ./fisproject/requirements.txt ./deploy/requirements.txt
      cd ./deploy
      docker-compose up -d --build
      cd ..
    else
      prompt -e "\n El archivo requirements.txt no existe, verifique su existencia"
    fi
  else
    prompt -e "\n Docker compose no está instalado"
  fi
}

function has_command(){
  command -v $1 > /dev/null
}

prompt(){
  case ${1} in
    "-s"|"--success")
      echo -e "${b_CGSC}${@/-s/}${CDEF}";;    # print success message
    "-e"|"--error")
      echo -e "${b_CRER}${@/-e/}${CDEF}";;    # print error message
    "-w"|"--warning")
      echo -e "${b_CWAR}${@/-w/}${CDEF}";;    # print warning message
    "-i"|"--info")
      echo -e "${b_CCIN}${@/-i/}${CDEF}";;    # print info message
    *)
    echo -e "$@"
    ;;
  esac
}

PS3='Seleccione una opción: '
options=("Despliegue local" "Despliegue" "Cerrar")
select opt in "${options[@]}"
do
    case $opt in
        "Despliegue local")
            echo "Despliegue local 1"
            deploy_local
            ;;
        "Despliegue")
            echo "Despliegue"
            deploy
            ;;
        "Cerrar")
            break
            ;;
        *) echo "Opcion invalida $REPLY";;
    esac
done
