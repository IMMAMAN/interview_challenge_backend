from models.hoa import HOA
from typing import List
from repository.hoa import add_hoa, get_hoas

def get_all_hoas() -> List[HOA]:
    json_hoas = get_hoas()
    hoas = []

    for hoa in json_hoas:
        h = HOA(hoa.get("id"), hoa.get("name"), hoa.get("address"))
        hoas.append(h)

    return hoas

def add_hoas(hoa_name, hoa_address):
    hoa_id = len(get_hoas()) + 1
    new_hoa = HOA(hoa_id, hoa_name, hoa_address)
    add_hoa(new_hoa)
