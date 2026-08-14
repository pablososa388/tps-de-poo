using System;
using System.Collections.Generic;
using System.Text;

namespace TP6
{
    internal class Edificio : IImpactoEcologico
    {
        public Edificio(string nombre, string direccion, int cantPisos, float consumoGasXmt3piso)
        {
            this.Nombre = nombre;
            this.Direccion = direccion;
            this.CantPisos = cantPisos;
            this.ConsumoGasXmt3piso=consumoGasXmt3piso;
        }
        public string Nombre { get; set; }
        public string Direccion { get; set; }
        public int CantPisos { get; set; }  
        public float ConsumoGasXmt3piso { get; set; }


        public string ObtenerImpactoEcologico()
        {
            // 2 = factor de emisión aproximado, kg CO2 por m3 de gas natural
          float impacto= (float)(CantPisos * ConsumoGasXmt3piso * 2);
            return "impacto del edificio: "+impacto+ "kg CO2"; 
        }
        public override string ToString()
        {
            return $"Nombre: {Nombre}, Dirección: {Direccion}, Cantidad de pisos: {CantPisos}, Consumo por metro cúbico: {ConsumoGasXmt3piso}";
        }
    }
}
