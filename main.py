import os

os.chdir('tensorflow_object_counting_api')

print(os.path.join(os.path.dirname(os.getcwd()),'frontend/app.py'))

com = 'python ' + os.path.join(os.path.dirname(os.getcwd()),'frontend/app.py')
os.system(com)
