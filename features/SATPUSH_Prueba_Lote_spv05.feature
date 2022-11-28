# language: es
    Característica: Se envía un mensaje del tipo Sat push y se graba la información de las líneas con la fecha, código y texto enviado en la tabla parametrizada en el proceso.

    Escenario: PRYSAS-601   TC_003_Ejecución de campaña SATPUSH_Prueba_Lote_spv05 con más de un código de envío.
    Dado La linea "3516852322" se encuentre existente en la tabla sas_dm.ar_abt_campaign
    Y se encuentre existente en la tabla AR_aux.OFFERS_MATRIX
    Cuando Se ejecute la campaña SATPUSH_Prueba_Lote_spv05_Automation
    Entonces Se envía un mensaje del tipo Sat push y se inserta un registro en la tabla AR_AUX.EXECUTED_HISTORICO_DYNAMO