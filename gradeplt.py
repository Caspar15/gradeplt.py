import os
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
from matplotlib import cm
import numpy as np
from matplotlib.patches import Polygon

# 設定全局字體 (使用 Microsoft JhengHei)
font_path = 'C:/Windows/Fonts/msjh.ttc'
font_prop = FontProperties(fname=font_path)
rcParams['font.sans-serif'] = ['Microsoft JhengHei']
rcParams['axes.unicode_minus'] = False

# 資料
semesters = ['一上', '一下', '二上', '二下', '三上', '三下']
gpa_scores = [2.77, 3.31, 3.73, 4.09, 4.3, 4.28]
ranks_percent = [44.9, 37.3, 17.0, 2.7, 0.7, 4.1]
ranks_numerators = [61, 50, 25, 4, 1, 6]
ranks_denominators = [136, 134, 147, 148, 144, 146]

# 建立排名標註字串
rank_annotations = [f'{num}/{denom} ({percent}%)' for num, denom, percent in zip(ranks_numerators, ranks_denominators, ranks_percent)]

# 使用 seaborn 主題風格
sns.set_theme(style="whitegrid")

# 建立圖表
fig, ax1 = plt.subplots(figsize=(14, 8))

# 設定顏色
gpa_color = sns.color_palette("Set2")[0]
rank_color = sns.color_palette("Set2")[2]

# GPA 曲線
sns.lineplot(x=np.arange(len(semesters)), y=gpa_scores, marker='o', color=gpa_color, markersize=12, linewidth=3, ax=ax1, legend=False)
ax1.set_xlabel('學期', fontsize=18, fontproperties=font_prop)
ax1.set_ylabel('GPA', color=gpa_color, fontsize=18, fontproperties=font_prop)
ax1.tick_params(axis='y', labelcolor=gpa_color)
ax1.set_ylim(2.5, 4.4)
ax1.set_yticks([2.5, 3.0, 3.5, 4.0, 4.3])
ax1.set_xticks(np.arange(len(semesters)))
ax1.set_xticklabels(semesters, fontsize=16, fontproperties=font_prop)

# 在 GPA 曲線上添加標註
for i, gpa in enumerate(gpa_scores):
    ax1.annotate(f'{gpa:.2f}', xy=(i, gpa), xytext=(0, 12), textcoords='offset points',
                 color=gpa_color, fontsize=14, fontproperties=font_prop, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.7))

# 加入第二個 Y 軸用於排名
ax2 = ax1.twinx()
sns.lineplot(x=np.arange(len(semesters)), y=ranks_percent, marker='s', color=rank_color, markersize=12, linewidth=3, ax=ax2, linestyle='--', legend=False)
ax2.set_ylabel('系排名 (%)', color=rank_color, fontsize=18, fontproperties=font_prop)
ax2.tick_params(axis='y', labelcolor=rank_color)
ax2.set_ylim(-5, 50)  # 將下限設為 -5，增加下方空間

# 在系排名曲線上添加標註（包含名次和百分比）
for i, rank in enumerate(ranks_percent):
    # 根據數據點的位置調整標註的垂直偏移，避免重疊
    if rank <= 5:
        offset = 15  # 將標註上移
    else:
        offset = -15 if i % 2 == 0 else 15
    ax2.annotate(rank_annotations[i], xy=(i, rank), xytext=(0, offset), textcoords='offset points',
                 color=rank_color, fontsize=14, fontproperties=font_prop, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.7))

# 圖表標題
plt.title('學業成績曲線圖', fontsize=24, fontweight='bold', fontproperties=font_prop)

# 調整圖例位置，避免遮擋數據
custom_lines = [
    plt.Line2D([0], [0], color=gpa_color, lw=3, marker='o', markersize=12, label='GPA'),
    plt.Line2D([0], [0], color=rank_color, lw=3, linestyle='--', marker='s', markersize=12, label='系排名')
]
ax1.legend(handles=custom_lines, loc='upper center', bbox_to_anchor=(0.5, 1.12),
           fontsize=14, prop=font_prop, frameon=False, ncol=2)

# 增強格線可見性
ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# 添加漸變陰影效果
gpa_gradient = np.linspace(0, 1, len(gpa_scores))
gpa_colors = [cm.get_cmap('Blues')(x) for x in gpa_gradient]
for i in range(len(gpa_scores)-1):
    polygon = Polygon([
        (i, gpa_scores[i]),
        (i+1, gpa_scores[i+1]),
        (i+1, ax1.get_ylim()[0]),
        (i, ax1.get_ylim()[0])
    ], facecolor=gpa_colors[i], edgecolor='none', alpha=0.3)
    ax1.add_patch(polygon)

rank_gradient = np.linspace(0, 1, len(ranks_percent))
rank_colors = [cm.get_cmap('Purples')(x) for x in rank_gradient]
for i in range(len(ranks_percent)-1):
    polygon = Polygon([
        (i, ranks_percent[i]),
        (i+1, ranks_percent[i+1]),
        (i+1, ax2.get_ylim()[0]),
        (i, ax2.get_ylim()[0])
    ], facecolor=rank_colors[i], edgecolor='none', alpha=0.3)
    ax2.add_patch(polygon)

# 調整圖表邊距，防止圖例被截斷
plt.tight_layout(rect=[0, 0, 1, 0.95])

# 在保存圖片之前，檢查目錄是否存在，若不存在則創建
output_dir = 'images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 保存圖片
plt.savefig(os.path.join(output_dir, 'academic_performance.png'), dpi=300, bbox_inches='tight')
plt.show()
