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

    for lang in targets.keys():
        #if targets[lang].startsWith("http://") or targets[lang].startsWith("https://"):
        #if not os.path.isdir(targets[lang]):
        #    print targets[lang] + " is an invalid directory. Skipping " + lang + " generation."
        #    continue

        module = __import__(lang+".generate")
        module.generate.headers()
        print targets[lang]



if __name__ == "__main__":
    main()