class Cargo:
    def __init__(self, name: str, weight: float):
        self.name = name          # Название груза
        self.weight = weight      # Вес груза в тоннах

    def get_cargo_type(self) -> str:
        return "Общий груз"

class PalletCargo(Cargo):
    def __init__(self, name: str, weight: float, pallet_count: int):
        super().__init__(name, weight)
        self.pallet_count = pallet_count  # Количество паллет

    def get_cargo_type(self) -> str:
        return "Паллетный"

class BulkCargo(Cargo):
    def __init__(self, name: str, weight: float, volume_m3: float):
        super().__init__(name, weight)
        self.volume_m3 = volume_m3        # Объем в кубических метрах

    def get_cargo_type(self) -> str:
        return "Насыпной"

class LiquidCargo(Cargo):
    def __init__(self, name: str, weight: float, temperature_required: bool):
        super().__init__(name, weight)
        self.temperature_required = temperature_required  # Нужен ли подогрев/охлаждение

    def get_cargo_type(self) -> str:
        return "Наливной"

class Truck:
    def __init__(self, brand: str, body_type: str, max_capacity: float):
        self.brand = brand                  # Марка грузовика
        self.body_type = body_type          # Тип кузова ("Тент", "Самосвал", "Цистерна")
        self.max_capacity = max_capacity    # Максимальная грузоподъемность в тоннах
        self.current_cargo = None           # Текущий загруженный груз (изначально пусто)

    def _is_body_compatible(self, cargo: Cargo) -> bool:
        cargo_type = cargo.get_cargo_type()
        
        if cargo_type == "Паллетный" and self.body_type == "Тент":
            return True
        if cargo_type == "Насыпной" and self.body_type == "Самосвал":
            return True
        if cargo_type == "Наливной" and self.body_type == "Цистерна":
            return True
        return False

    def load(self, cargo: Cargo):
        print(f"\nПопытка загрузить [{cargo.name}] ({cargo.get_cargo_type()}) весом {cargo.weight} т в грузовик {self.brand} ({self.body_type})...")
        
        if self.current_cargo is not None:
            print(f"Ошибка: Грузовик {self.brand} уже занят грузом {self.current_cargo.name}!")
            return

        if not self._is_body_compatible(cargo):
            print(f"Ошибка: Тип кузова '{self.body_type}' не подходит для типа груза '{cargo.get_cargo_type()}'!")
            return

        if cargo.weight > self.max_capacity:
            print(f"Ошибка: Вес груза ({cargo.weight} т) превышает лимит грузовика ({self.max_capacity} т)!")
            return

        self.current_cargo = cargo
        print(f"Успешно: Груз '{cargo.name}' загружен.")

    def unload(self):
        if self.current_cargo is None:
            print(f"Грузовик {self.brand} и так пустой.")
        else:
            print(f"Груз '{self.current_cargo.name}' успешно разгружен из {self.brand}.")
            self.current_cargo = None

if __name__ == "__main__":
    print("=== 1. СОЗДАНИЕ ГРУЗОВ ===")
    cargo1 = PalletCargo("Коробки с техникой", 8.5, 16)      # Паллетный
    cargo2 = BulkCargo("Речной песок", 22.0, 15.0)           # Насыпной
    cargo3 = LiquidCargo("Свежее молоко", 12.0, True)        # Наливной
    cargo4 = PalletCargo("Тяжелое оборудование", 35.0, 4)    # Паллетный (слишком тяжелый)

    print("=== 2. СОЗДАНИЕ АВТОПАРКА ===")
    curtain_truck = Truck("Камаз Neo", "Тент", 20.0)
    tipper_truck = Truck("Scania P410", "Самосвал", 25.0)
    tanker_truck = Truck("MAN TGS", "Цистерна", 15.0)

    print("\n=== 3. ПРОВЕРКА ЛОГИКИ И ПОЛИМОРФИЗМА ===")
    
    curtain_truck.load(cargo3)
    
    curtain_truck.load(cargo1)
    
    curtain_truck.load(cargo2)
    
    tipper_truck.load(cargo2)

    tanker_truck.load(cargo4)
    
    tanker_truck.load(cargo3)