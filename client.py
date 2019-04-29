#!/usr/bin/env python3 

import sys, json, csv, argparse
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# Ignore warnings ( Irritating ones from dicttoxml)
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


def result(interactive, output, mode, test_data = None, file = None):
    # Retrieve data directly from command line
    if interactive:
        if mode == 'normal':
            print()
            print("Enter you data. Once finished press CTRL+d (Mac,Linux), CTRL+z (Windows)")
            print()
            data = sys.stdin.read()
            reader = csv.DictReader(data.splitlines())
        elif mode == 'unittest':
            reader = csv.DictReader(test_data.splitlines())
    # Retrieve data from the file if file option is specified
    elif file:
        filename = file
        try:
            f = open(filename, 'r')
            reader = csv.DictReader(f)
        except FileNotFoundError:
            print("Unable to find the specified file")
            sys.exit(2)
    
    # Initialize Result
    result = {'person':[]}

    # Parse the CSV content
    for row in reader:
        if 'nationality' in row:
            del row['nationality']
        result['person'].append(row)
    
    # Close the file stream
    if file:
        f.close()

    # JSON result
    if output.lower() == 'json':
        print(json.dumps(result,indent=4))
        return json.dumps(result,indent=4) 

    # XML result
    elif output.lower() == 'xml': 
        xml = dicttoxml(result, attr_type=False)
        xml = parseString(xml)
        print(xml.toprettyxml())
        return xml.toprettyxml() 

def create_parser():
    parser = argparse.ArgumentParser()
    eg = parser.add_mutually_exclusive_group(required=True)
    eg.add_argument('-f', '--file', help='Name of the file containing your input data', required=False)
    eg.add_argument('-i','--interactive', help='Enter your input directly', action='store_true')
    parser.add_argument('-o','--output', help='Defines the output format. JSON or XML. Default is JSON', default='json', choices=['json','xml'])
    return parser.parse_args()
    
def main():
    args = create_parser()
    result(args.interactive, args.output.lower(), 'normal', file = args.file)


if __name__ == "__main__":
    main()
