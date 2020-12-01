# Generate_MTL
A python script to generate simple .mtl files for .obj files vy selecting random images as textures froma pool of available categories

## How to install and run?
### 1. Create a new virtual environment
It’s advisable to [make a new virtual environment](https://towardsdatascience.com/setting-up-python-platform-for-machine-learning-projects-cfd85682c54b) for this project and install the dependencies. Following steps can be taken to download get started with generate_mtl
```
conda create -n generate_mtl python=3.6
# Once the environment is set up, activate it
activate generate_mtl
```

### 2. Download the repository
```
git clone https://github.com/aqeelanwar/generate_mtl.git
cd generate_mtl
```

### 3. Install required packages
```
pip instal -r requirements.txt
```

### 4. Run the gen_mtl.py file
```
python gen_mtl.py
```

## Code structure
The .obj file that need to be processed with this code needs to follow certain rules

1. The name of referenced .mtl file in the .obj file needs to be the same as the .pbj file itself.
```
# Example
# .obj file name: YellowJacket.obj
# Open the file in a text editor (notepad++ etc.)
# Search for the term 'mtllib' the reference after the mtllib should be 'YellowJacket.mtl'
```

 
