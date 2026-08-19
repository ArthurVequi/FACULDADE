public class Carro : Veiculo {
    public Carro(string placa, string modelo) : base(placa, modelo) {}

    public override void Mover(double distancia) {
        double consumo = distancia / 10.0;

        if (NivelCombustivel >= consumo) {
            NivelCombustivel -= consumo;
            base.Mover(distancia);
            Console.WriteLine($"O Carro andou {distancia}km");
        } else {
            Console.WriteLine("Combustível insuficiente.");
        }
    }
}