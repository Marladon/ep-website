from csscompressor import compress as compress_css
from htmlmin import minify as compress_html
from os import walk
from os.path import join as join_path
from typing import Callable


def process_file(path: str, proc: Callable[[str], str]):
    with open(path, "r") as f:
        out = proc(f.read())
    with open(path, "w") as f:
        f.write(out)
    print("Process " + path)


if __name__ == '__main__':
    for root, _, files in walk("."):
        for file in files:
            path = join_path(root, file)
            if path.endswith(".css"):
                process_file(path, compress_css)
            elif path.endswith(".html"):
                process_file(path, compress_html)
