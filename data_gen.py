from faker import Faker
import pandas as pd

fake = Faker()

col1 = [fake.name() for i in range(100)]

df = pd.DataFrame({"Name": col1})

if __name__ == '__main__':
    print(df.head())
