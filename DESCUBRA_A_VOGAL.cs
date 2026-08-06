char[] vogais = { 'a','e','i','o','u' };
char certo = 'n';
while (true) {
    Console.WriteLine("Insira uma Letra:");
    char letraEscolhida = char.Parse(Console.ReadLine());
    for (int i = 0; i < 5; i++)
    {
        if (letraEscolhida == vogais[i])
        {
            certo = 's';
            break;
        }
    }
    if (certo == 's')
    {
        break;
    }
    else
    {
        Console.Clear();
        Console.WriteLine("Voce Errou! Tente Novamente");
        continue;
    }
}
Console.WriteLine("Parabens voce acertou a vogal!");