from pydantic import BaseModel, confloat

class GastoBase(BaseModel):
    id_gasto: int
    paquete_id: int
    monto_iva_quetzal: confloat(gt=0)
    monto_dai_quetzal: confloat(gt=0)
    monto_flete: confloat(gt=0)
    monto_combex: confloat(gt=0)
    valor_quetzal: confloat(gt=0)
    gasto_total: confloat(gt=0)

    class Config:
        orm_mode = True