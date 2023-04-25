import tensorflow as tf

# Test Tensor
def testTensor ():
    print (f"TensorFlow verision = {tf.__version__}")
    
    # Load the MNIST Dataset
    try:
        mnist                                = tf.keras.datasets.mnist
        print ("\n\nmnist values \n", mnist)
        
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        
        print ("\n\nx-train values \n", x_train, "\n\nx-test values \n",x_test)
        print ("\n\ny-train values \n", y_train, "\n\ny-test values \n", y_test)
        
    except:
        print ("\n\n*** tensorflow load error!\n\n")
        return
    
    # Scale these values to a range of 0 to 1 (float) by dividing the values by 255.0
    x_train, x_test = x_train/255.0, x_test/255.0
    
    print ("\n\nx-train values \n", x_train, "\n\nx-test values \n",x_test)
    print ("\n\ny-train values \n", y_train, "\n\ny-test values \n", y_test)

    # Build a machine learning model
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])
    
    print ("\n\nmodel values \n", model)
    
    # Get our predictions and convert these logits to probabilities 
    predictions = model(x_train[:1]).numpy()
    tf.nn.softmax(predictions).numpy()
    
    #  Define a loss function for training
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    
    # Calculate a scalar loss for each example
    loss_fn(y_train[:1], predictions).numpy()
    
    # Configure and compile the model using Keras
    model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
              
    # Train and evaluate the model
    print ("\nTraining the model...\n")
    model.fit(x_train, y_train, epochs=5)
    
    # Checks the model's performance
    print ("\nEvaluating the model...\n")
    model.evaluate(x_test,  y_test, verbose=2)
    
    # Wrap the trained model and attach the softmax to it to return a probability
    print ("\nReturning model probability...\n")
    probability_model = tf.keras.Sequential([
      model,
      tf.keras.layers.Softmax()
    ])
    print ("\n\nprobability_model values \n", probability_model)
    
    print (probability_model(x_test[:5]))
        
    return
    
# Main
print ("\n\n—BOJ—\n\n")
testTensor ()
print ("\n\n—EOJ—\n\n")
