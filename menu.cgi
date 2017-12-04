#!/bin/bash
read POST
echo "Content-type: text/html"
echo
op=$(echo $POST | cut -d"=" -f2)
relat(){
	echo "<h1>Relatório</h1>	"
}
cadas(){
	source ./scripts/cadas.sh
	menu
}
modif(){
	source ./scripts/modif.sh
	menu
}
exclu(){
	source ./scripts/exclu.sh
	menu
}
opcao(){
case $op in
	"Relatorio") relat ;;
	"Cadastro") cadas ;;
	"Modificacao") modif ;;
	"Exclusao") exclu ;;
	*) echo "<h1>Falha no Script</h1>" ;;
esac
}
opcao
