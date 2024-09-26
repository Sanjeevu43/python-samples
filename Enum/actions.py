from enum import Enum

class Actions(Enum):
    PAYEE_NAME_ACTION = "PAYEE_NAME_SCORING"
    LARCAR_ACTION = "LARCAR_SCORING"
    DATE_ACTION = "DATE_VALIDATION"
    CAR_ACTION = "CAR_VALUE"
    SIG_ACTION = "SIGNATURE"

action = Actions.SIG_ACTION
print('Given Action is :', action)

match action:
    case "PAYEE_NAME_SCORING":
        print('Payee Name Action')
    case _ :
        print('Action not matched')

