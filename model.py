from sklearn.linear_model import LinearRegression

model = LinearRegression()

def train(X, y):
    model.fit(X, y)
    return model
    
def predict(X):
    return model.predict(X)
