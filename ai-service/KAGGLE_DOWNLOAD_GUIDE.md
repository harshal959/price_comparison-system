# Kaggle Dataset Download Instructions

## 📥 Step-by-Step Guide

### Prerequisites
1. Create a Kaggle account: https://www.kaggle.com/account/login
2. Go to Kaggle → Account → API → Create New API Token
3. This downloads `kaggle.json` to your downloads folder

### Setup Kaggle CLI

```bash
# Install Kaggle CLI
pip install kaggle

# Move kaggle.json to the right location
# Windows:
mkdir C:\Users\harsh\.kaggle
move Downloads\kaggle.json C:\Users\harsh\.kaggle\

# Linux/Mac:
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Download All Datasets

```bash
cd ai-service

# 1. Amazon Sales Dataset (1,465 products)
kaggle datasets download -d karkavelrajaj/amazon-sales-dataset
unzip amazon-sales-dataset.zip -d data/
mv data/amazon.csv data/amazon.csv

# 2. Flipkart Products Dataset (20,000+ products)
kaggle datasets download -d PromptCloudHQ/flipkart-products
unzip flipkart-products.zip -d data/
mv data/flipkart_com-ecommerce_sample.csv data/flipkart.csv

# 3. Croma Electronics Dataset
kaggle datasets download -d hetulmehta/croma-electronic-products-dataset
unzip croma-electronic-products-dataset.zip -d data/
# Find the CSV file and rename to croma.csv

# 4. Meesho Product Dataset
kaggle datasets download -d darshansingh2000/meesho-product-dataset-india
unzip meesho-product-dataset-india.zip -d data/
# Find the CSV file and rename to meesho.csv

# Clean up zip files
rm *.zip
```

### Expected Files

After download, your `ai-service/data/` folder should have:
- ✅ amazon.csv
- ✅ flipkart.csv
- ✅ croma.csv
- ✅ meesho.csv

---

## 🚀 Quick Start (Manual Download)

If Kaggle CLI doesn't work, manually download from browser:

1. **Amazon**: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset
2. **Flipkart**: https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products
3. **Croma**: https://www.kaggle.com/datasets/hetulmehta/croma-electronic-products-dataset
4. **Meesho**: https://www.kaggle.com/datasets/darshansingh2000/meesho-product-dataset-india

Extract all CSVs to `ai-service/data/` and rename them as shown above.

---

**Next**: Run `python load_kaggle_data.py` to process the datasets!
