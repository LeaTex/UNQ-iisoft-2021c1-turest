# desactivo este test porque requiere seleium, lo cual implica que todo el equipo tengo el ambiente configurado correctamente, 
# pero además no se puede ejecutar bien desde GitHub automation


# Feature: Iniciar sesión como cliente
#   Como cliente quiero iniciar sesión para acceder a los servicios del restaurant.

#   Background: user exists and goes to login page
#       Given the user "piggy" is registered in system with password "hambre2021"
#         And the customer go to login page at "/accounts/login/"

#   Scenario: registered customer log in successfully
#        When the customer completes username "piggy" and password "hambre2021" and clicks "Entrar"
#        Then menu with message "Bienvenido" "piggy" is displayed

#   Scenario: registered customer try to log in with wrong password
#        When the customer completes username "piggy" and password "wrong" and clicks "Entrar"
#        Then error message "Usuario y contraseña incorrectos. por favor verifique sus datos y vuelva a intentarlo" is displayed
