

---
# UV
1. project script, [project.scripts], doesn't work after running it several times
2. use uv to init pkb (app) and create pkb (package) later in order to be able to build & publish
3. run uv publish only in pkb (app) dir otherwise it will not find the dist folder
4. only pkb (package) dir meets the pypi folder structure or package upload will fail
5. run uv build in pkb (package) dir only as it produces right name in pkb/dist/pkb-0.1.0.tar.gz 
6. 
---
# tests
1. add pytest in pkb package folder: uv add pytest --dev
2. run pytest from both app and package folder: uv run pytest 
3. add tests folder under pkb (package)/src folder
4. 