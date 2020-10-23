inicio=62 * 100 * 1000 * 1000
final=63 * 100 * 1000 * 1000
carpeta="primos-"$inicio"-"$final

cd Primos
mkdir $carpeta
mv *.txt $carpeta
tar czvf $carpeta.zip $carpeta
rm -R $carpeta
git add .
git commit -m $carpeta
