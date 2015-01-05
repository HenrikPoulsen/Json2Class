import argparse
from convert import convert


def main():
    # First we parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("source",
                        help='Location of the json file(s) to convert. Can be URL (http/https), a file or a folder')
    parser.add_argument("--namespace",
                        help="The namespace the generated files will be in.",
                        default="Json2Class")
    parser.add_argument("--cs-out",
                        help='Folder where the generated C# file(s) should be placed')
    parser.add_argument("--cs-engine",
                        help='Comma separated list of engines to be used for reading/writing Json object in C#. Supported are: unitysimple, newtonsoft',
                        default="unitysimple")
    parser.add_argument("--java-out",
                        help='Folder where the generated Java file(s) should be placed')
    parser.add_argument("--java-engine",
                        help='Comma separated list of engines to be used for reading/writing Json object in Java. Supported are: jsonsimple, gson',
                        default="jsonsimple")
    parser.add_argument("--py-out",
                        help='Folder where the generated Python file(s) should be placed')
    parser.add_argument("--py-engine",
                        help='Comma separated list of engines to be used for reading/writing Json object in Python. Supported are: json',
                        default="json")
    args = parser.parse_args()

    targets = {}

    if args.py_out:
        targets['py'] = {"path": args.py_out, "engines": args.py_engine.split(',')}
    if args.cs_out:
        targets['cs'] = {"path": args.cs_out, "engines": args.cs_engine.split(',')}
    if args.java_out:
        targets['java'] = {"path": args.java_out, "engines": args.java_engine.split(',')}

    convert.run(args.namespace, targets, args.source)


if __name__ == "__main__":
    main()