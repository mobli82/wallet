from decimal import Decimal

from suppliers.models import PowerSupplierModel

def calculate_montlhy_power_cost(*args, **kwargs):
    try:
        usage = kwargs.get('usage')
        user = kwargs.get('user')

    except KeyError as error:
        print(error)

    energa = PowerSupplierModel.objects.filter(owner=user).first()

    try:
        vat = (energa.vat + 100) / 100
        energy_fee = energa.energy_fee
        subscription_fee = energa.subscription_fee
        network_fee_constant = energa.network_fee_constant
        network_fee_24_7 = energa.network_fee_24_7
        quality_fee = energa.quality_fee
        cogeneration_fee = energa.cogeneration_fee
        transitional_fee = energa.transitional_fee
    
    except AttributeError as error:
        print(error)

    energy_fee = round((Decimal(usage) * Decimal(energy_fee)), 2)
    subscription_fee = round(Decimal(subscription_fee), 2)
    network_fee_constant = round(Decimal(network_fee_constant), 2)
    network_fee_24_7 = round((Decimal(usage) * Decimal(network_fee_24_7)), 2)
    quality_fee = round((Decimal(usage) * Decimal(quality_fee)), 2)
    cogeneration_fee = round((Decimal(usage) * Decimal(cogeneration_fee)), 2)
    transitional_fee = round(Decimal(transitional_fee), 2)
    
    monthly_cost = sum([energy_fee, 
                        subscription_fee,
                        network_fee_24_7, 
                        quality_fee, 
                        cogeneration_fee,
                        network_fee_constant,
                        transitional_fee]) * round(Decimal(vat), 2)

    return round(Decimal(monthly_cost), 2)