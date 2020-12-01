# Author: Aqeel Anwar(ICSRL)
# Created: 11/10/2020, 1:10 AM
# Email: aqeel.anwar@gatech.edu

import pywavefront, os, random
from shutil import copyfile

list_category = ['paper', 'Metal', 'Plastic', 'plastic', 'fabric', 'cloth', 'metal', 'wood', 'color', 'glass',
                 'leather', 'wallpaper', 'brick', 'tile', 'concrete', 'undefined']

def check_category(name):
    detected_cat = []
    for cat in list_category:
        found = name.find(cat)
        if found != -1:
            detected_cat.append(cat)
    if len(detected_cat)<1:
        detected_cat = ['undefined']
    return detected_cat

def create_texture_dict(path_to_folder):
    texture_dict = {}
    path, dirs, _ = os.walk(path_to_folder).__next__()
    for dir in dirs:
        texture_dict[dir] = []
        dir_path = path +dir
        _, _, files = os.walk(dir_path).__next__()
        for file in files:
            texture_dict[dir].append(dir_path + os.path.sep +file)

    return texture_dict

def traverse_obj(obj_filename, texture_dict, undefined, processed, obj_status):
    mtl_dict={}
    obj_success = True
    try:
        scene = pywavefront.Wavefront(obj_filename, create_materials=True)
        for name, material in scene.materials.items():
            # Contains the vertex format (string) such as "T2F_N3F_V3F"
            # T2F, C3F, N3F and V3F may appear in this string
            current_dict = {}
            print(name)
            current_dict['name'] = name
            cat = check_category(name)
            pool_of_textures = []
            for cat_ in cat:
                if cat_ == 'fabric':
                    cat_ = "cloth"

                print(cat_)
                # assert cat_!='undefined', 'Undefined category found. Edit the .obj file'
                if cat_ == 'undefined':
                    obj_success = False
                    undefined.append((name, obj_filename))
                else:
                    processed.append((name, obj_filename))
                    pool_of_textures += texture_dict[cat_]

            if len(pool_of_textures) > 0:
                current_dict['map_Kd'] = random.choice(pool_of_textures)
            mtl_dict[name] = current_dict
        obj_status.append((obj_success, obj_filename))
        return mtl_dict, undefined, processed, obj_status, False
    except Exception as e:
        print('error')
        err_msg = str(e)
        print(err_msg)
        # if "Trying to merge vertex data with different format:" in err_msg:
        return [], undefined, processed, obj_status, True


def generate_mtl(obj_filename, mtl_dict):
    mtl_filepath = obj_filename[:-3]+'mtl'
    print(mtl_filepath)
    mtl_file = open(mtl_filepath, 'w')

    # Set up Headers
    header = '# MTL file generator - Author Aqeel' + "\n"
    header += '# Generated through python script' + "\n\n"
    mtl_file.write(header)

    for key, element_dict in mtl_dict.items():
        line = 'newmtl '+element_dict['name'] + "\n"
        mtl_file.write(line)

        for key, value in element_dict.items():
            if key!='name':
                image_path = value
                src = value
                dst = mtl_filepath.rsplit(os.path.sep, 1)[0] + os.path.sep + image_path
                # Copy the texture to local folder
                if not os.path.exists(dst.rsplit(os.path.sep, 1)[0]):
                    os.makedirs(dst.rsplit(os.path.sep, 1)[0])
                copyfile(src, dst)
                line = "\t"+key + " " + image_path + "\n"
                mtl_file.write(line)

        mtl_file.write("\n")
    mtl_file.close()