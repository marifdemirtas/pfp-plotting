# Local Deployment Steps

- Make sure you create a new conda environment (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) with Python 3.8.20
- Install requirements from requirements.txt using pip
    
    pip install -r requirements.txt

- Update the files under _sources, add new pages/new problems as needed
- (Optional) set a project name in pavement.py, line 13
- Run `runestone build' for building 
- Run `runestone serve' for debugging (you may need to delete the build folder with `rm -rf build/` and run the build command again)