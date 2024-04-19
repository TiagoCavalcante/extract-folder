from gzip import open as gzip_open
from os import path, remove, walk
from shutil import copyfileobj
from sys import argv, exit
from zipfile import ZipFile, is_zipfile


def is_gzip_file(filepath):
  try:
    with open(filepath, "rb") as f:
      return f.read(2) == b"\x1f\x8b"
  except:
    return False


def decompress_gzip(source_path, dest_path):
  with gzip_open(source_path, "rb") as f_in:
    with open(dest_path, "wb") as f_out:
      copyfileobj(f_in, f_out)
  remove(source_path)


def extract_zip(zip_path, extract_to):
  with ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_to)
  remove(zip_path)


def walk_and_decompress(root_path):
  for dirpath, dirnames, filenames in walk(
    root_path
  ):
    for filename in filenames:
      print(filename)
      file_path = path.join(dirpath, filename)
      if is_gzip_file(file_path):
        # Assuming the decompressed filename by
        # stripping the last extension.
        decompressed_path = path.splitext(
          file_path
        )[0]
        decompress_gzip(
          file_path, decompressed_path
        )
      elif is_zipfile(file_path):
        extract_zip(file_path, dirpath)


if __name__ == "__main__":
  if len(argv) != 2:
    print(
      "Usage: python script.py <path_to_directory>"
    )
    exit(1)

  root_path = argv[1]
  walk_and_decompress(root_path)
