# Le but de ce programme est de lancer sextractor sur toutes les images réduites
# dans les filtres rouge et vert.

rm m13-green-final/*.dat
rm m13-red-final/*.dat

for image in m13-green-final/*
do
	sextractor "$image"
	mv test.cat "$image".dat
done

for image in m13-red-final/*
do
	sextractor "$image"
	mv test.cat "$image".dat
done
