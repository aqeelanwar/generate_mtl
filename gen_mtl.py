# Author: Aqeel Anwar(ICSRL)
# Created: 10/1/2020, 11:15 PM
# Email: aqeel.anwar@gatech.edu


from util import *

# Set the input paths to texture and object folders
texture_folder = 'Texture/'
parent_obj_folder = 'source_obj'

texture_dict = create_texture_dict(texture_folder)
path, dirs, files = os.walk(parent_obj_folder).__next__()

already_processed = ['']
for obj_f in dirs:
    undefined = []
    processed = []
    obj_status = []
    vertex_status = []
    if obj_f not in already_processed:
        obj_folder = path+os.path.sep+obj_f
        p, d, f = os.walk(obj_folder).__next__()
        for obj_file in f:
            if obj_file.endswith(".obj"):
                obj_file = obj_folder + os.path.sep + obj_file
                print('Processing: ', obj_file)
                mtl_dict, undefined, processed, obj_status, vertex_error = traverse_obj(obj_file, texture_dict, undefined, processed, obj_status)
                vertex_status.append((obj_file, vertex_error))
                if not vertex_error:
                    generate_mtl(obj_file, mtl_dict)
                else:
                    continue

        write_file = obj_folder + "_vertex_error.txt"
        f = open(write_file, "w")
        for v in vertex_status:
            f.write(str(v))
            f.write("\n")
        f.close()

        write_file =obj_folder +".txt"
        f = open(write_file, "w")

        f.write('-------------------Status----------------------\n')
        for o in obj_status:
            f.write(str(o))
            f.write('\n')
            print(o)

        f.write('-------------Undefined Categories--------------\n')
        print('----------------------------------------')
        print('--------------Processed-----------------')
        for p in processed:
            print(p)
        print('----------------------------------------')
        print('--------------Undefined-----------------')
        for u in undefined:
            f.write(str(u))
            f.write('\n')
            print(u)
        f.close()






