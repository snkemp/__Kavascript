
from argparse import ArgumentParser

from src.parser import parse


def main():

    ap = ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('--port', '-p', action='store_true')
    ap.add_argument('--minify', '-m', action='store_true')

    args = ap.parse_args()

    parse(args.source, port=args.port, minify=args.minify)



if __name__ == '__main__':
    main()
