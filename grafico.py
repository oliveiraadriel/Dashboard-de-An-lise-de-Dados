import plotly.graph_objects as go

# Dados de exemplo
dados = [10, 20, 30, 40, 50]
fig = go.Figure(data=[go.Bar(x=[1, 2, 3, 4, 5], y=dados)])
fig.show()
