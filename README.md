# IMAST-EFREI
This is Sarah Gronemann's and Laura Scholz' IMAST Project for EFREI.
Further information can be found in our report about this project.

The objective is to code a website that can show users how healthy or harmful cosmetic projects are.
This is achieved with a web scraper, the use of a website's API and our own Flask API.

The Flask API can be found under Flask API -> __caller__.py
The web scraper and the other API can be found under Sephora_Webscraper.py in the same folder.
Under check.py is the assessment of the ingredients described.
The entries for the database are created with insert.py

The Website can be found in the folder IMAST-EFREI.
The different pages (views) can be found in src -> routes, there are two pages: / and about
The layout is saved in the +layout.svelte file. The pages itself in the +page.svelte files.
The Doughnut Chart Component can be found in src -> routes -> Chart.svelte

The folder BadIngredients is used to save the harmful ingredients and the according .csv files

The folder Database is used to create the database.