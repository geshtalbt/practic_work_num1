import math

G0 = 9.80665

def delta_v(m0, m1, isp=300):
    """Формула Циолковского, м/с."""
    if m1 <= 0 or m0 < m1:
        raise ValueError("Требуется m0 >= m1 > 0")
    return isp * G0 * math.log(m0 / m1)

def flight_time(distance_km, accel):
    """Время перелёта в часах: разгон на полпути + торможение."""
    if distance_km <= 0 or accel <= 0:
        raise ValueError("Дистанция и ускорение должны быть положительными")
    distance_m = distance_km * 1000.0
    half_dist = distance_m / 2.0
    # t = 2 * sqrt(d_half / a) в секундах, перевод в часы (/ 3600)
    time_sec = 2.0 * math.sqrt(half_dist / accel)
    return time_sec / 3600.0

def fuel_needed(m_dry, target_dv, isp=300):
    """Масса топлива для заданного dv (обратная формула Циолковского)."""
    if m_dry <= 0 or target_dv < 0 or isp <= 0:
        raise ValueError("Некорректные параметры для расчёта топлива")
    return m_dry * (math.exp(target_dv / (isp * G0)) - 1.0)