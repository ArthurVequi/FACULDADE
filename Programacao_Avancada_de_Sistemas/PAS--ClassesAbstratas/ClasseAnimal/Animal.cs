public abstract class Animal {
    private string nome {get; set;}
    private DateTime dataNascimento {get; set;}
    private float peso {get; set;}
    private float capEstomago {get; set;}
    private bool vacinado {get; set;}

    public Animal(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado){
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.peso = peso;
        this.capEstomago = capEstomago;
        this.vacinado = vacinado;
    }

    public int Idade() {
        int idade = DateTime.Now.Year - dataNascimento.Year;
        Console.WriteLine("A idade do animal é: " + idade);
        return idade;
    }
    public boolean Comer(float qtd) {
        if(qtd <= 0) {
            Console.WriteLine("Quantidade inválida!");
            return false;
        }
        Console.WriteLine("O animal comeu " + qtd + " kg de comida.");
        return true;
    }
}