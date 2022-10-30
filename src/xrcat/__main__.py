from argparse import ArgumentParser
from xrcat import xrcat

def main():
    argp = ArgumentParser(prog = 'xrcat',
                    description = 'This is a small package for getting resources from Xresources')
    argp.add_argument('query', help="Name of resource")      # option that takes a value
    args = argp.parse_args()

    xrcat.updateResources()
    print(xrcat.getResource(args.query))

if __name__ == "__main__":
    main()
