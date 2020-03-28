import os
import json
import hashlib


class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def colorPrint(color, msg):
    if color == 'RED':
        print(f'{bcolors.RED}{msg}{bcolors.ENDC}')
    elif color == 'GREEN':
        print(f'{bcolors.GREEN}{msg}{bcolors.ENDC}')
    else:
        print(msg)


def removeIfExist(path):
    if os.path.exists(path):
        os.remove(path)


def getJSONPath(version):
    ROOT_DIR = getRootPath()
    fileName = 'v' + str(version) + '.json'
    return os.path.join(ROOT_DIR, fileName)


def getStaticPath(version, fileName):
    FOLDER_PATH = getFolderPath(version)
    return os.path.join(FOLDER_PATH, fileName)


def getHash(version, fileName):
    path = getStaticPath(version, fileName)
    if os.path.exists(path) is False:
        return False

    with open(path, "rb") as f:
        fbytes = f.read()
        readable_hash = hashlib.md5(fbytes).hexdigest()
        return readable_hash


def saveJSON(obj, path):
    print('[Saving JSON]', path)
    removeIfExist(path)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=4)


def loadJSONFrom(path):
    if os.path.exists(path) is False:
        return {}

    with open(path) as f:
        return json.load(f)


def getFolderPath(version):
    ROOT_DIR = getRootPath()
    folder = 'v'+str(version)
    return os.path.join(ROOT_DIR, folder)


def getRootPath():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    res = os.path.join(ROOT_DIR, '..')
    return os.path.abspath(res)
