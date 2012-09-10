# -*- coding: utf-8 -*-
from trybox.model import Tutorial
from step_01 import step as step01

tutorial = Tutorial(
    title='Django',
    description='Build a web application step by step using an awesome interactive tutorial for Django',
    steps=[
        step01,
    ]
)

