from aiogram import Dispatcher

from loader import dp

from .adminfl import Adminfillter
from .groupfl import IsGroup
from .privetfl import IsPrivate



if __name__ == "filters":

    dp.filters_factory.bind(Adminfillter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)

