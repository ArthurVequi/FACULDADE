char n = ' ';
unsigned long tempoAnterior = 0;
const long intervalo = 1000;
char Ultimo = ' ';
char stop = ' ';

const int velocidadeMaxima = 255;
const int velocidadeCurva = 255;

void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  unsigned long tempoAtual = millis();

  if (Serial.available() > 0) {
    stop = 'n';
    n = Serial.read();

    // Atualiza o último comando se for um comando válido
    if (n == '1' || n == '2' || n == '3' || n == '4') {
      tempoAnterior = tempoAtual;
      Ultimo = n;
    }
  }

  // Se passou 1 segundo (1000ms) desde o último comando, parar o robô por segurança
  if (((tempoAtual - tempoAnterior) >= intervalo) && stop == 'n') {
    tempoAnterior = tempoAtual;
    stop = 's';
    Parar();
  }

  // Executa a ação do último comando recebido caso não esteja parado
  if (stop == 'n') {
    switch (Ultimo) {
      case '1': // Frente
        Frente();
        break;
      case '2': // Ré
        Re();
        break;
      case '3': // Esquerda
        Esq();
        break;
      case '4': // Direita
        Dir();
        break;
    }
  }
}

void Frente() {
  analogWrite(6, velocidadeMaxima);
  digitalWrite(5, LOW);
  analogWrite(10, velocidadeMaxima);
  digitalWrite(11, LOW);
}

void Re() {
  digitalWrite(6, LOW);
  analogWrite(5, velocidadeMaxima);
  digitalWrite(10, LOW);
  analogWrite(11, velocidadeMaxima);
}

void Esq() {
  digitalWrite(6, LOW);
  analogWrite(5, velocidadeCurva);
  analogWrite(10, velocidadeCurva);
  digitalWrite(11, LOW);
}

void Dir() {
  analogWrite(6, velocidadeCurva);
  digitalWrite(5, LOW);
  digitalWrite(10, LOW);
  analogWrite(11, velocidadeCurva);
}

void Parar() {
  digitalWrite(6, LOW);
  digitalWrite(5, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
}
