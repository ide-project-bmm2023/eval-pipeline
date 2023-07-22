import pandas as pd
from util import Sample, Function, Fail, Result

from typing import Iterable, Dict


def run_eval_pipline(algorithms: Iterable[Function], 
                     loader: Iterable[Sample], 
                     objective_functions: Iterable[Function]) -> Result(Dict[str, pd.DataFrame]):
    pass