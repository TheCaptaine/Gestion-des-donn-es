#define LedBlue 5
char serialData;
int time = 0;

void setup() {
	Serial.begin(9600);
  pinMode(LedBlue, OUTPUT);
  digitalWrite(LedBlue, LOW);
}

void loop() {
	Serial.println(String(analogRead(A0))+";"+String(time));
	delay(1000);
	time += 1;
	Serial.flush();
  led_on();
}

void led_on() {
    serialData = Serial.read();
    
    if (serialData == '1') {
      digitalWrite(LedBlue, HIGH);
    }
    else if (serialData == '0') {
      digitalWrite(LedBlue, LOW);
    }
}

