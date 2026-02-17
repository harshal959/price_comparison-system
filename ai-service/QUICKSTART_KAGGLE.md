# 🚀 Quick Start Guide - Kaggle Dataset Integration

## ✅ What's Done

Your system is now ready to use Kaggle datasets! Here's what's been implemented:

- ✅ **Smart 3-Tier Fallback System**:
  1. Your handpicked catalog (20 products)
  2. Kaggle datasets (20,000+ products) with fuzzy matching
  3. Smart Mock Generator with DuckDuckGo pricing

- ✅ **Intelligent Price Comparisons**:
  - Only shows platforms where products actually exist
  - 60% similarity threshold for matching
  - Automatic best price detection

---

## 📥 Next Steps: Download Datasets

### Option 1: Manual Download (Easiest for First Time)

1. **Create Free Kaggle Account**: https://www.kaggle.com/account/login

2. **Download Each Dataset**:
   - **Amazon** (1,465 products): https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset
     - Click "Download All" button
     - Extract `amazon.csv` to `ai-service/data/`
   
   - **Flipkart** (20,000+ products): https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products
     - Download and extract
     - Rename CSV file to `flipkart.csv`
     - Move to `ai-service/data/`
   
   - **Croma** (Electronics): https://www.kaggle.com/datasets/hetulmehta/croma-electronic-products-dataset
     - Download, extract, rename to `croma.csv`
     - Move to `ai-service/data/`
   
      - **Meesho**: https://www.kaggle.com/datasets/darshansingh2000/meesho-product-dataset-india
     - Download, extract, rename to `meesho.csv`
     - Move to `ai-service/data/`

3. **Process the Datasets**:
   ```bash
   cd ai-service
   python load_kaggle_data.py
   ```

4. **Restart Flask Server**:
   ```bash
   # Stop current server (Ctrl+C)
   python app.py
   ```

---

### Option 2: Kaggle CLI (Advanced)

```bash
# Setup (one-time)
pip install kaggle
# Download kaggle.json from https://www.kaggle.com/account -> API -> Create New Token
mkdir C:\Users\harsh\.kaggle
move Downloads\kaggle.json C:\Users\harsh\.kaggle\

# Download all datasets
cd ai-service
kaggle datasets download -d karkavelrajaj/amazon-sales-dataset -p data --unzip
kaggle datasets download -d PromptCloudHQ/flipkart-products -p data --unzip
kaggle datasets download -d hetulmehta/croma-electronic-products-dataset -p data --unzip
kaggle datasets download -d darshansingh2000/meesho-product-dataset-india -p data --unzip

# Rename files if needed
# Then run:
python load_kaggle_data.py
```

---

## 🧪 Testing

Once datasets are downloaded and processed:

1. **Check the index was created**:
   ```bash
   ls ai-service/product_index.json
   ```

2. **Search for a product** (example: "samsung galaxy"):
   - Go to http://localhost:3000
   - Search "samsung galaxy"
   - You should see real prices from multiple platforms!

3. **Check logs** for dataset usage:
   ```
   ✅ Loaded product index with XXXX unique products
   ✅ Found match in index: 'samsung galaxy s24' (similarity: 0.85)
   DEBUG: Using Kaggle dataset for 'samsung'
   ```

---

## 📊 Expected Results

### Before Datasets:
- Searches use Smart Mock Generator
- DuckDuckGo pricing (hit or miss)
- 4 platforms always shown

### After Datasets:
- **20,000+ real products** available
- **Real historical prices** from Kaggle
- **Only relevant platforms shown** (if product doesn't exist on Meesho, it won't show)
- Instant response (no 3-10s scraping delay)

---

## 🐛 Troubleshooting

**Issue**: `⚠️ Product index not found`
- **Solution**: Run `python load_kaggle_data.py` after downloading datasets

**Issue**: CSV files not found during loading
- **Solution**: Check file names match exactly (`amazon.csv`, `flipkart.csv`, etc.)

**Issue**: No products matching searches
- **Solution**: Lower similarity threshold in `scraper.py` (line ~306: change `0.6` to `0.5`)

---

**Status**: Ready to download datasets! 🎉
