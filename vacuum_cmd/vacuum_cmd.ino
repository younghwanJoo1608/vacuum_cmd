#include <ros.h>
#include <std_msgs/Int32MultiArray.h>
#include <stdlib.h>

ros::NodeHandle nh;

// Solenoid valve pin number
unsigned int pin_num[6] = { 5, 3, 9, 6, 11, 10 };

void VacuumCallback( const std_msgs::Int32MultiArray& cmd_msg){
  for (int i = 0; i < cmd_msg.data_length; i++){
    if (!cmd_msg.data[i])
      digitalWrite(pin_num[i], LOW);
    else
      digitalWrite(pin_num[i], HIGH);    
  }
}

ros::Subscriber<std_msgs::Int32MultiArray> sub("/unld/vacuum_cmd", &VacuumCallback);

void setup() {

  for (auto i : pin_num){
    pinMode(i, OUTPUT);
  }
  nh.initNode();
  delay(1);
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
