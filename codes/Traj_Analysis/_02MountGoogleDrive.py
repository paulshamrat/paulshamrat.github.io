# Mount Google Drive
from google.colab import drive
drive.mount('/content/gdrive')

#Let's make a folder first. We need to import the os and path library
import os
from pathlib import Path 

#Then, we define the path of the folder we want to create.
#Notice that the HOME folder for a hosted runtime in colab is /content/
mdpath = Path("/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto")
#mdpath = Path("/content")


#Now, we create the folder using the os.mkdir() command
#The if conditional is just to check whether the folder already exists
#In which case, python returns an error
if os.path.exists(mdpath):
  print("path already exists")
if not os.path.exists(mdpath):
  os.mkdir(mdpath)
  print("path was succesfully created")


