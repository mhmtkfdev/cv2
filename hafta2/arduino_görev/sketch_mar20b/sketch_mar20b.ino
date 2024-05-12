const int LEDdizisi[] = {2,3,4,5,6};
const int dugme = 7;
int dugme_durumu = 0; 

void setup () {     
 
  for(int i=0; i<5 ;i++)    
  { 
    pinMode(LEDdizisi[i], OUTPUT);
  }
  pinMode(dugme,İNPUT);

}

void loop() 
{ 
  dugme_durumu = digitalRead(dugme);
  if (dugme_durumu == HIGH)
  { 
      digitalWrite(LEDdizisi[i],LOW); 
  }
  else if (dugme_durumu == LOW)
  {
      for(int i=0; i<5; i++){ 
      digitalWrite(LEDdizisi[i],HIGH);      
      delay(250);                           
  }
      for(int i=0; i<5; i++)
  { 
      digitalWrite(LEDdizisi[i],LOW); 
  }
 
      for(int j=4;j>-1; j--)
  { 
      digitalWrite(LEDdizisi[j],HIGH);     
      delay(250);
  }
      for(int j=0; j<5; j++)
  { 
      digitalWrite(LEDdizisi[j],LOW); 
  }
  }                                             

}
