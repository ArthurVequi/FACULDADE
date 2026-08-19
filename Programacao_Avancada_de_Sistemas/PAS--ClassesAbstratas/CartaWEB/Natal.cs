using System;

public class Natal : CartaoWeb
{
    public Natal(string destinatario) : base(destinatario)
    {
    }

    public override void ExibirMensagem()
    {
        Console.WriteLine($"Feliz Natal, {Destinatario}! Que seu Natal seja repleto de alegria e paz.");
    }
}
