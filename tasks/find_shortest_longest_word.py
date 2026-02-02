__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    # Разбиваем текст на слова
    words = [word for word in text.split() if word]  # если вдруг будут пустые строки
    
    if not words:
        return (None, None)
    
    # Инициализируем первым словом
    shortest = words[0]
    longest = words[0]
    
    # Проходим по всем словам
    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    
    return (shortest, longest)