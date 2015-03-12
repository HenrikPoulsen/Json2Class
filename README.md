Json2Class
=============
This is a little tool written in Python 2.7 which generates class definitions from json files that are supplied to it.
It also generates functions which can load and save these objects from json strings.

I like to have static typing since it makes it a lot easier to keep track of what is going on and having classes
generated from the same source makes it easier to sync changes between frontend/backend if they use different languages.

If you make changes to the code I would love it if you submit a pull request so I can take in any improvements or fixes.

## Requirements
View [Getting Started](GettingStarted.md) for requirements and more details into how the tool is used

## Example
### Commandline
    Json2Class.py Person.json --cs-out cs/Generated --py-out py/Generated --java-out java/Generated --namespace Generated
### Person.json
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
### Results in
#### [cs/Generated/Person.cs](test/SampleProjects/CsSample/Generated/Person.cs)
#### [py/Generated/person.py](test/SampleProjects/PySample/Generated/person.py)
#### [java/Generated/Person.java](test/SampleProjects/javaSample/src/main/java/Generated/Person.java)
#### See [Getting Started](GettingStarted.md) for more information
