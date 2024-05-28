import altair as alt
import pandas as pd

# 创建一个简单的数据集
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 23, 17, 5]
})

# 使用 Altair 创建条形图
chart = alt.Chart(data).mark_bar().encode(
    x='Category',
    y='Value'
)

# 显示图表
chart.display()