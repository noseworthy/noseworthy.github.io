import sys
import urllib.request


def get_and_write_url(url:str, file_path:str) -> None:
    with urllib.request.urlopen(url) as response:
        with open(file_path, 'w') as w:
            w.write(response.read())


if __name__ == '__main__':
    if len(args) != 3:
        raise ValueError('Usage: get_url.py <url> <file_path>')

    url, file_path = sys.argv[1:]
    get_and_write_url(url, file_path)
