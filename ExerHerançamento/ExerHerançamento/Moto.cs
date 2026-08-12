public class Moto : Veiculo {
    private double limiteDistancia {get; set;}
    public Moto(string placa, string modelo) : base(placa, modelo){
        limiteDistancia = 300;
    }

    public override void Mover(double distancia){
        if (distancia > limiteDistancia)
        {
            Console.WriteLine("Distância excedida");
        } 
        else {
            double consumo = distancia / 25;
            if (NivelCombustivel >= consumo){
                NivelCombustivel -= consumo;
                base.Mover(distancia);
                Console.WriteLine($"A Moto andou {distancia}km");

            }
            else {
                Console.WriteLine("Combustível insuficiente");
            }
        }
    }
}