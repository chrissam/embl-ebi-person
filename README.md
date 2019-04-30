# EMBL-EBI Person client

This client generates person entities represented as JSON objects, such as
```json
{
    "person": [
    {
        "first_name": "John",
        "last_name": "Keynes",
        "age": "29",
        "favourite_colour": "red"
    },
    {
        "first_name": "Sarah",
        "last_name": "Robinson",
        "age": "54",
        "favourite_colour": "blue"
    }
    ]
}
```

XML object such as,
```xml
<root>
	<person>
		<item>
			<first_name>John</first_name>
			<surname>Keynes</surname>
			<age>29</age>
			<favourite_color>red</favourite_color>
		</item>
		<item>
			<first_name>Sarah</first_name>
			<surname>Robinson</surname>
			<age>54</age>
			<favourite_color>blue</favourite_color>
		</item>
	</person>
</root>
```
### INPUT
The client will consume both direct user input and text files with the following format:
```sh
first_name,surname,age,nationality,favourite_color
John,Keynes,29,British,red
Sarah,Robinson,54,,blue
```
**Note:**
Based on the requirement, the nationality field will not be represented in the response


# Script Usage
The script takes several options as arguments
```sh
./client.py -h
usage: client.py [-h] (-f FILE | -i) [-o {json,xml}]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Name of the file containing your input data
  -i, --interactive     Enter your input directly
  -o {json,xml}, --output {json,xml}
                        Defines the output format. JSON or XML. Default is
                        JSON
```
| Option | Description |
| ------ | ------ |
| -h / --help| Help |
| -f / --file | File input. Requires file Name |
| -i / --interactive | Direct Input. Used for entering your input interactivley |
| -o / --output | Output Format (JSON or XML). Default is JSON |

# Dependency and Requirements
This client requires only one external dependency - (dicttoxml). You can install it by running
```sh
pip install -r requirement.txt
```
This script was tested against python `3.7.2` but should work on all versions of python3

### Example with file as input 
```sh
$ ./client.py -f test_file.csv
{
    "person": [
        {
            "first_name": "John",
            "surname": "Keynes",
            "age": "29",
            "favourite_color": "red",
            "interest": "cricket"
        },
        {
            "first_name": "Sarah",
            "surname": "Robinson",
            "age": "54",
            "favourite_color": "blue",
            "interest": "badminton"
        }
    ]
}
```
**test_file.csv:**
```sh
first_name,surname,age,nationality,favourite_color,interest
John,Keynes,29,British,red,cricket
Sarah,Robinson,54,,blue,badminton
```
In this example, we are passing the filename test_file.csv directly as input by using -f flag. If output option is not specified, JSON is used by default.

File input with xml response:
```xml
$ ./client.py -f test_file.csv -o xml
<?xml version="1.0" ?>
<root>
	<person>
		<item>
			<first_name>John</first_name>
			<surname>Keynes</surname>
			<age>29</age>
			<favourite_color>red</favourite_color>
			<interest>cricket</interest>
		</item>
		<item>
			<first_name>Sarah</first_name>
			<surname>Robinson</surname>
			<age>54</age>
			<favourite_color>blue</favourite_color>
			<interest>badminton</interest>
		</item>
	</person>
</root>
```

### Example passing input directly
```sh
$ ./client.py -i

Enter you data. Once finished press CTRL+d (Mac,Linux), CTRL+z (Windows)

first_name,surname,age,nationality,favourite_color,interest
John,Keynes,29,British,red,cricket
Sarah,Robinson,54,,blue,badminton
{
    "person": [
        {
            "first_name": "John",
            "surname": "Keynes",
            "age": "29",
            "favourite_color": "red",
            "interest": "cricket"
        },
        {
            "first_name": "Sarah",
            "surname": "Robinson",
            "age": "54",
            "favourite_color": "blue",
            "interest": "badminton"
        }
    ]
}
```
In this case the input is passed interactively. Once completed passing the input, press CTRL+d (Mac,Linux) or CTRL+Z (Windows) to submit it.

Similarly pass '-o' flag to get the desired response format

# Running Tests
You can run tests by invoking the following command. Tests are written to validate data with sample input (test_file.csv) and by passing values diretctly to the function for interactive input.
```sh
python -m unittest test -v
```
**Output**
```sh
$ python -m unittest test -v
test_json_direct (test.TestPerson) ... ok
test_json_file (test.TestPerson) ... ok
test_xml_direct (test.TestPerson) ... ok
test_xml_file (test.TestPerson) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```

# Packaging
You can package this script as python package that can be installed using pip. To do so, make sure you have **setuptools** and **whell** installed in your python environment. 
Run the below command to create distributed python package
```sh
python3 setup.py sdist bdist_wheel
```
This will create `wheel` and `gzip` package with the name `embl_ebi_person-0.0.1-py3-none-any.whl` and `embl-ebi-person-0.0.1.tar.gz` inside `/dist` directory

You can then install it using pip by running
```sh
pip install embl-ebi-person-0.0.1.tar.gz
```
(or)
```sh
pip install embl_ebi_person-0.0.1-py3-none-any.whl
```

