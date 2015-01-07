using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Generated;
using SimpleJSON;

namespace CsSample
{
    class Program
    {
        static void Main(string[] args)
        {
            var myPerson = Person.NewtonsoftFactory.FromJson(File.ReadAllText("..\\..\\..\\..\\jsonSamples\\Person.json"));
            Console.WriteLine(myPerson.Family.Count);

            myPerson.Family.Add(new Person());

            var outJson = Person.SimpleJsonFactory.ToJson(myPerson);
            Console.WriteLine(outJson.ToString());

            var listSample = new ListSample();
            listSample.ObjectList.Add(new ObjectList{ Name = "Hello"});
            outJson = ListSample.SimpleJsonFactory.ToJson(listSample);
            Console.WriteLine(outJson.ToString());
        }
    }
}
