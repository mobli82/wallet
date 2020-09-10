from decimal import Decimal
import math


def calculate_gaz_usage(usage, supplier):
    if usage is None:
        raise ValueError
    
    try:
        vat = (supplier.vat + 100) / 100
        conversion_rate = supplier.conversion_rate
        distribution_fee = supplier.distribution_fee
        gaz_fuel = supplier.gaz_fuel
        subscription_fee = supplier.subscription_fee
        distribution_fee_constant = supplier.distribution_fee_constant

    except KeyError:
        pass
        
    kwh_value = math.ceil(conversion_rate * usage)
    dist_fee = round((kwh_value * float(Decimal(distribution_fee)) * vat), 2)
    fuel_fee = round((kwh_value * float(Decimal(gaz_fuel)) * vat), 2)
    sub_fee = round(float(Decimal(subscription_fee)) * vat, 2)
    dist_fee_const = round(float(Decimal(distribution_fee_constant)) * vat, 2)

    print(dist_fee, fuel_fee, sub_fee, dist_fee_const)

    total = sum([dist_fee, fuel_fee, sub_fee, dist_fee_const])

    return total