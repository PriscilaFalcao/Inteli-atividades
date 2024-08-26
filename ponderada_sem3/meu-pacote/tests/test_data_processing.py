import unittest
import pandas as pd
from ..data_pipeline.data_processing import process_data, prepare_dataframe_for_insert

class TestDataProcessing(unittest.TestCase):
    def test_process_data(self):
        # Test with sample data
        sample_data = [
            {"fact": "Dogs have three eyelids. The third lid, called a nictitating membrane, keeps the eye lubricated when the dog is swimming."},
            {"fact": "Dogs have better low-light vision than humans."}
        ]
        filename = process_data(sample_data)
        self.assertIsInstance(filename, str)
        self.assertTrue(filename.endswith(".parquet"))

    def test_prepare_dataframe_for_insert(self):
        # Test with sample data
        sample_data = [
            {"fact": "Dogs have three eyelids. The third lid, called a nictitating membrane, keeps the eye lubricated when the dog is swimming."},
            {"fact": "Dogs have better low-light vision than humans."}
        ]
        df = prepare_dataframe_for_insert(sample_data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("data_ingestao", df.columns)
        self.assertIn("dado_linha", df.columns)
        self.assertIn("tag", df.columns)

if __name__ == '__main__':
    unittest.main()