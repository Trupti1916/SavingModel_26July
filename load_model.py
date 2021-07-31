import joblib

load_model = joblib.load('dib_79.pkl')

pred = load_model.predict([[10, 20, 30, 40, 50, 60,70, 80]])

if pred[0] == 1:
    print('Person is dibetic')
else:
    print('Person is not dibetic')