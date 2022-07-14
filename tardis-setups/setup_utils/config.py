import os
import re
from setup_utils.download import download_from_url


def find_file(name, path):
    for dirpath, _, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
    return name


def config_modifier(conf):
    conf["montecarlo"]["nthreads"] = 2
    conf["montecarlo"]["last_no_of_packets"] = 1.0e5
    conf["montecarlo"]["no_of_virtual_packets"] = 3

    print("Config")
    url_check = re.search(
        r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",
        conf["atom_data"],
    )
    print(url_check)
    if url_check:
        conf["atom_data"] = download_from_url(conf["atom_data"])

    else:
        conf["atom_data"] = os.path.join(
            os.path.expanduser("~"), "Downloads", "tardis-data", conf["atom_data"]
        )

    # if os.path.exists(conf["atom_data"]) == False:
    #     conf["atom_data"] = find_file(conf["atom_data"], "/home")
    #     if os.path.exists(conf["atom_data"]) == False:
    #         raise Exception("Atomic dataset not found")

    return conf
