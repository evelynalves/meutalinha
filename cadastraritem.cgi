#!/bin/bash
read POST
usuario=$(echo $POST | cut -d"&" -f1 | cut -d"=" f2)
senha=$(echo $POST | cut -d"&" -f2 | cut -d"=" f2)
echo $usuario';'$nome >> ../cadastraritem.html
cat <<EOFFF
content-type: text-html
<html>
<h1>caralho</h1>
<a href="../pgnadm.html">Voltar</a>
</html>
EOFFF
