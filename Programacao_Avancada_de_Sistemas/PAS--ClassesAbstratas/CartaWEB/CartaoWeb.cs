using System;

public abstract class CartaoWeb
{
    public string Destinatario { get; protected set; }

    public CartaoWeb(string destinatario)
    {
        Destinatario = destinatario;
    }

    public abstract void ExibirMensagem();
}
