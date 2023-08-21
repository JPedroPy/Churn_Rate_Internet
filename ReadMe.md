# Churn Rate Internet
An analysis of data regarding the churn of an internet service provided by a company, aiming to comprehend issues and enhance churn rate.

## _Stages of Analysis_
[1. Define the problem]()

[2. Collect Data]()

[3. Data Cleaning and Preprocessing]()

[4. Data Analysis Techniques]()

[5. Exploratory Data Analysis (EDA) and Interpretation of Results]()

[6. Conclusion and Recommendations]()

### _1. Define the problem_ [⬆️ Return]()
In this study, we will analyze various variables related to an internet company, with the goal of examining the cancellation rate and implementing improvements to minimize this rate. The mentioned variables are:

- CustomerID
- Age
- Gender
- Tenure
- Usage Frequency
- Calls to the Call Center
- Days of Delay
- Subscription
- Contract Duration
- Total Spent
- Months since last interaction
- Churned

### _2. Collect Data_ [⬆️ Return]()
The data was extracted from the file `cancelations.csv`

### _3. Data Cleaning and Preprocessing_ [⬆️ Return]()
Using the library [pandas](https://pandas.pydata.org/docs/) to import and interprete the data:

    import pandas as pd
    
    internet_df = pd.read_csv('cancelations.csv')
    internet_df.info()
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 881666 entries, 0 to 881665
    Data columns (total 12 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   CustomerID              881664 non-null  float64
     1   idade                   881664 non-null  float64
     2   sexo                    881664 non-null  object 
     3   tempo_como_cliente      881663 non-null  float64
     4   frequencia_uso          881663 non-null  float64
     5   ligacoes_callcenter     881664 non-null  float64
     6   dias_atraso             881664 non-null  float64
     7   assinatura              881661 non-null  object 
     8   duracao_contrato        881663 non-null  object 
     9   total_gasto             881664 non-null  float64
     10  meses_ultima_interacao  881664 non-null  float64
     11  cancelou                881664 non-null  float64
      
Checking if there's NaN values:

    internet_df.isna().sum()
  
    CustomerID                2
    idade                     2
    sexo                      2
    tempo_como_cliente        3
    frequencia_uso            3
    ligacoes_callcenter       2
    dias_atraso               2
    assinatura                5
    duracao_contrato          3
    total_gasto               2
    meses_ultima_interacao    2
    cancelou                  2

As all columns contain null values, we will use the `.dropna()` function to remove all empty rows:

    internet_df = internet_df.dropna()

Removing the customer ID column (irrelevant):

    internet_df = internet_df.drop('CustomerID', axis=1)
    internet_df.info()
    
    <class 'pandas.core.frame.DataFrame'>
    Index: 881659 entries, 0 to 881665
    Data columns (total 11 columns):
     #   Column                  Non-Null Count   Dtype  
    ---  ------                  --------------   -----  
     0   idade                   881659 non-null  float64
     1   sexo                    881659 non-null  object 
     2   tempo_como_cliente      881659 non-null  float64
     3   frequencia_uso          881659 non-null  float64
     4   ligacoes_callcenter     881659 non-null  float64
     5   dias_atraso             881659 non-null  float64
     6   assinatura              881659 non-null  object 
     7   duracao_contrato        881659 non-null  object 
     8   total_gasto             881659 non-null  float64
     9   meses_ultima_interacao  881659 non-null  float64
     10  cancelou                881659 non-null  float64

### _Initial churn rate_
    qtd_cancel = internet_df['cancelou'].value_counts(normalize = True)
    
    cancelou
    1.0    0.567105
    0.0    0.432895

With `1.0` representing `Yes` and `0.0` representing `No`, we observe that `56.71%` of the customers have canceled the service.

### _4. Data Analysis Techniques_ [⬆️ Return]()
Histogram charts will be used to analyze correlations between variables.

### _5. Exploratory Data Analysis (EDA) and Interpretation of Results_ [⬆️ Return]()
To aid in understanding the reasons contributing to a higher cancellation rate of services, histogram charts were generated, with the dependent variable being 'cancelou'. This analysis aims to examine how other variables impact churn. Therefore:

    colors = {1.0:'red', 0.0:'green'}
    
    for coluna in internet_df.columns:
        graphic = px.histogram(internet_df, x = coluna, color = 'cancelou', color_discrete_map = colors)
        graphic.show()
        
Analyzing the generated charts, some of them exhibited intriguing patterns: `idade`, `total_gasto`, `ligacoes_callcenter`, `assinatura` and `dias_atraso`. 

### _Idade_
![idade](https://github.com/JPedroPy/Churn_Rate_Internet/assets/141521444/434b35c6-39d6-460a-8986-80cd2f0d0b48)

Notice that customers `above 50 years old` consistently cancel the service.

### _Total_Gasto_
![total_gasto](https://github.com/JPedroPy/Churn_Rate_Internet/assets/141521444/0d0b5dc8-0adf-4c68-9707-e6789ede2293)

Observe that services with spending amounts `below 497.5` are consistently canceled.

### _Ligacoes_Callcenter_
![callcenter](https://github.com/JPedroPy/Churn_Rate_Internet/assets/141521444/8766b304-6cb3-4d1e-950e-525ab7073e45)

Statistically, in almost all instances where customers called `5 times or more`, they churned.

### _Assinatura_
![monthly](https://github.com/JPedroPy/Churn_Rate_Internet/assets/141521444/d91912ea-5603-4b21-8e89-6ff1398003b8)

All `monthly` subscriptions are canceled.

### _Dias_Atraso_
![dias_atraso](https://github.com/JPedroPy/Churn_Rate_Internet/assets/141521444/c2de6ae4-e822-49dd-9a0b-e5e19dd13a90)

When the payment is delayed by `more than 20 days`, customers churn.

### _Applying the suggested filters_
    internet_df = internet_df[internet_df['duracao_contrato'] != 'Monthly']
    internet_df = internet_df[internet_df['idade'] <= 50.00]
    internet_df = internet_df[internet_df['ligacoes_callcenter'] <= 4.00]
    internet_df = internet_df[internet_df['dias_atraso'] <= 20.00]
    internet_df = internet_df[internet_df['total_gasto'] >= 497.50]
    qtd_cancel = internet_df['cancelou'].value_counts(normalize = True)

    cancelou
    0.0    0.951529
    1.0    0.048471

Thus, with the implemented changes, it can be observed that the cancellation rate is now only `4.85%`.

### _6. Conclusion and Recommendations_ [⬆️ Return]()

Considering the obtained results, some insights can be drawn:

- `Monthly` contracts should be completely `eliminated`.
- Advertising efforts should be `focused` on customers `below the age of 50`, given that older customers consistently cancel.
- `Avoid` customers making `more than 4 calls`, implying that the call center should prioritize customers who are nearing the 4-call mark.
- `Preventing delays` from `exceeding 20 days`, by offering conditions that encourage customers to make payments when the delay extends.
- Exploring ways to increase the `total spent` to a `minimum of 497.50`.

Taking these actions, we have observed that the cancellations, which previously stood at `56.71%`, have now reduced to `4.85%`, an almost negligible value. This highlights that the mentioned actions are indeed effective.


