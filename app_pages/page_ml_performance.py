import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_evaluate_pkl

def ml_performance_page():
    """ 
    Contents of ml performance page that displays
    saved plots. 
    """
    st.title("Machine Learning Performance")

    st.header("Labels Distribution Between the Sets")
    
    if st.button("Bar Plot"):
        labels_distribution = plt.imread(f"outputs/v2/label_distribution_graph.jpg")
        st.image(labels_distribution, caption="Label distribution for train, validation"
                                              " and test sets.")
    if st.button("Pie Chart"):
        labels_distribution = plt.imread(f"outputs/v2/label_distribution_pie_plot.jpg")
        st.image(labels_distribution, caption="Label distribution pie chart for train, validation"
                                              " and test sets.")
    
    st.success("Even distribution between the labels. The sets have a 70:15:15 split"
               " for train, validation and test sets respectively.")
    
    st.header("Model History")

    st.subheader("Accuracy Plot")

    acc_plot = plt.imread(f"outputs/v2/model_accuracy.jpg")
    st.image(acc_plot, caption="Accuracy plot during model training")

    st.subheader("Loss Plot")
    
    loss_plot = plt.imread(f"outputs/v2/model_loss.jpg")
    st.image(loss_plot, caption="Loss plot during model training")

    st.success("Both plots suggest a normal fit. The accuracy of the"
               " train set does not continue to increase as the validation"
               " set flattens. For the loss plot, the training set rapidly"
               " decreases at first and then begins to flatten, the two lines"
               " growing closer together.")

    st.header("Generalised Performance on Test Set")

    st.dataframe(pd.DataFrame(load_evaluate_pkl("v2"), index=["Loss", "Accuracy"]))

    st.success("The values strongly match that of the train and validation sets so"
               " there is no overfitting. The accuracy is over 97% and fulfills the"
               " business requirements.")