from pathlib import Path
import pandas as pd

def validate_filename(path_arg) -> Path:
    """
    Validates that `path_arg` is a filename (no directory)
    and has an extension.
    """
    p = Path(path_arg)

    # 1. Check: No directory components (only a filename)
    if p.parent != Path("."):
        raise ValueError(f"Argument must be a filename, not a path: {path_arg}")

    # 2. Check: It must have a suffix / extension
    if p.suffix == "":
        raise ValueError(f"Filename must have an extension: {path_arg}")

    return p

def validate_extension(ext: str) -> str:
    allowed = [".xlsx", ".csv", ".txt"]

    if ext not in allowed:
        raise ValueError(f"results file must have a valid extension: {allowed}")

    return ext


def validate_pell_columns(df: pd.DataFrame, id_column: str, required_cols: set[str] | None = None) -> None:
    
    # Build default required columns if none supplied
    if required_cols is None:
        required_cols = {
            "AID_YEAR"
       }

    required_cols = set(required_cols)  # convert user input to a set
    required_cols.add(id_column)

    # Now you can use required_cols
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_cohort_columns(df: pd.DataFrame, id_column: str, required_cols: set[str] | None = None) -> None:
    
    # Build default required columns if none supplied
    if required_cols is None:
        required_cols = {
            "Cohort Name"
       }

    required_cols = set(required_cols)  # convert user input to a set
    required_cols.add(id_column)

    # Now you can use required_cols
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_enrollment_columns(df: pd.DataFrame, id_column: str, required_cols: set[str] | None = None) -> None:
    
    # Build default required columns if none supplied
    if required_cols is None:
        required_cols = {
            "Academic Period",
            "Time Status",
            "Student Level",
            "Degree"
        }

    required_cols = set(required_cols)  # convert user input to a set
    required_cols.add(id_column)

    # Now you can use required_cols
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
