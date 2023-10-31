"""File containing usefull general functions."""

import os
import tarfile
from urllib import request

from .cfg.config import DOWNLOAD_ROOT, HOUSING_PATH, HOUSING_URL


def fetch_housing_data(
    housing_url: str = HOUSING_URL, housing_path: str = HOUSING_PATH
) -> None:
    """Retrieve housing data from URL.

    This function is from Aurélien Geron (@ageron), in the Github repository handson-ml2
    (https://github.com/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb).

    Args:
        housing_url (str, optional): The URL from where to retrieve the data.
            Defaults to HOUSING_URL.
        housing_path (str, optional): The path of the data. Defaults to HOUSING_PATH.
    """
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def fetch_california_map() -> None:
    """Retrieve California map.

    This function is from Aurélien Geron (@ageron), in the Github repository handson-ml2
    (https://github.com/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb).
    """
    images_path = os.path.join(os.getcwd(), "images", "end_to_end_project")
    os.makedirs(images_path, exist_ok=True)
    url = f"{DOWNLOAD_ROOT}/images/end_to_end_project/california.png"
    request.urlretrieve(url, os.path.join(images_path, "california.png"))
