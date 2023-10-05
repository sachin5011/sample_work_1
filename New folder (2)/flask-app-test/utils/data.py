import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

conn = sqlite3.connect(r"C:/Users/Sachin.Pal/Desktop/flask-app-test/instance/student.db", check_same_thread=False)

def create_df():
    df = pd.read_csv(r"C:/Users/Sachin.Pal/Desktop/flask-app-test/datasets/student-dataset.csv").reset_index(drop=True)
    df.tail(df.shape[0]-1)
    df.rename(columns={
        'ethnic.group': 'ethenic_group',
        'english.grade': 'english_grade', 
        'math.grade': 'math_grade', 
        'sciences.grade': 'sciences_grade',
       'language.grade': 'language_grade', 
       'portfolio.rating': 'portfolio_rating', 
       'coverletter.rating': 'coverletter_rating',
       'refletter.rating': 'refletter_rating'
    }, inplace=True)
    # df.to_sql("Student1", con=conn, index=False, if_exists="replace")
    return df

def getcolumns():
    df = create_df()
    print(df.columns)




def analysis():
    df = create_df()
    img = BytesIO()
    df_plot = df[["name", "nationality", 'city', 'latitude', 'longitude', 'gender']]
    
    plt.plot(sns.catplot(data=df))
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode("utf-8")
    
    return plot_url
    









