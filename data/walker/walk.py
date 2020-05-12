from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, List
from os import listdir
from os.path import isdir, basename, join as join_path, getmtime, getsize, sep
from distutils.version import LooseVersion
from humanize import naturalsize


@dataclass
class FileInfo:
    version: LooseVersion
    date: date
    size: str
    link: str

    @classmethod
    def fromfile(cls, path: str, url_prefix: str) -> "FileInfo":
        """
        File name must be in format name-v.v.v-platform
        :param url_prefix: url prefix, for example: /static
        :param path: path to file (relative!)
        :return: "FileInfo"
        """
        try:
            version = LooseVersion(basename(path).split("-")[1])
        except (ValueError, IndexError):
            version = LooseVersion()

        # convert /foo/bar/spam/download/EyePointS1/firmware to download/EyePointS1/firmware
        path_short = join_path(*path.split(sep)[-3:])

        return FileInfo(version,
                        datetime.fromtimestamp(getmtime(path)).date(),
                        naturalsize(getsize(path)),
                        join_path(url_prefix, path_short))


def _walk_software(path: str, url_prefix: str) -> List[FileInfo]:
    result = []
    for file in listdir(path):
        fullpath = join_path(path, file)
        if isdir(file):
            continue
        result.append(FileInfo.fromfile(fullpath, url_prefix))
    return sorted(result, key=lambda f: f.version, reverse=True)


def _walk_product(path: str, url_prefix: str) -> Dict[str, List[FileInfo]]:
    result = {}
    for software in listdir(path):
        fullpath = join_path(path, software)
        if not isdir(fullpath):
            continue
        result[software] = _walk_software(fullpath, url_prefix)
    return result


def walk(path: str, url_prefix: str) -> Dict[str, Dict[str, List[FileInfo]]]:
    """
    Search files in directory
    :param path:
    :param url_prefix:
    :return:
    smth like:
    {"eyepoint-s1": {
        "firmware": [
            FileInfo, FilInfo, FileInfo
        ],
        "debugger": [
            FileInfo, FineInfo, FineInfo
        ]
      }
    }
    """

    result = {}

    for product in listdir(path):
        fullpath = join_path(path, product)
        if not isdir(fullpath):
            continue
        result[product] = _walk_product(fullpath, url_prefix)

    return result


if __name__ == '__main__':
    #  Run example
    result = walk("view/static/download", "/static/download")
    print(result)
