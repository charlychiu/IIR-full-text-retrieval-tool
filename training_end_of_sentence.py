from keras.layers import Dense, Dropout, LSTM, Embedding, SimpleRNN
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.models import Sequential, load_model
import pandas as pd
import numpy as np

input_file = 'input.csv'


def load_data(test_split=0.2):
    print('Loading data...')
    df = pd.read_csv(input_file)  # df['text'] df['label']
    df = df.reindex(np.random.permutation(df.index))  # reindex

    train_size = int(len(df) * (1 - test_split))

    X_train = df['text'].values[:train_size]
    y_train = np.array(df['label'].values[:train_size])
    X_test = np.array(df['text'].values[train_size:])
    y_test = np.array(df['label'].values[train_size:])

    token = Tokenizer(filters='')
    token.fit_on_texts(X_train)
    # convert text to vector
    x_train_seq = token.texts_to_sequences(X_train)
    x_test_seq = token.texts_to_sequences(X_test)
    # padding
    MAX_LEN_OF_TOKEN = 50
    x_train = sequence.pad_sequences(x_train_seq, maxlen=MAX_LEN_OF_TOKEN)
    x_test = sequence.pad_sequences(x_test_seq, maxlen=MAX_LEN_OF_TOKEN)

    return x_train, y_train, x_test, y_test


def create_model(input_length):
    print('Creating model...')
    model = Sequential()
    # model.add(Embedding(output_dim=32,
    #                     input_dim=50,
    #                     input_length=input_length))
    # model.add(Flatten())

    model.add(Dense(units=512, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))

    print('Compiling...')
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


X_train, y_train, X_test, y_test = load_data()

model = create_model(len(X_train[0]))

print('Fitting model...')

model.fit(X_train, y_train, batch_size=128, epochs=30, validation_split=0.1, verbose=2)
model.save('eos_model.h5')  # HDF5
#
# score, acc = model.evaluate(X_test, y_test, batch_size=1)
# print('Test score:', score)
# print('Test accuracy:', acc)
#
# del model
# model = load_model('eos_model.h5')
#
# predict_classes = model.predict_classes(X_test).reshape(-1)
# labelDict = {1: 'true', 0: 'false'}
# i = 2
# print('Ground truth: {}; prediction result: {}'.format(labelDict[y_test[i]], labelDict[predict_classes[i]]))
