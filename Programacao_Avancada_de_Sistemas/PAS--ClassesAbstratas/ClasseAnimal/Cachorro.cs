public class Cachorro : Mamifero {
    private string Raca {get; set;}
    private bool EhCastrado {get; set;}
    
    public Cachorro(string nome, DateTime dataNascimento, float peso, float capEstomago, bool vacinado, int qtdMamas, string corPelos, string raca, bool ehCastrado) : base(nome, dataNascimento, peso, capEstomago, vacinado, qtdMamas, corPelos){
        this.Raca = raca;
        this.EhCastrado = ehCastrado;
    }
}