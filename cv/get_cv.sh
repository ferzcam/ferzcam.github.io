set -e

cd scripts
python publications.py
python teaching.py
python honors.py
python talks.py
python extracurricular.py

cd ..
xelatex cv.tex
mv cv.pdf ../assets/cv.pdf
