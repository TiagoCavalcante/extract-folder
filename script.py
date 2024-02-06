"""Extract compressed files in a given directory.

It supports both gzip and zip formats.
This is especially useful if you downloaded a site
from the Internet Archive.
You can execute the following commands to obtain
the files from a site in the Internet Archive.
```sh
sudo apt install ruby-rubygems
sudo gem install wayback_machine_downloader
wayback_machine_downloader -a URL -p 1000 -s
```.
"""

from gzip import open as gzip_open
from pathlib import Path
from shutil import copyfileobj
from sys import argv, exit
from zipfile import ZipFile

from magic import Magic

EXPECTED_ARG_COUNT = 2


def identify_compression_type(
    file_path: Path,
) -> str:
    """Identify MIME type of a file or directory.

    This uses the magic library.

    Args:
    ----
        file_path: Path to the file or directory.

    Returns:
    -------
        MIME type of the file or "directory" if
        it's not a file.

    """
    if file_path.is_dir():
        return "directory"
    mime = Magic()
    return mime.from_file(str(file_path))


def extract_file(file_path: Path) -> None:
    """Extract file based on its MIME type.

    Supports gzip and zip formats.

    Args:
    ----
        file_path: Path to the compressed file, if
        it is a file.

    """
    compression_type = identify_compression_type(
        file_path,
    )

    if compression_type == "application/gzip":
        with gzip_open(
            file_path,
            "rb",
        ) as f_in, file_path.with_suffix("").open(
            "wb",
        ) as f_out:
            copyfileobj(f_in, f_out)
    elif compression_type == "application/zip":
        with ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(file_path.parent)


def process_folder(folder_path: Path) -> None:
    """Process a folder for extraction.

    This is done recursively.

    Args:
    ----
        folder_path: Path to the folder containing
        files to be extracted.

    """
    for item in folder_path.iterdir():
        if item.is_dir():
            process_folder(item)
        else:
            mime_type = identify_compression_type(
                item,
            )
            if mime_type in [
                "application/gzip",
                "application/zip",
            ]:
                extract_file(item)


def print_help() -> None:
    """Print the usage instructions."""
    print("Usage: python script.py <folder_path>")
    print("  <folder_path>: Path to the folder containing")
    print("                 the compressed files.")


if __name__ == "__main__":
    if len(argv) != EXPECTED_ARG_COUNT:
        print_help()
        exit(1)

    folder_path = Path(argv[1])

    if not folder_path.exists():
        print_help()
        exit(1)

    process_folder(folder_path)
