# Personal Knowledge Base
Organize personal information with markdown files, folders and search


# Prerequisites
- Python >=3.12.7


# Installation 
Create a knowledge base folder, eg. kb

<pre>
mkdir kb && cd kb
</pre>

Get content folder and .env file for customization later

<pre>
git clone https://github.com/hyw208/pkb.git
cp -R ./pkb/content .
cp .env .
</pre>

Create/activate virtual environment and install pkb lib

<pre>
python -m venv .venv
source .venv/bin/activate
pip install pkb
</pre>
   

# Launch 
<pre>
python -m pkb.fast

// Or
uvicorn pkb.fast:app

</pre>


# Customize
Change site name and restart

<pre>
// in .env file, 
WEBSITE_NAME="Markdown Website"
</pre>

# TODO
1. fix both launch issues where 'poetry install' has to be run multiple times
2. 



<!-- Styling --->
<style type="text/css">
pre { 
   color:white; 
   background-color:grey;
   padding:5px;
}
</style>