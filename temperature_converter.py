class TEMPERATURE_CONVERTER:
    def __init__(self):
        self.tempToConvert = 0

    def receive_temp_to_convert(self):
        self.to_convert = input("Do you want to convert to Celsius or Fahrenheit? ").lower()
        try:
            self.tempToConvert = float(input(f"What is the number in {self.to_convert}? "))
            if self.to_convert == "celsius":
                result = self.celsius_to_fahrenheit()
                print(result)
            elif self.to_convert == "fahrenheit":
                result = self.fahrenheit_to_celsius()
                print(result)
            else:
                self.to_convert = input("Enter Celsius or Fahrenheit: ")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for temperature. ")


    def celsius_to_fahrenheit(self):
        fahrenheit = 9 / 5 * self.tempToConvert + 32
        return f"{self.tempToConvert} Celsius is {fahrenheit} Fahrenheit."

    def fahrenheit_to_celsius(self):
        celsius = 5 / 9 * (self.tempToConvert - 32)
        return f"{self.tempToConvert} Fahrenheit is {celsius} Celsius."
    
temperature_converter = TEMPERATURE_CONVERTER()

while True:
    temperature_converter.receive_temp_to_convert()

    another_temp_to_convert = input("Do you want to convert another? ").lower()
    
    if another_temp_to_convert == "n" or another_temp_to_convert == "no":
        break
