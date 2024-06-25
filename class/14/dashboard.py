
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2,
                    subplot_titles=("折線圖", "柱狀圖", "散點圖", "餅圖"),
                    specs=[[{'type': 'xy'}, {'type': 'xy'}], [{'type': 'xy'}, {'type': 'domain'}]])

# 折線圖
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 3, 5, 7, 11], mode='lines+markers'), row=1, col=1)

# 柱狀圖
fig.add_trace(go.Bar(x=['A', 'B', 'C', 'D'], y=[5, 7, 3, 8]), row=1, col=2)

# 散點圖
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 3, 5, 7, 11], mode='markers'), row=2, col=1)

# 餅圖
labels = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]
fig.add_trace(go.Pie(labels=labels, values=values), row=2, col=2)

fig.update_layout(title_text="多圖表儀表盤")
fig.show()
