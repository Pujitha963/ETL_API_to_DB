from extract_data import extract
from transform_data import transform
from load_data import load

def main():
    """Run the ETL process."""
    df = extract()
    transformed = transform(df)
    load(transformed)

if __name__ == '__main__':
    main()