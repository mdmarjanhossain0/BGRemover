from .inference import BGRemove



# from pathlib import Path
# import os
# WORKER_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# C:\\Users\\Marjan\\Desktop\\Marjan\\Python\\projects\\uploadimage\\media\\img\\21\\backgound.jpg"


def cutout(path):

    print(path)
    path = path[1:]
    output_path = "media/img/"

    bg_remover = BGRemove()
    result = bg_remover.image(filename=path, output=output_path, background=False)
    
    return result





