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
The .obj file that needs to be processed with this code must follow certain rules

1. The name of referenced .mtl file in the .obj file needs to be the same as the .obj file itself.
```
1. Open the .obj file in a text editor (notepad++ etc.)
2. Search for the term 'mtllib' the reference after the mtllib should be <name_of_obj_file>.mtl

# Example
# .obj file name: YellowJacket.obj
# mtllib YellowJacket.mtl
```

2. Categories need to be assigned to material group inside the .obj file
```
1. Open the .obj file in a text editor (notepad++ etc.)
2. Seach for the term 'usemtl'
3. Update the term refernces after 'usemtl' to include one of the categories mentioned in util.py file

# Example
# .obj file name: Buzz.obj
# usemtl <whatever>_cloth
# usemtl <anythin>_wood
```

 
