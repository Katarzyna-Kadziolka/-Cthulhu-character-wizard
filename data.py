class Data:
    data ={}

    @staticmethod
    def save_data(sv, name):
        try:
            Data.data[name] = int(sv.get())
        except ValueError:
            Data.data[name] = sv.get()