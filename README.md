# Temperature Converter

A simple Python class to convert temperatures between Celsius and Fahrenheit.

## Table of Contents

- [Introduction](#temperature-converter)
- [Usage](#usage)
- [Methods](#methods)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Temperature Converter class is designed to convert temperatures between Celsius and Fahrenheit.

## Usage

To use the Temperature Converter class, create an instance and call the `receive_temp_to_convert` method to input the temperature value and the unit to convert. The conversion methods `celsius_to_fahrenheit` and `fahrenheit_to_celsius` perform the actual temperature conversion.

## Methods

### `receive_temp_to_convert()`

Receives input for temperature and unit to convert, and performs the conversion.

### `celsius_to_fahrenheit()`

Converts Celsius to Fahrenheit.

### `fahrenheit_to_celsius()`

Converts Fahrenheit to Celsius.

## Example

```python
from temperature_converter import TEMPERATURE_CONVERTER

temperature_converter = TEMPERATURE_CONVERTER()

while True:
    temperature_converter.receive_temp_to_convert()

    another_temp_to_convert = input("Do you want to convert another? ").lower()

    if another_temp_to_convert == "n" or another_temp_to_convert == "no":
        break

```
