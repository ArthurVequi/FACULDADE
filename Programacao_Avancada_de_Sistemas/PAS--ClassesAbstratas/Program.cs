using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("--- Teste de Animais ---");

        // Instanciando um Cachorro
        Cachorro rex = new Cachorro("Rex", new DateTime(2020, 5, 10), 15.5f, 1.2f, true, 8, "Marrom", "Vira-lata", true);
        Console.WriteLine("\nCriado o cachorro Rex");
        rex.Idade();
        rex.Comer(0.5f);
        rex.Amamentar();

        // Instanciando um Gato
        Gato mingau = new Gato("Mingau", new DateTime(2022, 1, 15), 4.2f, 0.4f, true, 6, "Branco", "Siamês", false);
        mingau.Idade();
        mingau.Comer(0.2f);
        mingau.Amamentar();

        // Instanciando um Gavião
        Gaviao falcao = new Gaviao("Falcão", new DateTime(2018, 3, 22), 2.5f, 0.3f, false, 150f, 1.2f);
        falcao.Idade();
        falcao.Comer(0.1f);
        falcao.Voar();
        falcao.Planar();
        falcao.Cacar(120f);

        // Instanciando um Curió
        Curio piu = new Curio("Piu", new DateTime(2023, 10, 5), 0.1f, 0.05f, true, 40f, 1.5f);
        piu.Idade();
        piu.Comer(0.02f);
        piu.Voar();
        piu.Cantar();
    }
}
