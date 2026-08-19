using System;

class Program
{
    static void Main(string[] args)
    {
        // Criação de um vetor (array) de CartaoWeb com 3 posições
        CartaoWeb[] cartoes = new CartaoWeb[3];

        // Inserindo as instâncias dos 3 tipos de cartões
        cartoes[0] = new DiaDosNamorados("Maria");
        cartoes[1] = new Natal("João");
        cartoes[2] = new Aniversario("Carlos");

        // Usando um laço for para exibir as mensagens
        Console.WriteLine("--- Exibindo os Cartões ---");
        for (int i = 0; i < cartoes.Length; i++)
        {
            cartoes[i].ExibirMensagem();
            Console.WriteLine("---------------------------");
        }
    }
}
