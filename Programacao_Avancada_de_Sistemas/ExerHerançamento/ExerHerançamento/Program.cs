using System;

class Program {
    static void Main(string[] args) {
        GerenciadorFrota frota = new GerenciadorFrota();

        Carro meuCarro = new Carro("ABC-1234", "Sedan");
        Caminhao meuCaminhao = new Caminhao("DEF-5678", "Volvo");
        Moto minhaMoto = new Moto("GHI-9012", "Honda");

        Console.WriteLine("Abastecendo os veiculos");
        meuCarro.Abastecer(100.0);
        meuCaminhao.Abastecer(100.0);
        minhaMoto.Abastecer(50);
        Console.WriteLine("Veiculos abastecidos (100l)\n");

        //nao deve ser possivel abastecer, tanque cheio
        meuCarro.Abastecer(50.0);

        frota.AdicionarVeiculo(meuCarro);
        frota.AdicionarVeiculo(meuCaminhao);
        frota.AdicionarVeiculo(minhaMoto);

        Console.WriteLine("Realizando missão de 50km:");
        frota.RealizarMissao(50);

        Console.WriteLine("\nRealizando missão de 100km");
        frota.RealizarMissao(100);

        //vai acabar o combustivel
        Console.WriteLine("\nRealizando missão de 400km");
        frota.RealizarMissao(400);


    }
}
