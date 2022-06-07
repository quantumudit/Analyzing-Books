# ![Project Logo][project_logo]

---

<h4 align="center">Scraping & Analyzing books from <a href="https://books.toscrape.com/" target="_blank">Books To Scrape</a> website with <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">Python</a> and <a href="https://en.wikipedia.org/wiki/Microsoft_Power_BI" target="_blank">Power BI</a></h4>

<p align='center'>
<img src="https://i.ibb.co/KxfMMsP/built-with-love.png" alt="built-with-love" border="0">
<img src="https://i.ibb.co/MBDK1Pk/powered-by-coffee.png" alt="powered-by-coffee" border="0">
<img src="https://i.ibb.co/CtGqhQH/cc-nc-sa.png" alt="cc-nc-sa" border="0">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#demo">Demo</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

## Overview

This project focuses on scraping books and their associated attributes from [Books To Scrape][website_link], performing exploratory data analysis to generate insights and visualize them with the help of Power BI.

[![Website Snippet][website_snippet]][website_link]

The repository directory structure is as follows:

Analyzing-Books<br>
├─ 01_SCRAPER<br>
├─ 02_ETL<br>
├─ 03_DATA<br>
├─ 04_ANALYSIS<br>
├─ 05_DASHBOARD<br>
├─ 06_RESOURCES<br>

The type of content present in the directories is as follows:

<h5>01_SCRAPER</h5>

This directory contains the python script to scrape data from the website along with flat file that has the scraped data.

<h5>02_ETL</h5>

This directory contains a Jupyter Notebook that performs ETL on the scraped dataset to produce an analysis-ready dataset and exports that into the _03_DATA_ directory.

<h5>03_DATA</h5>

This directory contains the data that can be directly used for data analysis and visualization.

<h5>04_ANALYSIS</h5>

This directory contains the python notebooks that analyzes the clean dataset to generate insights.

<h5>05_DASHBOARD</h5>

This directory contains a simple markdown file with an embedded Power BI report link that visualizes the data.

<h5>06_RESOURCES</h5>

This directory contains images, icons, layouts, etc. that are used in this project.

## Prerequisites

The major skills that are required as prerequisite to fully understand this project are as follows:

- Basics of Python & Jupyter Notebook
- Understanding of Python libraries mentioned in [requirements.txt][requirements] file
- Basics of HTML & CSS
- Basics of Power BI

> The choice of applications & their installation might vary based on individual preferences & system settings.

## Architecture

The project architecture is quite straight forward and can be explained through the below image:

![Process Architecture][process_workflow]

As per the above workflow suggests; we are first scraping the data from the website using the Python script and collecting it in a flat file which is then processed and cleaned with another ETL specific Jupyter Notebook.

Finally; we leverage the clean & analysis-ready dataset for some exploratory data analysis (EDA) using Jupyter Notebook and creating an insightful report using Power BI.

## Demo

The below graphic shows scraping of data from the website:

![Scraping Graphic][scraping_graphic]

## Support

If you have any doubts, queries or, suggestions then, please connect with me in any of the following platforms:

[![Linkedin Badge][linkedinbadge]][linkedin] [![Twitter Badge][twitterbadge]][twitter]

If you like my work then, you may support me at [Patreon][patreon]:

<a href="https://www.patreon.com/quantumudit" target="_blank">
<img src="https://i.ibb.co/94bkJwp/become-a-patreon.png" alt="become-a-patreon" border="0" width="170" height="50">
</a>

## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src="https://i.ibb.co/mvmWGkm/by-nc-sa.png" alt="by-nc-sa" border="0" width="88" height="31">
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.

<!-- Image Links -->

[project_logo]: 06_RESOURCES/project_cover_image.png
[process_workflow]: 06_RESOURCES/process_architecture.png
[scraping_graphic]: 06_RESOURCES/scraping_graphic.gif
[website_snippet]: 06_RESOURCES/website_snip.png
[dashboard_image]: ...

<!-- External Links -->

[website_link]: https://books.toscrape.com/
[requirements]: ./requirements.txt
[dashboard_link]: https://app.powerbi.com/..

<!-- Profile Links -->

[linkedin]: https://www.linkedin.com/in/uditkumarchatterjee/
[twitter]: https://twitter.com/quantumudit
[patreon]: https://www.patreon.com/quantumudit

<!-- Shields Profile Links -->

[linkedinbadge]: https://img.shields.io/badge/-uditkumarchatterjee-0e76a8?style=flat&labelColor=0e76a8&logo=linkedin&logoColor=white
[twitterbadge]: https://img.shields.io/badge/-@quantumudit-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/quantumudit
