##
# Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
# Languages supported:
# -English
# -German
# -Spanish
# -French

module IsItAWeekday
  def weekday?(day)
    day.downcase!
    if "ghy".include? day[-1]
      return day[0] != "s"
    elsif "iesoa".include? day[-1]
      return !("mb".include? day[2])
    end
    true
  end


  def weekend?(day)
    !weekday?(day)
  end
end