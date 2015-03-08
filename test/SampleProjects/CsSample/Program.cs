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
            var listSample = new ListSample();
            listSample.ObjectList.Add(new ObjectList{ Name = "Hello"});
        }
    }
}
