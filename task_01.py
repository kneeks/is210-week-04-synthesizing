#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts farenheit to celsius."""


# Import Python libs
import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """
    This function takes the conversion of degrees fahrenheit to celsius

    Args:
        degrees (int): the number of degrees

    Returns:
        int: of the conversion

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(200)
        Decimal('93.33333333333333333333333333')

    """
    celsius = (((decimal.Decimal(degrees) - 32) * 5) / 9)
    return celsius


def celsius_to_kelvin(degrees):
    """
    This function takes the conversion of degrees celsius to kelvin

    Args:
        degrees (int): the number of degrees

    Returns:
        int: of the conversion

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(200)
        Decimal('473.15')

    """
    kelvin = (decimal.Decimal(degrees + ABSOLUTE_DIFFERENCE))
    return kelvin


def farenheit_to_kelvin(degrees):
    """
    This function takes the conversion of degrees farenheit to kelvin

    Args:
        degrees (int): the number of degrees

    Returns:
        int: of the conversion

    Examples:

        >>> farenheit_to_kelvin(212)
        Decimal('373.15')

        >>> farenheit_to_kelvin(41)
        Decimal('278.15')

    """
    kelvin = (fahrenheit_to_celsius(degrees) + celsius_to_kelvin(degrees)
              - degrees)
    return kelvin
