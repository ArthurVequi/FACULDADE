using System.ComponentModel.Design;

Console.WriteLine("Digite sua primeira nota: ");
double n1 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Digite sua primeira nota: ");
double n2 = Convert.ToDouble(Console.ReadLine());
double soma = (n1 + n2)/2;

if (soma > 7)
{
    Console.WriteLine("Aprovado");
}
if (soma < 7 && soma > 3)
{
    Console.WriteLine("Prova final");
    Console.WriteLine("Digite sua nota da prova final: ");
    double novaNota = Convert.ToDouble(Console.ReadLine());
    soma += novaNota / 2;
    if (soma > 5)
    {
        Console.WriteLine("Aprovado");
    }
    else
    {
        Console.WriteLine("Reprovado");
    }
else {
        Console.WriteLine("Reprovado sem direito a prova final");
    }

