public class Mamifero : Animal {
    private int qtdMamas {get; set;}
    private string corPelos {get; set;}
    
    public Mamifero(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado, int qtdMamas, string corPelos) : base(nome, dataNascimento, peso, capEstomago, vacinado){
        this.qtdMamas = qtdMamas;
        this.corPelos = corPelos;
    }
    public void Amamentar() {
        Console.WriteLine("O mamifero " + nome + " está amamentando.");
    }
}