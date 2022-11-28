import glob
import os
from behave.model_core import Status
global stepPass
global stepFail



def after_scenario(context, scenario):
    global stepFail, stepPass
    f = open('./Logs/' + context.nomArchivo, 'a')

    espacios = 160 - len(scenario.name)
    if scenario.status == Status.failed:
        f.write('\n' "JLR>  {:<10}".format(scenario.name) + '0      1'.rjust(espacios))
        f.close()
        stepFail += 1
    if scenario.status == Status.passed:
        f.write('\n' "JLR>  {:<10}".format(scenario.name) + '1      0'.rjust(espacios))
        f.close()
        stepPass += 1

def before_all(context):
    global stepFail, stepPass
    stepFail=0
    stepPass=0
    files = glob.glob('./Logs/*')
    for f in files: os.remove(f)
    #fecha = datetime.now()
    #fechaHora = fecha.strftime("%d-%m-%Y %H%M%S")
    f = open('./Logs/Logs Status.txt', 'w')
    context.nomArchivo = 'Logs Status.txt'
    f.write('JLR>  ID TSC/TC        NOMBRE TSC/TC                                                                                                                         PASS   FAIL')


def after_all(context):
    global stepFail, stepPass
    f = open('./Logs/' + context.nomArchivo, 'a')
    f.write('\n' "JLR>  TC PASADOS: " + str(stepPass) + "    TC FALLADOS: " + str(stepFail) + "    TC TOTALES: " + str(
        stepPass + stepFail))

    try:
        with open("./Logs/Logs Status.txt", "r") as archivo:
            for linea in archivo:
                print(linea.rstrip())
    except Exception as error:
        print('Error al leer archivo log '+ error)

    print("JLR>  TC PASADOS: " + str(stepPass) + "    TC FALLADOS: " + str(stepFail) + "    TC TOTALES: " + str(
        stepPass + stepFail))