%.html : %.ipynb
	jupyter nbconvert $< --to html

%.html : %.tex
	pandoc $< -t html --standalone --mathml -o $@

%.odt : %.tex
	pandoc $< -t odt -o $@

%.slides.html : %.ipynb
	jupyter nbconvert --execute $< --to slides
