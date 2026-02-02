__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    if seconds == 0:
        return "00s"
    
    DAY = 86400
    HOUR = 3600
    MINUTE = 60
    
    days = seconds // DAY
    seconds %= DAY
    
    hours = seconds // HOUR
    seconds %= HOUR
    
    minutes = seconds // MINUTE
    seconds %= MINUTE
    

    parts = []
    
    if days > 0:
        parts.append(f"{days:02d}d")

        parts.append(f"{hours:02d}h{minutes:02d}m{seconds:02d}s")
        return "".join(parts)
    
    if hours > 0:
        parts.append(f"{hours:02d}h")

        parts.append(f"{minutes:02d}m{seconds:02d}s")
        return "".join(parts)
    
    if minutes > 0:
        parts.append(f"{minutes:02d}m")

        parts.append(f"{seconds:02d}s")
        return "".join(parts)
    

    return f"{seconds:02d}s"