public class Curio : Passaro {
    private float tamanhoBico {get; set;}
    
    public Curio(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado, float velocidadeVoo, float tamanhoBico) : base(nome, dataNascimento, peso, capEstomago, vacinado, velocidadeVoo){
        this.tamanhoBico = tamanhoBico;
    }

    public void Cantar() {
        Console.WriteLine($"O curio {nome} está cantando.");
    }
}