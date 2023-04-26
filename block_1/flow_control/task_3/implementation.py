def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    days_31 = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
    days_30 = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
    days_28_or_29 = 'февраль'
    if month in days_31:
        return 31
    elif month in days_30:
        return 30
    elif month in days_28_or_29:
        return 28 or 29
    else:
        return 0
