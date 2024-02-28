import plotly.express as px
import dataanalise as da

data = da.analisar2();



#data.drop(data.sort_values(by=['cvli'], ascending=False).head(3).index, inplace=True)

#print(data.sort_values(by=['cvli'], ascending=False))


data.drop(columns=['municipio'], inplace=True)

print(data.corr())

fig = px.imshow(data.corr())

fig.show()