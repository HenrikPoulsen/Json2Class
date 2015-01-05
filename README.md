Json2Class
=============
This is a little tool written in Python 2.7 which generates class definitions from json files that are supplied to it.
It also generates functions which can load and save these objects from json strings.

I like to have static typing since it makes it a lot easier to keep track of what is going on and having classes
generated from the same source makes it easier to sync changes between frontend/backend if they use different languages.

## Requirements
You need to have Python 2.7.x and install [enum34](https://pypi.python.org/pypi/enum34) so it can use some proper enums. 

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
#### [java/Generated/Person.java](test/SampleProjects/javaSample/src/Generated/Person.java)


## Info
### C# generated code
This project was initially created because I needed functionality like this for a Unity3D game I am making with a
python backend. But Unity doesn't support Newtonsoft.Json and reflection etc.
So the generated code uses the SimpleJSON implementation located at [Unity3D wiki](http://wiki.unity3d.com/index.php/SimpleJSON).
If you have need for something else feel free to let me know and I can try to add that, or feel free fix it yourself
and make a push request.