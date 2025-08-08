import numpy as np

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

# 데이터 준비
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

# figure 생성
p = figure(title="sin(x) 함수", x_axis_label='x', y_axis_label='y')

# line glyph 추가
p.line(x, y, legend_label="sin(x)", line_width=2)

# HTML 생성
html = file_html(p, CDN, "sin(x) plot")

# HTML 출력
print(html)
