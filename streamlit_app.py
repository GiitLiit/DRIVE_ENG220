import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("HPSA Score Comparison")

#Main New Mexico Data
NMdata = pd.read_csv("FinalProjectDataPt2.csv")

#print(NMdata.columns.tolist())

#Convert string to numbers
NMdata["HPSA Score"] = pd.to_numeric(NMdata["HPSA Score"], errors="coerce")

#Drop missing values
clean_score_col = NMdata["HPSA Score"].dropna()

st.write("### Average HPSA Score for New Mexico")
st.write(clean_score_col.mean())

#Main California Data
#cali = pd.read_csv("CaliDataFinal.csv")

caliData = pd.read_csv("CaliDataFinal.csv", encoding="latin1")


#Converting if it doesnt work
caliData["HPSA Score"] = pd.to_numeric(caliData["HPSA Score"], errors="coerce")

cali_clean = caliData["HPSA Score"].dropna()

st.write("### Average HPSA Score for California")
st.write(cali_clean.mean())

#Main Massachusetts Data
massData = pd.read_csv("MassachusettsData.csv", encoding="latin1")

#Convert Var8
massData["Unnamed: 7"] = pd.to_numeric(massData["Unnamed: 7"], errors="coerce")

mass_clean = massData["Unnamed: 7"].dropna()

st.write("### Average HPSA Score for Massachusetts")
st.write(mass_clean.mean())

#Plotting
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

#HPSA New Mexico plotting
axs[0].bar(range(len(clean_score_col)), clean_score_col)
axs[0].set_title("HPSA Score Within New Mexico")
axs[0].set_xlabel("Different Disciplines in NM")
axs[0].set_ylabel("HPSA Scores")

#HPSA California plotting
axs[1].bar(range(len(cali_clean)), cali_clean)
axs[1].set_title("HPSA Score Within California")
axs[1].set_xlabel("Different Disciplines in California")
axs[1].set_ylabel("HPSA Scores")

#HPSA Massachusetts plotting
axs[2].bar(range(len(mass_clean)), mass_clean)
axs[2].set_title("HPSA Score Within Massachusetts")
axs[2].set_xlabel("Different Disciplines in Massachusetts")
axs[2].set_ylabel("HPSA Scores")

plt.tight_layout()
plt.show()
