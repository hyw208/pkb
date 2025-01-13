# Personal Knowledge Base

# TODO 
1. fix both launch issues where 'poetry install' has to be run multiple times
2. 

# Prerequisites
1. Python >=3.12.7


# Installation 
1. git clone https://github.com/hyw208/pkb.git to get the 'content' folder and its md files
2. cd pkb
3. python -m venv .venv
4. source .venv/bin/activate 
5. pip install pkb 
   

# To Launch 
1. python -m pkb.fast (sometimes doesn't work... need to run 'poetry install' many times)
2. uvicorn pkb.fast:app (sometimes doesn't work... need to run 'poetry install' many times)
3. 