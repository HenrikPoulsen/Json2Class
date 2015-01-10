# Getting Started
## Setting up Json2Class
1. Install Python 2.7.x
2. Install [enum34](https://pypi.python.org/pypi/enum34)
3. Download Json2Class and place it wherever
4. Run Json2Class.py with your Python 2.7.x binary

## Generated code requirements
Currently the code generated will depend on the following 3rd party libraries.

### CSharp
Requires [Unity3D SimpleJSON.cs](http://wiki.unity3d.com/index.php/SimpleJSON)

### Java
Requires [json-simple](https://code.google.com/p/json-simple/)

### Python
Uses the built in json module, so you shouldn't have to do anything here hopefully

## Command line examples
Here are some examples for generating classes in the different supported languages.
In each case it will create one class called Person with language appropriate naming conventions like:

* C# = Person.cs
* Java = Person.java
* Python = person.py

### Basic usage
#### Generating C# class
    Java2Class --cs-out csProject/GeneratedClasses Person.json
#### Generating Java class
    Java2Class --java-out javaProject/GeneratedClasses Person.json
#### Generating Python class
    Java2Class --py-out pythonProject/GeneratedClasses Person.json
    
#### Everything at once
    Java2Class --py-out pythonProject/GeneratedClasses --cs-out csProject/GeneratedClasses --java-out javaProject/GeneratedClasses Person.json
    
### Custom Namespace
Default the tool will generate classes in the Json2Class namespace. If you want to override it use --namespace

<pre>Java2Class Java2Class <b>--namespace Generated</b> --py-out pythonProject/GeneratedClasses --cs-out csProject/GeneratedClasses --java-out javaProject/GeneratedClasses Person.json</pre>

This will generate:
 Person.cs with 
    namespace Generated {}
 Person.java with
   package Generated;
 
 person.py is unchanged since python bases namespace upon the file location.
 
### Hinting the tool about the Json object
If we take a look into Person.json we can see some entries that start with @.

    {
        "name": "Incognito",
        "age": 32,
        "country": "Sweden",
        "family": [{
                    "@name": "Person",
                    "@skip_generate": "",
                    "name": "Mom",
                    "age": 57,
                    "country": "Sweden",
                    "family": []
                },
                {
                    "@name": "Person",
                    "@skip_generate": "",
                    "name": "Dad",
                    "age": 65,
                    "country": "Sweden",
                    "family": []
            }]
    }
    
"@name": "Person" hints to the generator that the object it finds is of the type Person.
So in the generated C# code for example it will generate:

    public List<Person> Family {get; set;}
Without the hinting it would just assume the object type is Family and generate a Family.cs as well which would be incorrect in this case.

"@skip_generate" hints that this object should not be generated since it has already been generated before.

That way you can remove redundant information from the json template file.

    {
        "name": "Incognito",
        "age": 32,
        "country": "Sweden",
        "family": [{
                    "@name": "Person",
                    "@skip_generate": ""
                }]
    }
    
The above json would generate the exact same class results as the previous example.
