public class Veiculo{
    protected string Placa {get; set;}
    protected string Modelo {get; set;}
    protected double NivelCombustivel {get; set;}
    protected double CapacidadeTanque {get; set;}
    protected List<string> LogViagens { get; set; }

    public Veiculo(string placa, string modelo){
        Placa = placa;
        Modelo = modelo;
        CapacidadeTanque = 100; 
        NivelCombustivel = 0; 
        LogViagens = new List<string>();
    }

    public void Abastecer(double litros){
        if (litros + NivelCombustivel <= CapacidadeTanque){
            NivelCombustivel += litros;
        }
        else {
            Console.WriteLine("Não é possível abastecer, o veículo está cheio");
        }
    }
    public virtual void Mover(double distancia){
        LogViagens.Add($"Veículo percorreu {distancia} km.");
    }
}
            