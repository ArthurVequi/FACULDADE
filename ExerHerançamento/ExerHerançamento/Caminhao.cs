public class Caminhao : Veiculo {
   private double cargaAtual {get; set;}
   public Caminhao(string placa, string modelo) : base(placa, modelo){}

    public override void Mover(double distancia){
        double consumo = (distancia / 5) + (cargaAtual * 0.1);
        if (NivelCombustivel >= consumo){
            NivelCombustivel -= consumo;
            base.Mover(distancia);
            Console.WriteLine($"O Caminhão andou {distancia}km");

        }
        else {
            Console.WriteLine("Combustível insuficiente");
        }
    }
}
