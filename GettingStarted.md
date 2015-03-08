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
    Json2Class --cs-out csProject/GeneratedClasses Person.json
#### Generating Java class
    Json2Class --java-out javaProject/GeneratedClasses Person.json
#### Generating Python class
    Json2Class --py-out pythonProject/GeneratedClasses Person.json
    
#### Everything at once
    Json2Class --py-out pythonProject/GeneratedClasses --cs-out csProject/GeneratedClasses --java-out javaProject/GeneratedClasses Person.json
    
### Custom Namespace
Default the tool will generate classes in the Json2Class namespace. If you want to override it use --namespace

<pre>Json2Class <b>--namespace Generated</b> --py-out pythonProject/GeneratedClasses --cs-out csProject/GeneratedClasses --java-out javaProject/GeneratedClasses Person.json</pre>

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
      "isHuman": true, // Always use camelCase and Json2Class will convert it to the appropriate case for the given language
      "gender": {
        "@type": "enum",
        "unspecified": 0,
        "male": 1,
        "female": 2
      },
      "family": [
        {
          "@name": "Person",
          "@skipGenerate": "", 
          "name": "Mom",
          "age": 57,
          "country": "Sweden",
          "isHuman": true,
          "gender": { "@type": "enum", "@skipGenerate": ""},
          "family": []
        },
        {
          "@name": "Person", 
          "@skipGenerate": "",
        }
      ]
    }
    
"@name": "Person" hints to the generator that the object it finds is of the type Person.
So in the generated C# code for example it will generate:

    public List<Person> Family {get; set;}
Without the hinting it would just assume the object type is Family and generate a Family.cs as well which would be incorrect in this case.

"@skipGenerate" hints that this object should not be generated since it has already been generated before.

That way you can remove redundant information from the json template file.

    {
      "name": "Incognito",
      "age": 32,
      "country": "Sweden",
      "isHuman": true,
      "gender": {
        "@type": "enum",
        "unspecified": 0,
          "male": 1,
          "female": 2
        },
        "family": [{
          "@name": "Person",
          "@skipGenerate": ""
        }]
    }
    
The above json would generate the exact same class results as the previous example.

Another hint available is for when you want to send an enum. You could of course just send an integer and then
keep track of what 17 means and remember to update it in all places at the same time, or you can just let Json2Class
manage that for you.

So if we look at the following section from the earlier example you can see how this is done

    "gender": {
      "@type": "enum",
      "unspecified": 0,
      "male": 1,
      "female": 2
    }

"@type": "enum" hints that this object is an enum and all the fields in it represents the different enum values
so this will generate an enum in all the languages you generate it to where Unspecified = 1, Male = 2 etc.