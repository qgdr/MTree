# !~/anaconda3/bin/python
import os
import yaml

# def seek_files(root, filename):
#     """ shell> find root -name "filename" """
#     file_tuple_list = []
#     for dirpath, _, files in os.walk(root):
#         if filename in files:
#             file_tuple_list.append(dirpath)
    
#     return file_tuple_list


def change_str(nav, int_dir):
    if isinstance(nav, list):
        for idx, item in enumerate(nav):
            if isinstance(item, str):
                nav[idx] = os.path.join(int_dir, nav[idx])
            elif isinstance(item, dict):
                change_str(item, int_dir)
            else:
                raise 'nav error'
    elif isinstance(nav, dict):
        for key in nav.keys():
            if isinstance(nav[key], str):
                nav[key] = os.path.join(int_dir, nav[key])
            else:
                change_str(nav[key], int_dir)
    else:
        raise 'nav error'


def check_dir(nav):
    if isinstance(nav, list):
        for idx, item in enumerate(nav):
            if isinstance(item, str):
                if item[-1] == '/': # is a dir
                    nav.pop(idx)
                    for i, e in enumerate(sub_nav(root, item, filename)): 
                        nav.insert(idx+i, e)
            elif isinstance(item, dict):
                check_dir(item)
            else:
                raise 'nav error'
    elif isinstance(nav, dict):
        for key in nav.keys():
            if isinstance(nav[key], str):
                if nav[key][-1] == '/': # is a dir
                    nav[key] = sub_nav(root, nav[key], filename)
            else:
                check_dir(nav[key])
    else:
        raise 'nav error'


# def sub_nav(prestr, dirpath, filename):
#     """ sub cfg """
#     int_str = prestr + '/'
#     with open(dirpath+ '/' + filename, 'r') as ymlfile:
#         cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
#         nav = cfg['nav']
#         change_str(nav, int_str)
#     return nav
def sub_nav(root, dirpath, filename):
    """ sub cfg """
    with open(os.path.join(root, dirpath, filename), 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        nav = cfg['nav']
        change_str(nav, dirpath)
    return nav

    
if __name__ == '__main__':
    root = './docs/'
    filename = 'mkdocs.yml'
    # file_tuple_list = seek_files(root, 'mkdocs.yml')
    # print(file_tuple_list)

    with open('template.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    nav = cfg['nav']

        # for item in cfg['nav']:
        #     if isinstance(item, dict):
        #         for key in item.keys():
        #             print(key, item[key])
        #     else:
        #         print(item)

    # for dirpath in file_tuple_list:
    #     prestr = dirpath[len(root)+1:]
    #     nav.append({prestr : sub_nav(prestr, dirpath, 'mkdocs.yml')})

    # print(nav)
    check_dir(nav)
    with open('mkdocs.yml', 'w') as ymlfile:
        yaml.dump(cfg, ymlfile)
