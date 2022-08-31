from fastapi import APIRouter
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
def calc_vlp(vlp_in: VlpCalcRequest):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    # функция считающая VLP
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa
    parsed = vlp_in.dict()
    # hash_value = hashlib.sha256(vlp_in.json().encode()).hexdigest()

    # initial_data = get_check_vlp_exists(session, hash_value)
    # if not initial_data:
    #     return initial_data

    result = vlp_calculation(parsed['inclinometry'], parsed['casing'], parsed['tubing'], parsed['pvt'],
                             parsed['p_wh'], parsed['geo_grad'], parsed['h_res'])

    # save_vlp_data(get_session(), result)
    return result
    pass
