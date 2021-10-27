##
# Tests the weekday.rb script with relevant input

require "./weekday.rb"
include IsItAWeekday

def test_languages
  days = [
    # Spanish
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo",

    # English
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",

    # German
    "montag",
    "dienstag",
    "mittwoch",
    "donnerstag",
    "freitag",
    "samstag",
    "sonntag",

    # French
    "lundi",
    "mardi",
    "mercredi",
    "jeudi",
    "vendredi",
    "samedi",
    "dimanche",

    # Portuguese
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo",

    # Italian
    "lunedì",
    "martedì",
    "mercoledì",
    "giovedì",
    "venerdì",
    "sabato",
    "domenica"
  ]

  (0...days.length).each do |i|
    if i % 7 >= 5
      raise "Error" unless weekend?(days[i])
    else
      raise "Error" unless weekday?(days[i])
    end
  end
end


test_languages
