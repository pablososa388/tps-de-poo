using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Text;

namespace TP6
{
    internal class Auto : IImpactoEcologico
    {
        public Auto(string marca, string modelo, int anio, float kmRecorridos, float consumoX100km)
        {
            this.Marca = marca;
            this.Modelo = modelo;
            this.Anio = anio;
            this.KmRecorridos = kmRecorridos;
            this.ConsumoX100km = consumoX100km;
        }
        public string Marca { get; set; }
        public string Modelo { get; set; }
        public int Anio { get; set; }
        public float KmRecorridos { get; set; }
        public float ConsumoX100km { get; set; }

        public string ObtenerImpactoEcologico()
        {
            
            float totales = (float)(((KmRecorridos / 100) * ConsumoX100km)*2.3);
            return "impacto del auto: " + totales + "kg CO2";
        }
        public override string ToString()
        {
            return "Marca: " + Marca + ", Modelo: " + Modelo + ", Año: " + Anio + ", Km Recorridos: " + KmRecorridos + ", Consumo por 100km: " + ConsumoX100km;
        }
    }
}