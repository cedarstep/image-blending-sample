base_url = "https://www.spacetelescope.org/static/projects/fits_liberator/datasets/eagle/"
filenames = []

def task_download():
    actions = []
    for filename in filenames:
        action.append(['unzip','-o',base_url+filename])
        targets.append(['','',])
    return {'actions': [['wget', base_url+'/502nmos.zip']],
    'targets': ["502nmos.zip"] }
def task_unzip():
  return {'actions': [['unzip', '502nmos.zip']],
    'targets': ['502nmos.fits'],
    'file_dep': ['502nmos.zip']}
