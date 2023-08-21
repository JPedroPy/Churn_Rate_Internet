import pandas as pd
import plotly.express as px

#Importing dataset
internet_df = pd.read_csv('cancelations.csv')
internet_df.info()

#Checking if there's NaN values
internet_df.isna().sum()

#Removing lines without information and irrelevant columns
internet_df = internet_df.dropna()
internet_df = internet_df.drop('CustomerID', axis=1)

#Checking
internet_df.info()

#Checking how cancellations are (study issue)
qtd_cancel = internet_df['cancelou'].value_counts(normalize = True)
print(qtd_cancel)

#Generating graphs to assess cancellation behavior in relation to other variables
colors = {1.0:'red', 0.0:'green'}
for coluna in internet_df.columns:
    graphic = px.histogram(internet_df, x = coluna, color = 'cancelou', color_discrete_map = colors)
    graphic.show()

#Applying improvements
internet_df = internet_df[internet_df['duracao_contrato'] != 'Monthly']
internet_df = internet_df[internet_df['idade'] <= 50]
internet_df = internet_df[internet_df['ligacoes_callcenter'] <= 4]
internet_df = internet_df[internet_df['dias_atraso'] <= 20]
internet_df = internet_df[internet_df['total_gasto'] >= 497.5]
qtd_cancel = internet_df['cancelou'].value_counts(normalize = True)
print(qtd_cancel)
