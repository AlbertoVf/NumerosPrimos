inicio=6300000000
final=6400000000
incremento=1000000
carpeta="primos-"$inicio"-"$final

python dist.py
cd Primos
mkdir $carpeta
# mv *.txt $carpeta
# tar czvf $carpeta.zip $carpeta
# rm -R $carpeta
# git add .
# git commit -m $carpeta
