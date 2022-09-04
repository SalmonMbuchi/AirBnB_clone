#!/usr/bin/python3
""" this module contains the class User"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ public class attributes:
            email
            password
            first_name
            last_name"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
