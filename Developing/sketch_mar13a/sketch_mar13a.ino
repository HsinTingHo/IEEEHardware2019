int data; //python input
int trigPin = 11;
int echoPin = 12;
long distance;

long getDistance(int data, int trigPin, int echoPin){
  long duration, cm, inches;
  if(data == 48){//when input is 0, somehow arduino shows 48
     digitalWrite(trigPin, LOW);
     delayMicroseconds(5);
     digitalWrite(trigPin, HIGH);
     delayMicroseconds(10);
     digitalWrite(trigPin, LOW);

     pinMode(echoPin, INPUT);
     duration = pulseIn(echoPin, HIGH);

     //cm = (duration/2) / 29.1;
     inches = (duration/2) / 74;
  }
 
  return inches;
}

//return true when an object is within 3 inches
bool withinDistance(long d){
  long inches = 3;
  bool result;
    if(d < inches){
      result = true;
    }   
    else{
      result = false;
    }
    return result;
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {

  while(Serial.available()){
    data = Serial.read(); //Get the input from python   
    distance = getDistance(data, trigPin, echoPin);
    Serial.print(distance);

    
  }
  

  delay(20);
  
  
}
