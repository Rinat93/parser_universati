class FormatText:
    """
        Обработка текста, форматирование.
    """

    @staticmethod
    def format_for_p(elem):
        pass

    @staticmethod
    def format_for_a(elem):
        pass

    @staticmethod
    def format_for_title(elem):
        pass

    @staticmethod
    def _add_empty_line(elem):
        elem.insert_after(soup.new_tag('br'))
        elem.insert_after(soup.new_tag('br'))