#!/usr/bin/python3
"""
Module comprises a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    
    Args:
        text: input string

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance (text, str):
        raise TypeError("text must be a string")

    st = text[:]

    for i in ".?:":
        list_text = st.split(i)
        st = ""
        for j in list_text:
            j = j.strip(" ")
            st = j + i if st is "" else st + "\n\n" + j + i

    print(st[:-3], end="")
