def alarm_clock(day, vacation):
  week_day = day not in (0, 6)

  if vacation:
      return '10:00' if week_day else 'off'

  return '7:00' if week_day else '10:00'
