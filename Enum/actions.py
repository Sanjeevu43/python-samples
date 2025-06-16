from enum import Enum

class Actions(Enum):
    PAYEE_NAME_ACTION = "PAYEE_NAME_SCORING"
    LARCAR_ACTION = "LARCAR_SCORING"
    DATE_ACTION = "DATE_VALIDATION"
    CAR_ACTION = "CAR_VALUE"
    SIG_ACTION = "SIGNATURE"
    "CODE"

action = Actions.SIG_ACTION.value
print('Given Action is :', action)
action_name = Actions.SIG_ACTION.name
print('Given Action is :', action_name)

match action:
    case "PAYEE_NAME_SCORING":
        print('Payee Name Action')
    case _ :
        print('Action not matched')

all_actions = [action for action in Actions]

print(all_actions)

