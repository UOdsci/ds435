---
title: "course schedule"
description: schedule, with links to slides and homeworks
date-modified: last-modified
---

The source code for these lectures is available at
[the github repository](https://github.com/UOdsci/ds435/).
Also please see the [technical_notes](technical_notes.html)
for software and other troubleshooting tips.

# Winter 2026

This is a *tentative* schedule,
that will evolve somewhat throughout the quarter.

Week 1: Exploratory Data Analysis

: Overview of the goals of the course:
    description, visualization, exploration, pattern discovery, and summarization.
    Introduction to different frameworks and goals,
    and relationship to preregistration and hypothesis testing.
    Types of data: tidy data, images, geospatial, words, time series.

    * Reading: Chapter 2 ("Exploratory Data Analysis") from Haig, *The Philosophy of Quantitative Methods* (see Canvas)
    * Reading: Introduction from Tan, Steinbach, & Kumar, *Introduction to Data Mining* (see Canvas)
    - *Case study:* the [Youth Tobacco Survey](https://www.cdc.gov/tobacco/about-data/surveys/historical-nyts-data-and-documentation.html)
    - Reading: [NYTS report 2024](https://www.cdc.gov/mmwr/volumes/73/wr/mm7341a2.htm)
    - Slides: [Introduction](/slides/introduction.html)
        ([ipynb](/slides/introduction.ipynb))
    - Discussion: [Exploratory Data Analysis](/slides/exploratory_data_analysis.html)
    - Demo: [Youth Tobacco Survey](/slides/YTS_intro.html)
        ([ipynb](/slides/YTS_intro.ipynb))
    - Assignment (due Monday 1/12):
        [ipynb](/assignments/yts_assignment.ipynb)
        [html](/assignments/yts_assignment.html)
    - Lab (for 1/9):
        [ipynb](/labs/yts_lab.ipynb)
        [html](/labs/yts_lab.html)

Week 2: Visualization

: Grammar of graphics.
    Overview of types of plot for uni- and multi-variate summarization,
    color pallettes, transformations.
    Output: bitmap, vector, and web-based interactive.

    - Links: [plotnine documentation](https://plotnine.org/)
    - Reading: [A layered grammar of graphics](https://vita.had.co.nz/papers/layered-grammar.pdf), Wickham
    - Slides: [Graphics and visualization](/slides/plotting.html)
    - Demo: [Grammar of Graphics](/slides/plotnine_intro.html)
    - Demo: [Weather Data](/slides/weather_intro.html)
        ([**completed version from class**](/demos/weather_inclass.ipynb))
    - Assignment (due Tuesday 1/20):
        [ipynb](/assignments/yts_assignment2.ipynb)
        [html](/assignments/yts_assignment2.html)
    - Lab (for 1/16):
        [ipynb](/labs/yts_lab2.ipynb)
        [html](/labs/yts_lab2.html)

Week 3: Summarizing, smoothing, and outliers.

: Split-apply-combine options.
    Types and goals of smoothers.
    Methods for outlier identification.

    - *Monday: no class (MLK day)*
    - Optional reading: [The Split-Apply-Combine strategy for data analysis](https://www.jstatsoft.org/article/view/v040i01/468)
    - Slides: [Split/apply/combine](/slides/split_apply_combine.html)
        ([**completed version from class**](/demos/split_apply_combine_inclass.ipynb))
    - Assignment (due Monday 1/26):
        [ipynb](/assignments/weather_assignment.ipynb)
        [html](/assignments/weather_assignment.html)

Weeks 4-5: Dimension reduction.

: What low-dimensional representations do and what they don't.
    Overview of methods: similarity- and distance-based;
    examples: principal component analysis, t-SNE.

    - Slides: [PCA](/slides/pca.html)
    - Slides: [PCA and SVD](/slides/pca_and_svd.html)
    - Demo: [penguin PCA](/slides/pca_penguins.html)
        ([**completed version from class**](/demos/pca_penguins_inclass.ipynb))
    - Assignment (due Monday 2/2):
        [ipynb](/assignments/kidney_assignment.ipynb)
        [html](/assignments/kidney_assignment.html)
    - Lab (for 1/30):
        [ipynb](/labs/pca_lab.ipynb)
        [html](/labs/pca_lab.html)
    - Slides: [Generalizing: tSNE](/slides/tSNE.html)
    - Slides: [On ordination](/slides/on_ordination.html)
    - Assignment (due Monday 2/9):
        [ipynb](/assignments/novel_assignment.ipynb)
        [html](/assignments/novel_assignment.html)
    - Slides: [Federalist papers](/slides/federalist.html)
        ([**completed version from class**](/demos/federalist_inclass.ipynb))
    - Lab (for 2/6):
        [ipynb](/labs/federalist_lab.ipynb)
        [html](/labs/federalist_lab.html)
        ([**completed version from class**](/demos/federalist_lab_inclass.ipynb))

Week 6: Working with words.

: Bag of words, preprocessing, embeddings,
    latent Dirichlet allocation,
    other applications of dimension reduction.
    Finding n-grams, sentiment analysis.

    - Slides: [Working with text](/slides/text_as_data.html)
    - Assignment (due Monday 2/16):
        [ipynb](/assignments/movie_assignment.ipynb)
        [html](/assignments/movie_assignment.html)
    - Slides: [Scraping, and plotting text](/slides/scraping_and_plotting.html)
    - Lab (for 2/13):
        [ipynb](/labs/scraping_lab.ipynb)
        [html](/labs/scraping_lab.html)

    
Week 7: Working with images.

: Formats; layers; types of image data.
    Normalization and pre-processing.
    Applications of dimension reduction.

Week 8: Objects from images.

: Convolutional neural networks;
    classification, segmentation, identification with pre-trained networks.

Week 9: Spatial data.

: Spatial smoothing and prediction.

Week 10: Case study.

: TBD
