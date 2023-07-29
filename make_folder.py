import os

# def make_folder(mem_id):
#
#     os.mkdir("mem_image/{}".format(mem_id))
#     os.mkdir("train/{}".format(mem_id))


def make_folder(mem_id):
    mem_image_folder = "mem_image/{}".format(mem_id)
    train_folder = "train/{}".format(mem_id)

    if not os.path.exists(mem_image_folder):
        os.mkdir(mem_image_folder)
    
    if not os.path.exists(train_folder):
        os.mkdir(train_folder)