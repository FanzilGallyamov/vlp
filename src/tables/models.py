from src.db import Base
import sqlalchemy as sa

class WellData(Base):
    __tablename__ = "well_data"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False, autoincrement=True, comment="Идентификатор скважины")
    MD = sa.Column(sa.Float, nullable=True, comment="Глубина по стволу скважины, м")
    TVD = sa.Column(sa.Float, nullable=True, comment="Вертикальная глубина, м")
    d_casing = sa.Column(sa.Float, nullable=True, comment="Диаметр эксплуатационной колонны")
    d_tubing = sa.Column(sa.Float, nullable=True, comment="Диаметр по колонне насосно-компрессорных труб")
    h_mes = sa.Column(sa.Float, nullable=True, comment="Глубина спуска НКТ, м")
    wct = sa.Column(sa.Float, nullable=True, comment="Обводнённость, %")
    rp = sa.Column(sa.Float, nullable=True, comment="Газовый фактор, м3/т")
    gamma_oil = sa.Column(sa.Float, nullable=True, comment="Относительная плотность нефти")
    gamma_gas = sa.Column(sa.Float, nullable=True, comment="Относительная плотность газа")
    gamma_wat = sa.Column(sa.Float, nullable=True, comment="Относительная плотность воды")
    t_res = sa.Column(sa.Float, nullable=True, comment="Температура пласта, С")
    p_wh = sa.Column(sa.Float, nullable=True, comment="Буферное давление, атм")
    geo_grad = sa.Column(sa.Float, nullable=True, comment="Геотермический градиент, C/100 м")
    h_res = sa.Column(sa.Float, nullable=True, comment="Глубина верхних дыр перфорации, м")


class VLP(Base):
    __tablename__ = "vlp"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False, autoincrement=True, comment="Идентификатор скважины")
    q_liq = sa.Column(sa.String, nullable=True, comment="Дебит жидкости")
    p_wf = sa.Column(sa.String, nullable=True, comment="Забойное давление")
