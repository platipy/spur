from kurt.files import *

def convert_to_spyral(project_filename):
    project = ScratchProjectFile(project_filename)
    print project.stage.fields
    