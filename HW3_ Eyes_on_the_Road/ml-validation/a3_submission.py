"""Submission formatting only; contains no model or model solution."""
from pathlib import Path
import csv
import numpy as np

EXPECTED_IDS = np.arange(45000, 50000, dtype=np.int64)

def export_submission(predictions, ids=None, path='submission.csv'):
    """Export 5,000 integer class predictions, paired with their image IDs."""
    predictions = np.asarray(predictions)
    ids = EXPECTED_IDS.copy() if ids is None else np.asarray(ids)
    if predictions.shape != (5000,) or ids.shape != (5000,):
        raise ValueError('Expected 5,000 class labels and 5,000 IDs; convert logits with argmax(axis=1).')
    if not np.issubdtype(predictions.dtype, np.integer) or not np.issubdtype(ids.dtype, np.integer):
        raise ValueError('Labels and IDs must use integer dtypes.')
    if not np.array_equal(np.sort(ids), EXPECTED_IDS):
        raise ValueError('IDs must contain each integer from 45000 to 49999 exactly once.')
    if np.any((predictions < 0) | (predictions > 9)):
        raise ValueError('Labels must be integers from 0 to 9.')
    order = np.argsort(ids)
    path = Path(path)
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['id', 'label'])
        writer.writerows(zip(ids[order].tolist(), predictions[order].tolist()))
    return path
