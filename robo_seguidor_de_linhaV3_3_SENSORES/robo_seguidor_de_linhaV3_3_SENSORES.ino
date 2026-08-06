  // Definição das portas da ponte H
  const int in1 = 5;
  const int in2 = 6; //pwm // MOTOR DIREITO

  const int in3 = 9; //pwm // MOTOR ESQUERDO
  const int in4 = 10;

  // Definição das portas dos sensores infravermelhos
  const int pinSensorEsq = A2;
  const int pinSensorDir = A0;
  const int pinSensorCent = A1;

  // Definição das velocidades
  const int velocidadeMaxima = 40;
  const int velocidadeCurva = 20;

  void setup() {
    // Configuração das portas da ponte H como saídas
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);
    
    // Configuração das portas dos sensores como entradas
    pinMode(pinSensorEsq, INPUT_PULLUP);
    pinMode(pinSensorDir, INPUT_PULLUP);
    pinMode(pinSensorCent, INPUT_PULLUP);
  }

  void loop() {
    // Leitura dos sensores
    int leituraEsquerda = digitalRead(pinSensorEsq);
    int leituraDireita = digitalRead(pinSensorDir);
    int leituraCentro = digitalRead(pinSensorCent);

    // Caso o sensor do centro detecte a linha
    if (leituraCentro == LOW && leituraEsquerda == HIGH && leituraDireita == HIGH) {
      andarParaFrente();
    }
    // Caso os três sensores detectem a linha
    else if (leituraCentro == LOW && leituraEsquerda == LOW && leituraDireita == LOW) {
      andarParaFrente();
    }
    // Caso o sensor da esquerda detecte a linha
    else if (leituraCentro == LOW && leituraEsquerda == LOW && leituraDireita == HIGH) {
      virarEsquerda();
    }
    // Caso o sensor da direita detecte a linha
    else if (leituraCentro == LOW && leituraEsquerda == HIGH && leituraDireita == LOW) {
      virarDireita();
    }
    // Caso nenhum sensor detecte a linha
    else {
      parar();
    }
    delay(10);
  }

  void andarParaFrente() {
    //motor ESQUERDO  
    analogWrite(in2, velocidadeMaxima);
    digitalWrite(in1, LOW);
    
    //motor DIREITO
    analogWrite(in3, velocidadeMaxima);
    digitalWrite(in4, LOW);
  }

  void virarEsquerda() {
    //motor ESQUERDO
    digitalWrite(in4, LOW);
    analogWrite(in3, velocidadeCurva);

    //motor DIREITO (reduzindo a velocidade do motor direito para virar)
    digitalWrite(in1, LOW);
    analogWrite(in2, velocidadeMaxima);
  }

  void virarDireita() { 
    //motor ESQUERDO (reduzindo a velocidade do motor esquerdo para virar)
    analogWrite(in3, velocidadeMaxima);
    digitalWrite(in4, LOW);

    //motor DIREITO
    digitalWrite(in1, LOW);
    analogWrite(in2, velocidadeCurva);
  }

  void parar() {
    //motor ESQUERDO
    digitalWrite(in1, LOW);
    analogWrite(in2, 0);

    //motor DIREITO
    analogWrite(in3, 0);
    digitalWrite(in4, LOW);
  }
