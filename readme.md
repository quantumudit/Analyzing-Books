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

The objective of this project is to gather information about books and their attributes from the website [Books To Scrape][website_link].

The collected data will then undergo a thorough exploratory data analysis, aimed at gaining valuable insights. 

These insights will be effectively visualized using the Power BI tool to provide a clear and comprehensive understanding of the data. The project's primary focus is to extract information from the website and turn it into useful insights and visual representations.

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

### 01_SCRAPER

This directory comprises a [Python script](01_SCRAPER/main.py) designed to extract information from the website and a [flat file](01_SCRAPER/scraped_data.csv) that stores the data obtained through the scraping process. 

The script in this directory automates the data scraping process, making it easier to collect information from the website in question. The flat file serves as a storage space for the scraped data, allowing for easy access and manipulation of the information gathered. 

This setup facilitates the efficient and organized management of the data obtained from the website.

### 02_ETL

This directory houses a [Jupyter Notebook](02_ETL/books_data_transformation.ipynb) that undertakes an ETL (Extract, Transform, Load) process on the data obtained through scraping. 

The purpose of this process is to convert the raw data into a form that is suitable for analysis. The Jupyter Notebook performs transformations on the scraped dataset to clean, organize, and structure the data into a format that is ready for analysis. 

This notebook is characterized by its thorough documentation, with each step of the analysis process clearly explained and described. 

The data cleaning and transformation steps, in particular, are carefully documented, ensuring that the thought process and decisions made during these processes are easily understood. 

This attention to detail in the documentation makes the notebook a valuable resource for anyone looking to understand how the data was cleaned and transformed to generate meaningful insights.

Finally, the transformed data is exported into the [03_DATA](03_DATA/) directory, making it easily accessible for further examination and analysis.

This Jupyter Notebook serves as a crucial step in the data preparation process, enabling the effective and efficient transformation of raw data into a form that can provide valuable insights.

### 03_DATA

This directory contains the data that can be directly used for data analysis and visualization.

The contents of this directory include only the pristine and organized [data](/03_DATA/books_data.csv), ready to be utilized for data analysis and visualization. 

This data has been thoroughly processed and scrubbed of any errors or inconsistencies, ensuring that it can be relied upon to provide accurate and meaningful insights. 

### 04_ANALYSIS

This directory contains the python notebooks that analyzes the clean dataset to generate insights.

This directory contains a [Jupyter Notebook](/04_ANALYSIS/books_data_analysis.ipynb) that analyzes the clean dataset to uncover valuable insights. 

This notebook performs complex data analysis and has been crafted to make it easy to work with the clean data. 

The notebook is thoroughly annotated and the results of each analysis are clearly documented within the text cells. This detailed documentation makes it easy to follow the thought process and understand the insights generated through the analysis. 

The well-documented nature of the notebook makes it a valuable resource for anyone looking to gain a deeper understanding of the data and the insights it contains.

### 05_DASHBOARD

This directory houses a straightforward [markdown file](5_DASHBOARD/Books%20Analysis%20Dashboard.md) that includes an embedded link to a Power BI report. 

This report serves as a visual representation of the data and provides a dynamic, interactive experience for exploring and analyzing the information. 

The simplicity of the markdown file, combined with the robust capabilities of Power BI, make it easy to access and interact with the data in a way that is both intuitive and insightful. 

Whether you are looking to gain a high-level overview of the data, or to drill down into specific details, the Power BI report provides an effective and engaging way to work with the data.

### 06_RESOURCES

This directory serves as a repository for various visual elements used in this project, including images, icons, layouts, styling files, etc. 

These elements play a crucial role in the overall presentation and visualization of the data and help to bring the insights generated by the analysis to life. 

By having these elements easily accessible in a central location, the project is streamlined and efficient, allowing for faster and more effective data analysis and visualization.

## Prerequisites

To fully grasp the concepts and processes involved in this project, it is recommended to have a solid understanding of the following skills:

- Fundamental knowledge of Python and Jupyter Notebook
- Familiarity with the Python libraries listed in the [requirements.txt][requirements] file
- Basic proficiency in HTML and CSS
- Basic familiarity with browser developer tools
- An understanding of the basics of Power BI

Having these skills as a foundation will help to ensure a smooth and effective experience while working on this project.

> The selection of applications and their installation process may differ depending on personal preferences and computer configurations.

## Architecture

The architecture of this project is straightforward and can be easily understood through the accompanying diagram, as seen below:

![Process Architecture][process_workflow]

The project architecture consists of the following steps:

- **Data scraping**: Data is collected from a website using a Python script and stored in a flat file.
- **Data cleaning**: The raw data is processed and cleaned through the use of an ETL-specific Jupyter Notebook.
- **Data visualization**: The cleaned and analysis-ready dataset is used for exploratory data analysis (EDA) through Jupyter Notebook and creating a comprehensive and insightful report through Power BI.

These steps are designed to be straightforward and efficient, allowing for quick and effective analysis of the data and generation of meaningful insights.

## Demo

The following illustration demonstrates the process of collecting data from the website through scraping:

![Scraping Graphic][scraping_graphic]

Access the interactive Power BI dashboard by clicking on this link here:

[![Power BI Dashboard][dashboard_image]][dashboard_link]

## Support

If you have any questions, concerns, or suggestions, feel free to reach out to me through any of the following channels:

[![Linkedin Badge][linkedinbadge]][linkedin] [![Twitter Badge][twitterbadge]][twitter]

If you find my work valuable, you can show your appreciation by [buying me a coffee][buy_me_a_coffee]

<a href="https://www.buymeacoffee.com/quantumudit" target="_blank">
<img src="https://i.ibb.co/9cyrq6m/buy-me-a-coffee.png" alt="buy-me-a-coffee" border="0" width="170" height="50">
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
[dashboard_image]: 06_RESOURCES/dashboard_image.png

<!-- External Links -->

[website_link]: https://books.toscrape.com/
[requirements]: ./requirements.txt
[dashboard_link]: https://app.powerbi.com/view?r=eyJrIjoiMjdlZjJjYmUtNjEyMC00ODVjLTk4Y2YtMWEzYmI4MDZlNjljIiwidCI6IjcwODlkNGIxLTQyMmUtNDYzZi1hNGM3LTViY2FiOTk0MGRiZCJ9

<!-- Profile Links -->

[linkedin]: https://www.linkedin.com/in/uditkumarchatterjee/
[twitter]: https://twitter.com/quantumudit
[buy_me_a_coffee]: https://www.buymeacoffee.com/quantumudit

<!-- Shields Profile Links -->

[linkedinbadge]: https://img.shields.io/badge/-uditkumarchatterjee-0e76a8?style=flat&labelColor=0e76a8&logo=linkedin&logoColor=white
[twitterbadge]: https://img.shields.io/badge/-@quantumudit-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/quantumudit
