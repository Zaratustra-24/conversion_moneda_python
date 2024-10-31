# Paso 1: Definir el valor a tual del Euto y Dólar con respecto al Peso mexicano

tipo_cambio_eur_a_mxn = 23.70 #En un caso mas realista habría que consumir informaciónactualizada de una BBDD o API
tipo_cambio_usd_a_mxn = 20.75 #En un caso mas realista habría que consumir informaciónactualizada de una BBDD o API

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ")

# Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el cambio correspondiente
# Paso 5: Mostrar el resultado de la conversión al usuario 

if tipo_conversion.upper() == "EUR":
    resultado= monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es: ", resultado)
else:
    print ("No está diponible este tipo de conversión actualmente")