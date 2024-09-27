# 學業成績曲線圖

此項目使用 Python 的 Matplotlib 和 Seaborn 庫，繪製了一個展示 GPA 和系排名變化的學業成績曲線圖。圖表美觀，具有漸變陰影效果，可視化您的學習成果。

## 目錄

- [功能介紹](#功能介紹)
- [環境要求](#環境要求)
- [安裝指南](#安裝指南)
- [使用方法](#使用方法)
- [代碼說明](#代碼說明)
- [效果展示](#效果展示)
- [常見問題](#常見問題)
- [貢獻指南](#貢獻指南)
- [授權條款](#授權條款)

## 功能介紹

- **雙 Y 軸曲線圖**：同時展示 GPA 和系排名的變化趨勢。
- **數據標註**：在數據點上顯示具體的 GPA 值和排名詳細信息。
- **漸變陰影效果**：為曲線下方添加漸變色陰影，增強視覺效果。
- **自適應標註位置**：智能調整標註位置，避免與數據點或軸標籤重疊。
- **美觀的主題和配色**：使用 Seaborn 的主題風格和協調的配色方案。

## 環境要求

- Python 3.x
- 安裝以下 Python 庫：
  - Matplotlib
  - Seaborn
  - NumPy

## 安裝指南

1. **克隆或下載此項目**：

   ```bash
   git clone https://github.com/yourusername/academic-performance-plot.git
   ```

2. **安裝所需的 Python 庫**：

   使用 `pip` 安裝：

   ```bash
   pip install matplotlib seaborn numpy
   ```

3. **確保您的系統中安裝了 Microsoft JhengHei 字體**：

   - 在 Windows 系統中，通常已預裝。
   - 如果沒有，請下載並安裝該字體，或修改代碼使用您系統中的其他中文字體。

## 使用方法

1. **運行代碼**：

   在命令行或終端中，導航到代碼所在目錄，運行：

   ```bash
   python your_script_name.py
   ```

2. **查看圖表**：

   程序運行後，將彈出一個窗口顯示繪製的學業成績曲線圖。

## 代碼說明

- **導入庫**：

  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  from matplotlib import rcParams
  from matplotlib.font_manager import FontProperties
  from matplotlib import cm
  import numpy as np
  ```

- **字體設定**：

  使用 `Microsoft JhengHei` 字體顯示中文標籤。

- **數據準備**：

  ```python
  semesters = ['一上', '一下', '二上', '二下', '三上', '三下']
  gpa_scores = [2.77, 3.31, 3.73, 4.09, 4.3, 4.28]
  ranks_percent = [44.9, 37.3, 17.0, 2.7, 0.7, 4.1]
  ranks_numerators = [61, 50, 25, 4, 1, 6]
  ranks_denominators = [136, 134, 147, 148, 144, 146]
  ```

- **建立排名標註字串**：

  將名次和百分比組合成標註文本。

- **繪製 GPA 曲線**：

  使用左側 Y 軸，並添加數據標註。

- **繪製排名曲線**：

  使用右側 Y 軸，並添加包含名次和百分比的數據標註。

- **添加漸變陰影效果**：

  為兩條曲線下方添加漸變色陰影，增強視覺效果。

- **美化圖表**：

  設置標題、軸標籤、圖例和格線等，使圖表更加美觀。

## 效果展示

![學業成績曲線圖](爬蟲\gradeplt\images\academic_performance.png)

*圖：學業成績曲線圖示例*

## 常見問題

### 1. 運行代碼時出現字體相關的錯誤怎麼辦？

請確保您的系統中安裝了代碼中指定的字體，或修改代碼中的 `font_path` 為您系統中可用的中文字體。

### 2. 如何修改數據？

您可以直接在代碼中修改 `semesters`、`gpa_scores`、`ranks_percent`、`ranks_numerators` 和 `ranks_denominators` 這些列表，以替換為您的實際數據。

### 3. 圖表中的文字顯示為亂碼或方框怎麼辦？

這通常是字體問題，請確保正確設置了中文字體，並且代碼中指定的字體在您的系統中可用。

## 貢獻指南

歡迎對此項目提出意見或建議，您可以：

- 提交問題（Issue）
- 發送拉取請求（Pull Request）
- 聯繫項目作者


**作者**：Caspar15

**聯繫方式**：caspar9202166422@gmail.com
