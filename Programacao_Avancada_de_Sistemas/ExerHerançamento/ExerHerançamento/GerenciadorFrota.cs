public class GerenciadorFrota {
    private List<Veiculo> Veiculos {get; set;}

    public GerenciadorFrota(){
        Veiculos = new List<Veiculo>();
    }

    public void AdicionarVeiculo(Veiculo v){
        Veiculos.Add(v);
    }

    public void RealizarMissao(double km) {
        foreach(Veiculo v in Veiculos) {
            v.Mover(km);
        }
    }
}