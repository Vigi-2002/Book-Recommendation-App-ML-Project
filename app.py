import streamlit as st
import pandas as pd
import pickle

st.title("Logistic Regression")

def get_features():
	st.sidebar.title("Enter Details")
	cl = st.sidebar.radio('Class', [1,2,3])
	sex = st.sidebar.radio('Gender', [0,1])
	age = st.number_input('Enter Age')
	
	data = {'Pclass' : cl,
		'Sex' : sex,
		'Age' : age,
		}
	
	features = pd.DataFrame(data, index = [0])
	return features
	
x_vals = get_features()

if st.sidebar.button('Submit'):
	st.write(x_vals)
	# Load the model
	loaded_model = pickle.load(open('clf.pkl', 'rb')) 
	res = loaded_model.predict(x_vals)

	if res == 0:
		st.write('Not Survived')
	else:
		st.write('Survived')