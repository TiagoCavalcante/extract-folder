# Compressed File Extractor

This project provides a Python script that automates the extraction of compressed files (which may not have the correct extension) within a given directory. It supports both gzip and zip formats, making it particularly useful for processing archives, such as those downloaded from the Internet Archive via the `wayback_machine_downloader`.

## Prerequisites

Before running the script, ensure you have Python 3 installed on your system. Additionally, the script uses the `magic` library for MIME type identification, so make sure to install this dependency:

```sh
python3 -m pip install python-magic
```

## Installation

No installation is needed. Just download the script file or clone this repository:
```sh
git clone https://github.com/TiagoCavalcante/extract-folder
```

## Usage

To use the script, navigate to the directory containing the script in your terminal and execute the following command:

```sh
python3 extract_compressed.py <folder_path>
```

Replace <folder_path> with the path to the directory containing the compressed files you wish to extract.

## Additional Information

To download files from a site in the Internet Archive, you can use the wayback_machine_downloader with the following commands:

```sh
sudo apt install ruby-rubygems
sudo gem install wayback_machine_downloader
wayback_machine_downloader -a URL -p 1000 -s
```
Replace URL with the target website's URL.
