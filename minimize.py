from csscompressor import compress
from os import walk
from os.path import join as join_path


if __name__ == '__main__':
    for root, _, files in walk("."):
        for file in files:
            path = join_path(root, file)
            if path.endswith(".css") or path.endswith(".html"):
                with open(path, "r") as f:
                    out = compress(f.read())
                with open(path, "w") as f:
                    f.write(out)
                print("Process " + path)
