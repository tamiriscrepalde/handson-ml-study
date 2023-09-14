"""File containing usefull general functions."""

import os
import tarfile
from urllib import request

from .cfg.config import DOWNLOAD_ROOT, HOUSING_PATH, HOUSING_URL


def fetch_housing_data(
    housing_url: str = HOUSING_URL, housing_path: str = HOUSING_PATH
) -> None:
    """_summary_

    Args:
        housing_url (str, optional): _description_. Defaults to HOUSING_URL.
        housing_path (str, optional): _description_. Defaults to HOUSING_PATH.
    """
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def fetch_california_map() -> None:
    """_summary_"""
    images_path = os.path.join(os.getcwd(), "images", "end_to_end_project")
    os.makedirs(images_path, exist_ok=True)
    url = f"{DOWNLOAD_ROOT}/images/end_to_end_project/california.png"
    request.urlretrieve(url, os.path.join(images_path, "california.png"))
