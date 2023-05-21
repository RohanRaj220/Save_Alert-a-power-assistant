#include<PZEM004Tv30.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "HTTPSRedirect.h"
PZEM004Tv30 pzem(13,12);

const char* ssid     = "WIFINAME";
const char* password = "WIFI PASSWORD";
// to send the details to google sheets and access the through googlescriptID
const char *GScriptId = "AKfycbz0h87nNvqkONKw7yxLYksKy85KFSLs0og0q2kn9jhzVDV3KT0fQM413ErJzLSOJM987g";


String payload_base =  "{\"command\": \"insert_row\", \"sheet_name\": \"Sheet1\", \"values\": ";
String payload = "";

const char* host = "script.google.com";
const int httpsPort = 443;
const char* fingerprint = "";
String url = String("/macros/s/") + GScriptId + "/exec";
HTTPSRedirect* client = nullptr;

String volt = "";
String curr = "";
String powe = "";
String ener = "";
String freq = "";
String pf = "";

void setup() {

  Serial.begin(9600);        
  delay(10);
  Serial.println('\n');
 
  
  WiFi.begin(ssid, password);            
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());

  
  client = new HTTPSRedirect(httpsPort);
  client->setInsecure();
  client->setPrintResponseBody(true);
  client->setContentTypeHeader("application/json");
 
  Serial.print("Connecting to ");
  Serial.println(host);

  
  bool flag = false;
  for (int i=0; i<5; i++){
    int retval = client->connect(host, httpsPort);
    if (retval == 1){
       flag = true;
       Serial.println("Connected");
       break;
    }
    else
      Serial.println("Connection failed. Retrying...");
  }
  if (!flag){
    Serial.print("Could not connect to server: ");
    Serial.println(host);
    return;
  }
  delete client;    
  client = nullptr; 
}


void loop() {
    float voltag = pzem.voltage();
    float curren = pzem.current();
    float poww = pzem.power();
    float energ= pzem.energy();
    float frequenc= pzem.frequency();
    float pwf= pzem.pf();
    
    if(isnan(voltag)){
      voltag =0;
      curren=0;
      poww=0;
      energ=0;
      frequenc=0;
      pwf=0;
      }
 
  
  volt = String(voltag);
  curr = String(curren);
  powe = String(poww);
  ener = String(energ);
  freq = String(frequenc);
  pf   = String(pwf);
 
 

  static bool flag = false;
  if (!flag){
    client = new HTTPSRedirect(httpsPort);
    client->setInsecure();
    flag = true;
    client->setPrintResponseBody(true);
    client->setContentTypeHeader("application/json");
  }
  if (client != nullptr){
    if (!client->connected()){
      client->connect(host, httpsPort);
    }
  }
  else{
    Serial.println("Error creating client object!");
  }
 
  
  payload = payload_base + "\"" + volt + "," + curr + "," + powe +"," + ener + "," + freq + "," + pf + "\"}";
 
 
  
  Serial.println("Publishing data...");
  Serial.println(payload);
  if(client->POST(url, host, payload)){
    
  }
  else{
    
    Serial.println("Error while connecting");
  }

  // a delay of several seconds is required before publishing again    
  delay(1500);
}