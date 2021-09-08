import matplotlib.image as mpimg

def read_image(filepath):

    return mpimg.imread(filepath)

def read_list_of_images(list_of_files, exposures):

    images = {}

    for filepath, exposure in zip(list_of_files, exposures):

        images[exposure] = read_image(filepath = filepath)

    return images