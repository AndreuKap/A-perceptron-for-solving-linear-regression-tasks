from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class Data:
    def __init__(self, lean, control):
        self.a = lean
        self.b = control
        self.max_l = 101
        self.x_train, self.y_train = self.create_train()
    
    def create_mas(self):
        def f(t):
            return 5*t**4 - t*t - 1 
        self.time_rad = [(f(i) - f(1)) / (f(self.max_l) - f(1)) for i in range(1, self.max_l)]
        return  self.time_rad

    def create_train(self):
        self.create_mas()
        x_train = [[self.time_rad[i] for i in range(j, j+ self.a, 1)] for j in range(1, self.max_l - 6, self.b)]
        y_train = [[self.time_rad[i] for i in range(j + self.a, j + self.a + self.b)] for j in range(1, self.max_l - 6, self.b)]
        return x_train, y_train
    
class Learning(Data):
    def __init__(self, lean, control):
        super().__init__(lean, control)
        self.inp = lean
        self.onp = control
    
    def training(self):
        model = Sequential([
        Dense(100, input_shape=(self.inp,), activation='relu'),
        Dense(100, activation='relu'),        
        Dense(self.onp, activation='linear')
        ])

        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
        model.fit(np.array(self.x_train), np.array(self.y_train), batch_size=1, epochs=10, validation_split=0.2)
        return model
    
class Control:
    def __init__(self, model_object):
        self.model_object = model_object
    
    def contol(self):
        model = self.model_object.training()
        mas = self.model_object.create_mas()
        input_mas = [mas[i] for i in range(-self.model_object.a, 0)] 
        itog_mas = []
        for _ in range(int(6/self.model_object.b)):
            onput_mas = (model.predict(np.array([input_mas]))[0])
            itog_mas.extend(onput_mas)
            input_mas[-len(onput_mas):] = onput_mas

        for i in range(6):
            print(mas[i + self.model_object.max_l - 7], itog_mas[i])  

        for i in range(6):
            print((abs(itog_mas[i] - mas[i + self.model_object.max_l - 7])/mas[i + self.model_object.max_l - 7])*100)  

        print(mas)



Control(Learning(5, 2)).contol()
