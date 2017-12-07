# Le but de ce programme est de lancer sextractor sur toutes les images réduites
# dans les filtres rouge et vert.

rm ../output/m13-*.dat

for image in ../output/m13-*.fits
do
	sextractor "$image"
	mv test.cat "$image".dat
done
