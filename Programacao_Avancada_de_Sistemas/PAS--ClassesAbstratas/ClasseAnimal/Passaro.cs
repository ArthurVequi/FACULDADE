public class Passaro : Animal {
    private float velocidadeVoo {get; set;}
    
    public Passaro(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado, float velocidadeVoo) : base(nome, dataNascimento, peso, capEstomago, vacinado){
        this.velocidadeVoo = velocidadeVoo;
    }

    public void Voar() {
        Console.WriteLine("O pássaro " + nome + " está voando a " + velocidadeVoo + " km/h.");
    }
}