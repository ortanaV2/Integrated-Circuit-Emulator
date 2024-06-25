#include <Arduino.h>

const int auto_clk_pin = 5;       // GPIO5 -> D1
const int clk_pin = 2;            // GPIO2 -> D4
const int serial_output_pin = 0;  // GPIO0 -> D3
const int true_output_pin = 4;    // GPIO4 -> D2

String bin_data;
int bin_data_len;
int data_state = 0;

bool reset_button = false;
int clock_count = 0;
float clock_speed = 500; // in milliseconds

void setup() {
  pinMode(auto_clk_pin, OUTPUT);
  pinMode(clk_pin, INPUT);
  pinMode(serial_output_pin, OUTPUT);
  pinMode(true_output_pin, OUTPUT);

  // Initialize output pins
  digitalWrite(true_output_pin, LOW);
  digitalWrite(serial_output_pin, LOW);

  // Read binary data from file (simulated as a string for simplicity)
  bin_data = "11001010"; // Replace with your actual binary data
  bin_data_len = bin_data.length();

  Serial.begin(115200);
}

void loop() {
  clock_count++;

  if (clock_count % 2 == 0) {
    digitalWrite(auto_clk_pin, HIGH);
  } else {
    digitalWrite(auto_clk_pin, LOW);
  }

  if (digitalRead(clk_pin) == LOW && !reset_button) {
    reset_button = true;
    Serial.print("CLK - Request: ");
    Serial.println(clock_count);

    if (data_state != bin_data_len) {
      digitalWrite(true_output_pin, HIGH);
      digitalWrite(serial_output_pin, bin_data[data_state] == '1' ? HIGH : LOW);
      data_state++;
      Serial.println("Send bit");
    } else {
      digitalWrite(true_output_pin, LOW);
      digitalWrite(serial_output_pin, LOW);
    }
  }

  if (digitalRead(clk_pin) == HIGH && reset_button) {
    reset_button = false;
  }

  delay(clock_speed);
}
