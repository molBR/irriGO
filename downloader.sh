#!/bin/bash
ARQ="/home/comediabolado/PycharmProjects/leitorxml/previsao.xml"
if [ -f "$ARQ" ]		
then
	echo "Deletando arquivo passado"
	rm -r $ARQ
fi
wget "http://api.openweathermap.org/data/2.5/forecast?id=3460960&APPID=46da90f196b230adbbf21b78c275413e&mode=xml" -O "previsao.xml"