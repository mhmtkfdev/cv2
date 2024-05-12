const int LEDdizisi[] = {2,3,4,5,6};

void setup () {     
 
  for(int i=0; i<5 ;i++)    
  { 
    pinMode(LEDdizisi[i], OUTPUT); 
  }

}

void loop() 
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
