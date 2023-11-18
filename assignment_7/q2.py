from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod
    def drive(self, dist):
        pass

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if isinstance(gas_capacity, (int, float)) and isinstance(gas_per_100km, (int, float)):
            if gas_capacity > 0 and gas_per_100km > 0:
                self.gas_capacity = gas_capacity
                self.gas_per_100km = gas_per_100km
                self.gas_max_capacity = gas_capacity
            else:
                raise Warning("Negative numbers are not accepted!")
        else:
            raise Warning("Only numbers are accepted!")

    def fuel(self, f):
        if self.gas_capacity + f > self.gas_max_capacity:
            self.gas_capacity = 0
            raise Warning("The gas tank has been overfilled!")
        else:
            self.gas_capacity += f

    def get_gas_tank_status(self):
        return (round(self.gas_capacity, 1), round(self.gas_max_capacity, 1))

    def get_remaining_range(self):
        return self.gas_capacity / self.gas_per_100km  * 100

    def drive(self, dist):
        if isinstance(dist, float) or isinstance(dist, int):
            if dist < 0:
                raise Warning("Negative numbers are not accepted!")
            used_gas = dist * self.gas_per_100km / 100
            if used_gas > self.gas_capacity:
                self.gas_capacity = 0
                raise Warning("Fuel is depleted")
            else:
                self.gas_capacity -= used_gas
        else:
            raise Warning("Only numbers are accepted!")

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if isinstance(battery_size, (int, float)) and isinstance(battery_range_km, (int, float)):
            if battery_size > 0 and battery_range_km > 0:
                self.battery_size = battery_size
                self.battery_range_km = battery_range_km
                self.max_battery_size = battery_size
            else:
                raise Warning("Negative numbers are not accepted!")
        else:
            raise Warning("Only numbers are accepted!")

    def charge(self, kwh):
        if self.battery_size + kwh > self.max_battery_size:
            self.battery_size = 0
            raise Warning("Overcharged!")
        else:
            self.battery_size += kwh    

    def get_battery_status(self):
        return (round(self.battery_size, 1), round(self.max_battery_size, 1))

    def get_remaining_range(self):
        return self.battery_range_km / self.max_battery_size * self.battery_size

    def drive(self, dist):
        if isinstance(dist, float) or isinstance(dist, int):
            if dist < 0:
                raise Warning("Negative numbers are not accepted!")
            used_battery = dist / self.battery_range_km * self.max_battery_size
            if used_battery > self.battery_size:
                self.battery_size = 0
                raise Warning("Electricity depleted!")
            else:
                self.battery_size -= used_battery
        else:
            raise Warning("Only numbers are accepted!")

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if isinstance(gas_capacity, (int, float)) and isinstance(gas_per_100km, (int, float)) and isinstance(battery_size, (int, float)) and isinstance(battery_range_km, (int, float)):
            if gas_capacity > 0 and gas_per_100km > 0 and battery_size > 0 and battery_range_km > 0:
                CombustionCar.__init__(self, gas_capacity, gas_per_100km)
                ElectricCar.__init__(self, battery_size, battery_range_km)
                self.current_mode = 'electric'
            else:
                raise Warning("Negative numbers are not accepted!")
        else:
            raise Warning("Only numbers are accepted!")

    def switch_to_combustion(self):
        self.current_mode = 'combustion'
        print("Switched to combustion mode.")

    def switch_to_electric(self):
        self.current_mode = 'electric'
        print("Switched to electric mode.")

    def get_remaining_range(self):
        combustion_range = CombustionCar.get_remaining_range(self)
        electric_range = ElectricCar.get_remaining_range(self)
        return combustion_range + electric_range

    def drive(self, dist):
        if isinstance(dist, float) or isinstance(dist, int):
            if dist < 0:
                raise Warning("Negative numbers are not accepted!")
            
            if self.current_mode is None:
                raise Warning("Mode is not selected")
            
            if self.current_mode == 'combustion':
                try:
                    combustion_drive_range = CombustionCar.get_remaining_range(self)
                    CombustionCar.drive(self, dist)
                except Warning as e:
                    remaining_distance = dist - combustion_drive_range
                    if self.battery_size == 0:
                        raise Warning("Both Electricity and Combustion Fuels are out!")
                    self.switch_to_electric()  
                    self.drive(remaining_distance) 
            elif self.current_mode == 'electric':
                try:
                    electric_drive_range = ElectricCar.get_remaining_range(self)
                    ElectricCar.drive(self, dist)
                except Warning as e:
                    remaining_distance = dist - electric_drive_range
                    if self.gas_capacity == 0:
                        raise Warning("Both Electricity and Combustion Fuels are out!")
                    self.switch_to_combustion()  
                    self.drive(remaining_distance) 
        else:
            raise Warning("Only numbers are accepted!")
        
if __name__ == "__main__":
    try:
        print("Combustion testing")
        c = CombustionCar(40, 8.0)
        print(c.get_remaining_range()) # 500
        c.drive(-10)
        print(c.get_gas_tank_status()) # (38.0, 40.0)
        c.drive(500) # fuel is depleted, Warning raised

    except Warning as warn:
        print("Caught a warning: ",warn)
    
    try:
        print("Electric testing")
        e = ElectricCar(25.0, 500.0)
        e.drive(100.0)
        e.charge(2.0)
        print(e.get_battery_status()) # (22.0, 25)

    except Warning as warn:
        print("Caught a warning: ",warn)

    try:
        print("Hybrid testing")
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(1100.0) # depletes fuel, auto-switch
        print(h.get_gas_tank_status()) # (0.0, 40.0)
        print(h.get_battery_status()) # (20.0, 25.0)

    except Warning as warn:
        print("Caught a warning: ",warn)
    


