using System.Data;
using System.Diagnostics;
using System.Net;


Console.WriteLine("Quantos graus fazem hoje? (Em Celcius) ");
double graus = Convert.ToDouble(Console.ReadLine());
while (graus != 0) {
    Console.WriteLine("\n1 - Kelvin;\n 2 - Fahrenheit\n 3 - Rankine;\n 4 - TODOS;\n 0 - PARA SAIR\n Digite sua opção: ");
    int escolha = Convert.ToInt32(Console.ReadLine());
    Console.Clear();
    Console.WriteLine($"{graus} GRAUS CELCIUS");
    switch (escolha)
    {
        case 1:
            Console.WriteLine("Você escolheu Kelvin!");
            graus += 273.13f;
            Console.WriteLine($"Fazem {graus.ToString("F3")} graus Kelvin");
            break;
        case 2:
            Console.WriteLine("Você escolheu Fahrenheit!");
            graus += 1.8f + 32;
            Console.WriteLine($"Fazem {graus.ToString("F3")} graus Fahrenheit");
            break;
        case 3:
            Console.WriteLine("Você escolheu Rankine!");
            graus += 9 / 5f + 491.67f;
            Console.WriteLine($"Fazem {graus.ToString("F3")} graus Rankine");
            break;
        case 4:
            Console.WriteLine("Você escolheu TODOS!");
            double fire = graus += 1.8f + 32;
            double kelv = graus += 273.13f;
            double rank = graus += 9 / 5f + 491.67f;
            Console.WriteLine($"Fazem {rank.ToString("F3")} graus em Rankine,\n {fire.ToString("F3")} Fahrenheit,\n {kelv.ToString("F3")} Kelvin e\n {graus.ToString("F3")} Celcius! ");
            break;
    }
}
