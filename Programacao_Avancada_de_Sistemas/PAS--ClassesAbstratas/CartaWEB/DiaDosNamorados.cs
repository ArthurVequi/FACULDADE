using System;

public class DiaDosNamorados : CartaoWeb
{
    public DiaDosNamorados(string destinatario) : base(destinatario)
    {
    }

    public override void ExibirMensagem()
    {
        Console.WriteLine($"Feliz Dia dos Namorados, {Destinatario}! Te amo muito!");
    }
}
