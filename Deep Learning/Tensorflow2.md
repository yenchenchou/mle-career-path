# TensorFlow API Utilization Notes & Feedbacks

## Save and load model
### 1. Saving weights

### 2. Saving model graph

### 3. Saving model architecture, weights, state of the optimizer (tensorflow==2.3.*)

#### Saving
* common all methods in this version output the same file and same folder structure
 
1. Model.save()
    * def: Saves the model to Tensorflow SavedModel or a single HDF5 file
    * it allows tools like Tensorflow Serving to reason about the relative freshness
       
2. tf.keras.models.save_model()
    * def: Saves the model to Tensorflow SavedModel or a single HDF5 file
    * it allows tools like Tensorflow Serving to reason about the relative freshness

3. tf.saved_model.save()
    * def: Exports the Trackable object `obj` to SavedModel format
    * it allows tools like Tensorflow Serving to reason about the relative freshness
    
#### Loading

1. tf.keras.models.load_model() / keras.models.load_model()*
    * Def: Loads a model saved via `model.save()` / `tf.keras.models.save_model()` / `tf.saved_model.save()`. Returns a 
    keras object 
    * Return the model and corresponding weight and configuration
    * You can use `model.get_weights()`, `model.variables`, `model.get_layer()` for advanced tweaks
    * During prediction, still need to use method `predict()`
    * For example, `model.get_layer(name="GRU")` is a way when `reset_state()` does not need to clean the entire matrix
    
2. tf.saved_model.load()
    * Def: Load a SavedModel from `export_dir`.  The object returned by tf.saved_model.load is not a Keras object 
    (i.e. doesn't have .fit, .predict, etc. methods). A few attributes and functions are still available. This is 
    particular for production convenience - Tensorflow Serving
    * This object does not need predict and does not restrict by different batch size during training and prediction.
    The input format is almost same as `predict()` is Keras object. The only difference is that keras object accept 
    array-liked data types but `tf.saved_model.load()` only accept tensors.
    * For example, before feed into the a CNN model, these are all acceptable since they are all tensors
    
    ```
    x1 = tf.expand_dims(train_images[0].astype('float32'), axis=0)
    x2 = [np.array(train_images[0])]
    x3 = np.expand_dims(train_images[0], axis=0)
    ```

    

