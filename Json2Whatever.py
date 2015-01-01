import argparse
from convert import convert



def main():
    # First we parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("source",
                        help='Location of the json file(s) to convert. Can be URL (http/https), a file or a folder')
    parser.add_argument("--namespace",
                        help="The namespace the generated files will be in.",
                        default="Json2Whatever")
    parser.add_argument("--cs-out",
                        help='Folder where the generated C# file(s) should be placed')
    parser.add_argument("--py-out",
                        help='Folder where the generated Python file(s) should be placed')
    args = parser.parse_args()

    targets = {}

    if args.py_out:
        targets['py'] = args.py_out
    if args.cs_out:
        targets['cs'] = args.cs_out

    convert.run(args.namespace, targets, args.source)



if __name__ == "__main__":
    main()