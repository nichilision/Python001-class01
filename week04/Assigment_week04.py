#作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。
#因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
#作业要求：请将以下的 SQL 语句翻译成 pandas 语句：

import pandas as pd 
import numpy as np

data = pd.DataFrame({
    'id':np.arange(1,21),
    'age':np.random.randint(25,100,20)
})

table1 = pd.DataFrame({
    'id':np.arange(1,11),
    'age':np.random.randint(20,100,10)
})

table2 = pd.DataFrame({
    'id':np.arange(1,11),
    'age':np.random.randint(20,100,10)
})


#1. SELECT * FROM data;
print(data)

#2. SELECT * FROM data LIMIT 10;
print(data[:11])

#3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])

#4. SELECT COUNT(id) FROM data;
print(data.id.shape[0])

#5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id']<1000) & (data['age']>30)])

#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;


#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1, table2, on='id'))

#8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1,table2]).reset_index(drop=True))

#9. DELETE FROM table1 WHERE id=10;
table1.drop(table1[table1['id'] == 10].index[0])

#10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(columns=['age'] , axis=1)