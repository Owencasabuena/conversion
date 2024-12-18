from decimal import Decimal

def convert(value, from_unit, to_unit):
    conversions = {
        'km': Decimal(1e3),
        'm': Decimal(1),
        'cm': Decimal(1e-2),
        'mm': Decimal(1e-3)
    }
    
    value = Decimal(value)
    """Convert a value from one metric unit to another."""
    try:
        # Convert to base unit (meters)
        value_in_meters = value * conversions[from_unit]
        
        # Convert from base unit to target unit
        converted_value = value_in_meters / conversions[to_unit]
        return round(converted_value, 3)
    except KeyError:
        raise ValueError("Invalid unit provided for conversion.")
    
def convert_temp(value, from_unit, to_unit):
    try:
        if from_unit == 'C':
            if to_unit == 'K':
                return (value + 273.15)
            elif to_unit == 'F':
                return ((value * 9/5) + 32)
            
        elif from_unit == 'K':
            if to_unit == 'C':
                return (value - 273.15)
            elif to_unit == 'F':
                return (((value - 273.15) * 9/5) + 32)
            
        elif from_unit == 'F':
            if to_unit == 'C':
                return ((value - 32) * 5/9)
            elif to_unit == 'K':
                return (((value - 32) * 5/9) + 32)
            
        raise ValueError("Invalid temperature units provided.")
    except ValueError as e:
        raise ValueError(f"Error in temperature conversion: {e}")