import models.product as md


def controllerProd():
    prod=md.ModelProd()
    data=prod.getProd()
    return data


def insertProd(data):
    prod=md.ModelProd()
    prod.insertProd(data)