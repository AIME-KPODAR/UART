const int PIN_POT = A0;
const int PIN_LED = 8;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
}

void loop() {
  int valeur = analogRead(PIN_POT);
  Serial.println(valeur);

  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '1') digitalWrite(PIN_LED, HIGH);
    if (c == '0') digitalWrite(PIN_LED, LOW);
  }
  delay(500);
}