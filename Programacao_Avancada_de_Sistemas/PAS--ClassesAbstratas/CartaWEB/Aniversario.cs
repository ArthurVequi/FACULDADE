using System;

public class Aniversario : CartaoWeb
{
    public Aniversario(string destinatario) : base(destinatario)
    {
    }

    public override void ExibirMensagem()
    {
        Console.WriteLine($"Feliz Aniversário, {Destinatario}! Muitos anos de vida e felicidades.");
    }
}
