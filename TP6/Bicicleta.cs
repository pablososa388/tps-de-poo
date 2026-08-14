using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace TP6
{
    internal class Bicicleta : IImpactoEcologico
    {
        public Bicicleta(string marca, float rodado, string tipo)
        {
            this.Marca = marca;
            this.Rodado = rodado;
            this.Tipo = tipo;


            
        }
        public string Marca { get; set; }
        public float Rodado { get; set; }
        public string Tipo { get; set; }

        public override string ToString()
        {
            return $"Marca: {Marca}, Rodado: {Rodado}, Tipo:{Tipo}";
        }

        
        public string ObtenerImpactoEcologico()
        {
            return "impacto de la bicicleta: 0kg CO2, es despreciable";
        }

    }
}
