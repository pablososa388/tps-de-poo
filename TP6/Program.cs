using System;
using System.Collections.Generic;
using System.Text;
namespace TP6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Auto a1= new Auto("Chevrolet", "Agile", 2010, 10000, 8);
            Auto a2 = new Auto("Ford", "Fiesta", 2011, 154000, 9);
            Edificio ed1 = new Edificio("Edificio 1", "Calle Falsa 123", 5, 10);
            Bicicleta b1 = new Bicicleta("Bianchi",20, "Sprint");



            List<IImpactoEcologico> elementos= new List<IImpactoEcologico>();

            elementos.Add(a2);
            elementos.Add(a1);
            elementos.Add(ed1);
            elementos.Add(b1);
           
            foreach (IImpactoEcologico e in elementos)
            {
               Console.WriteLine(e.ToString() +" "+ e.ObtenerImpactoEcologico());
            }

            Console.ReadKey();


        }
    }
}
