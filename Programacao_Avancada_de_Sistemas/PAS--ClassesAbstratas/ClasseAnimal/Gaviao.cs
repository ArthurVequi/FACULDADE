public class Gaviao : Passaro {
    private float envergaduraAsas {get; set;}
    
    public Gaviao(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado, float velocidadeVoo, float envergaduraAsas) : base(nome, dataNascimento, peso, capEstomago, vacinado, velocidadeVoo){
        this.envergaduraAsas = envergaduraAsas;
    }

    public void Planar() {
        Console.WriteLine($"O gaviao {nome} está planando");
    }

    public void Cacar(float velocidadeVoo) {
        Console.WriteLine($"O gaviao {nome} está caçando a {velocidadeVoo} km/h.");
    }