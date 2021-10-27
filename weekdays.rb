##
# Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
# Languages supported:
# -English
# -German
# -Spanish
# -French
module IsItAWeekday

  # Checks if a string is the name of a weekday in the supported languages.
  # @param [String] day Any string, ideally one that actually represents a day
  # @return [Boolean] True if it is a weekday.
  def weekday?(day)
    day.downcase!
    if "ghy".include? day[-1]
      return day[0] != "s"
    elsif "iesoa".include? day[-1]
      return !("mb".include? day[2])
    end
    true
  end


  # Checks if a string is the name of a weekend in the supported languages.
  # @param [String] day Any string, ideally one that actually represents a day
  # @return [Boolean] True if it is a weekend.
  def weekend?(day)
    !weekday?(day)
  end

end