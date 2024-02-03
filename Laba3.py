class Array3d:
    def __init__(self, dim0, dim1, dim2):
        # Инициализация размеров массива и самого массива данными
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.data = [0] * (dim0 * dim1 * dim2)

    def __getitem__(self, index):
        # Перегрузка оператора [] для доступа к элементам массива
        i, j, k = index
        return self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k]

    def __setitem__(self, index, value):
        # Перегрузка оператора [] для установки значения элемента массива
        i, j, k = index
        self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = value



    def get_values_0(self, i):
        """Метод для получения среза данных по первой оси"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for j in range(self.dim1) for k in range(self.dim2)]

    def get_values_1(self, j):
        """Метод для получения среза данных по второй оси"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0) for k in range(self.dim2)]

    def get_values_2(self, k):
        """Метод для получения среза данных по третьей оси"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0) for j in range(self.dim1)]



    def get_values_01(self, i, j):
        """Метод для получения срезов данных по первой и воторой плоскостяи"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for k in range(self.dim2)]

    def get_values_02(self, i, k):
        """Метод для получения среза данных по первой и третьей плоскостяи"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for j in range(self.dim1)]

    def get_values_12(self, j, k):
        """Метод для получения среза данных по второй и третьей плоскосяти"""
        return [self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] for i in range(self.dim0)]




    def set_values_0(self, i, values):
        """Метод для установки среза данных по первой оси"""
        for j in range(self.dim1):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[j][k]

    def set_values_1(self, j, values):
        """Метод для установки среза данных по второй оси"""
        for i in range(self.dim0):
            for k in range(self.dim2):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i][k]

    def set_values_2(self, k, values):
        """Метод для установки среза данных по третьей оси"""
        for i in range(self.dim0):
            for j in range(self.dim1):
                self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i][j]





    def set_values_01(self, i, j, values):
        """Метод для установки срезов данных по первой и воторой плоскостяи"""
        for k in range(self.dim2):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[k]

    def set_values_02(self, i, k, values):
        """Метод для установки срезов данных по первой и воторой плоскостяи"""
        for j in range(self.dim1):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[j]

    def set_values_12(self, j, k, values):
        """Метод для установки срезов данных по первой и воторой плоскостяи"""
        for i in range(self.dim0):
            self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k] = values[i]



    def ones(self):
        """Метод для установки нулей"""
        self.data = [1] * (self.dim0 * self.dim1 * self.dim2)

    def zeros(self):
        """Метод для установки единиц"""
        self.data = [0] * (self.dim0 * self.dim1 * self.dim2)

    def fill(self, value):
        """Метод для заполнения массива значением"""
        self.data = [value] * (self.dim0 * self.dim1 * self.dim2)



    def array_print(self):
        """Метод для вывода массива в консоль"""
        for i in range(self.dim0):
            print(f"i = {i}")
            for j in range(self.dim1):
                for k in range(self.dim2):
                    print(self.data[i * self.dim1 * self.dim2 + j * self.dim2 + k], end=" ")
                print()
            print()



if __name__ == '__main__':
    # Пример использования
    arr = Array3d(2, 3, 4)

    arr.set_values_0(0, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    arr.set_values_0(1, [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])

    arr.array_print()

    slice = arr.get_values_0(1)

    for i in slice:
        print(i, end=" ")
    print()