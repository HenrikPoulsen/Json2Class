using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Json2Whatever;
using SimpleJSON;

namespace CsSample
{
    class Program
    {
        static void Main(string[] args)
        {
            var myPerson = new Person(SimpleJSON.JSONNode.Parse(File.ReadAllText("..\\..\\..\\..\\jsonSamples\\Person.json")));
            Console.WriteLine(myPerson.Family.Count);

            myPerson.Family.Add(new Person());

            var outJson = myPerson.ToJson();
            Console.WriteLine(outJson.ToString());

            var listSample = new ListSample();
            listSample.ObjectList.Add(new ObjectList{ Name = "Hello"});
            outJson = listSample.ToJson();
            Console.WriteLine(outJson.ToString());
        }
    }
}
