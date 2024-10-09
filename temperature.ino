float temp; //variable to hold temperature sensor value
float tem=100;

void setup()
{
  Serial.begin(9600);
  pinMode(0,INPUT);//temperature sensor connected to analog 0
  analogReference(DEFAULT);
  for(int i=0;i<=10;i++)
  {
   temp = analogRead(0); //analog reading temperature sensor values
   temp= temp* 0.48828125;
   Serial.flush();
   
   Serial.print("trail no: ");
   Serial.println(i);
   Serial.println(temp);
   //printing temperature sensor values
   if (tem > temp)
   {
    
    if (i!=0)
    {
      Serial.print("temperature is ");
      Serial.println(tem);
      Serial.println("fertile");
      break;
    }
  }
   else if (temp>tem && i==10)
   {
    Serial.println("infertile");
   }
   delay(5000);//delay of 5 seconds
   tem=temp;
  }
}
