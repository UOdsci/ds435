# Data Science 435/535

*Data Mining, Exploration, and Visualization*

Instructor/author: Peter Ralph; plr@uoregon.edu

The actual website can be viewed at [https://uodsci.github.io/ds435/](https://uodsci.github.io/ds435/).

# Building the website locally:

Make a python virtual environment; activate the environment; install `requirements.txt`.

Then, in the base directory, do
```
quarto render
```
This will produce a copy of the website in the `docs/` directory.
Then browse that directory.
To publish to github pages, commit any new files/changes as necessary and push.

# Notes on how this website was made:


## Links:

- the website got started looking at [the example of Louise Sinks](https://lsinks.github.io/posts/2023-11-01-website-building/website.html)
- lots of [example quarto websites](https://drganghe.github.io/quarto-academic-site-examples.html), including templates
- an example [class website](https://github.com/drganghe/energy-climate-policy)
- [lots of links](https://github.com/mcanouil/awesome-quarto) to quarto resources
- a list of [themes](https://quarto.org/docs/output-formats/html-themes.html) and sass variables
- a list of [options to quarto's revealjs format](https://quarto.org/docs/reference/formats/presentations/revealjs.html)

## Quarto oddities

To debug quarto rendering issues, put [`keep-md: true`](https://quarto-tdg.org/look-under-hood.html)
and perhaps `keep-ipynb: true`
in the top level of the YAML header of the qmd file.

- **Output of more than one format with the same extension:**
    Quarto by default does not deal with more than one output
    format that has the same file extension: if you try to specify both `revealjs` and `html`
    formats it [throws a `NotFound` error](https://github.com/quarto-dev/quarto-cli/issues/4583).
    So: you need to either specify the output extension (e.g., `output-ext: slides.html`)
    or else specify the `output-file: ` for one of them by hand.

- **Revealjs pauses:** Using `. . .` (pause) for your revealjs slides
    ends you up with `. . .` in other formats.
    The [solution](https://github.com/quarto-dev/quarto-cli/issues/2302#issuecomment-1237212189)
    is a lua filter that removes them.

- **Don't try to have ipynb files as the *primary* file.**
    Quarto wants the "primary" files to be qmd/md, and all others to derive from those.
    For example, if you try to have a ipynb file
    that you then render to html, and have links to both,
    like `download homework here: \[ipynb](hw.ipynb) \[html](hw.html)`,
    then quarto will automatically adjust the first link to be to `hw.html`,
    same as the second one.
    The workaround is to explicitly setting the
    [render targets](https://quarto.org/docs/websites/index.html#render-targets)
    which means you have to put every file you do want rendered in a list somewhere.

## Slides:

Before, I've made slides with **interactive code** using [RISE](https://rise.readthedocs.io/en/latest/).
However, this is not maintained, and the replacement, [jupyterlab-rise](https://github.com/jupyterlab-contrib/rise),
is not yet there (or actively developed, AFAICT).
Another option is Quarto's [interactive code blocks](https://r-wasm.github.io/quarto-live/getting_started/editor.html).
A difference here is that with RISE you're editing the actual juypter notebook.
This has the upside that students can go back and look at what you did.
Maybe it's possible to write slides in markdown (qmd),
render these [to ipynb](https://quarto.org/docs/computations/python.html),
and then display them using RISE.
However, that'd require being able to have the correct cell structure and cell metadata
in the ipynb output, and hence a custom pandoc template.

Options:

- write slide documents as jupyter notebooks, and render with quarto:
    **but** quarto executes and displays the jupyter notebooks nicely as html
    but does not make slides.

- write slide documents as jupyter notebooks, and render with nbconvert:
    **but** all the nice markdown available to customize slides via pandoc
    (e.g., columns, styled divs, etc) is not available

- write slide documents as markdown (qmd), and render to ipynb and slides
    using quarto.

Quarto is really only set up to have the source as `qmd` files.
For instance, if you try to tread the `ipynb` files as the primary documents,
doing `quarto render` will overwrite your `ipynb` file (as it executes it?),
rather than sensibly doing this elsewhere.
And don't try maintaining both a `file.md` and a `file.ipynb`,
I'll bet one would be clobbered.

## Other notes:

Alt text is done like this:
```
![Caption](none.png "title text"){fig-alt="alt text"}
```
and simply appending [a backslash](https://pandoc.org/MANUAL.html#extension-implicit_figures)
makes the alt text the same as the caption:
```
![Caption and alt text](none.png "title text")\
```
