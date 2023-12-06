class Home:
    def new(self, value):
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Аргумент может быть только целым числом")

