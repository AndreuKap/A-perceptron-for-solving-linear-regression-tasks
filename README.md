# A-perceptron-for-solving-linear-regression-tasks

Data Class
The Data class generates training data based on a custom mathematical function and prepares it for model training.

__init__(self, lean, control): Initializes the class with parameters for input and output lengths.
create_mas(self): Generates a normalized dataset based on a custom mathematical function.
create_train(self): Prepares the training data.
Learning Class
The Learning class inherits from Data and is responsible for creating and training the neural network model.

__init__(self, lean, control): Initializes the class with input and output lengths.
training(self): Defines, compiles, and trains the model.
Control Class
The Control class manages the entire process, from data preparation to model evaluation.

__init__(self, model_object): Initializes the class with a Learning object.
contol(self): Trains the model, makes predictions, and evaluates the results.
